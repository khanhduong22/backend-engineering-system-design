import os
import re
import json
import urllib.request
import urllib.error
import time
import zipfile
import sqlite3
import shutil

# 1. Dynamically import or install genanki
try:
    import genanki
except ImportError:
    print("Installing 'genanki' library for Anki packaging...")
    import subprocess
    import sys
    import site
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--break-system-packages", "--user", "genanki"])
        user_site = site.getusersitepackages()
        if user_site not in sys.path:
            sys.path.append(user_site)
        import genanki
        print("genanki successfully installed.")
    except Exception as e:
        print(f"Error installing genanki: {e}")
        print("Please run: pip install genanki")
        sys.exit(1)

def clean_html(text):
    if not text:
        return ""
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<div>', '\n', text)
    text = re.sub(r'</div>', '', text)
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&amp;', '&')
    text = text.replace('&quot;', '"')
    text = re.sub(r'<[^>]+>', '', text)
    return re.sub(r'\n+', '\n', text).strip()

def format_markdown_table_cell(text):
    cleaned = clean_html(text)
    return cleaned.replace('\n', '<br>')

def markdown_to_html(text):
    if not text:
        return ""
    def replace_code_block(match):
        code = match.group(1)
        code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return f'<pre><code>{code.strip()}</code></pre>'
    text = re.sub(r'```(?:\w+)?\n(.*?)\n```', replace_code_block, text, flags=re.DOTALL)
    text = re.sub(r'`([^`\n]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    parts = re.split(r'(<pre>.*?</pre>)', text, flags=re.DOTALL)
    for i in range(len(parts)):
        if not parts[i].startswith("<pre>"):
            parts[i] = parts[i].replace('\n', '<br>')
    return "".join(parts)

def get_field_mappings(models_json):
    try:
        models = json.loads(models_json)
    except Exception:
        return {}
    mappings = {}
    for mid_str, model in models.items():
        try:
            mid = int(mid_str)
            fields = model.get('flds', [])
            
            front_idx = 0
            front_keywords = ['front', 'question', 'vorderseite', 'text', 'name', 'header', 'term', 'word']
            found_front = False
            for kw in front_keywords:
                for f in fields:
                    if kw in f.get('name', '').lower():
                        front_idx = f.get('ord', 0)
                        found_front = True
                        break
                if found_front:
                    break
                    
            back_idx = 1 if len(fields) > 1 else 0
            back_keywords = ['back', 'answer', 'rückseite', 'definition', 'extra', 'explanation', 'meaning']
            found_back = False
            for kw in back_keywords:
                for f in fields:
                    if kw in f.get('name', '').lower():
                        back_idx = f.get('ord', 0)
                        found_back = True
                        break
                if found_back:
                    break
                    
            if front_idx == back_idx and len(fields) > 1:
                for f in fields:
                    if f.get('ord', 0) != front_idx:
                        back_idx = f.get('ord', 0)
                        break
            mappings[mid] = (front_idx, back_idx)
        except Exception:
            continue
    return mappings

def extract_cards_from_apkg(apkg_path):
    filename = os.path.basename(apkg_path)
    deck_key = os.path.splitext(filename)[0]
    temp_dir = os.path.join(os.path.dirname(apkg_path), f"temp_extract_{deck_key}")
    
    print(f"Extracting {filename}...")
    try:
        os.makedirs(temp_dir, exist_ok=True)
        with zipfile.ZipFile(apkg_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    except Exception as e:
        print(f"  Error extracting zip: {e}")
        shutil.rmtree(temp_dir, ignore_errors=True)
        return []

    db_file = None
    for f in ['collection.anki21', 'collection.anki2']:
        p = os.path.join(temp_dir, f)
        if os.path.exists(p):
            db_file = p
            break
            
    if not db_file:
        print("  Error: SQLite collection database not found.")
        shutil.rmtree(temp_dir, ignore_errors=True)
        return []

    cards_list = []
    deck_name = deck_key
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        field_mappings = {}
        try:
            cursor.execute('select models from col')
            row = cursor.fetchone()
            if row:
                field_mappings = get_field_mappings(row[0])
                
                cursor.execute('select decks from col')
                deck_row = cursor.fetchone()
                if deck_row:
                    decks = json.loads(deck_row[0])
                    deck_names = [d['name'] for d in decks.values() if d.get('name') != 'Default']
                    if deck_names:
                        deck_name = deck_names[0]
        except Exception as e:
            print(f"  Warning retrieving models metadata: {e}")
            
        cursor.execute('''
            select n.mid, n.flds
            from notes n
            join cards c on c.nid = n.id
            order by n.id
        ''')
        
        for row in cursor.fetchall():
            mid, flds = row
            fields = flds.split('\x1f')
            front_idx, back_idx = field_mappings.get(mid, (0, 1 if len(fields) > 1 else 0))
            front = fields[front_idx] if front_idx < len(fields) else (fields[0] if fields else "")
            back = fields[back_idx] if back_idx < len(fields) else (fields[1] if len(fields) > 1 else (fields[0] if fields else ""))
            
            cards_list.append({
                'deck': deck_name,
                'question': front,
                'answer': back
            })
        conn.close()
    except Exception as e:
        print(f"  Error reading database: {e}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
        
    return cards_list

def call_gemini_api(api_key, cards_batch, batch_num, total_batches):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent?key=" + api_key
    
    prompt = """You are a professional database administrator and educator specializing in PostgreSQL. Your task is to clean, deduplicate, categorize, and classify the difficulty of a list of PostgreSQL flashcards.

INPUT FORMAT:
You will receive a JSON list of flashcards. Each card has a temporary 'id', 'question', and 'answer'.

TASKS:
1. Deduplicate: Identify cards with the same semantic meaning or very similar questions. Merge them into a single card.
   - Keep the most clear and descriptive question.
   - Combine details from both answers if they complement each other to create a thorough, high-quality answer.
2. Categorize: Assign each card to exactly one of the following categories:
   - 'Basic SQL & Syntax'
   - 'Joins & Set Operators'
   - 'Subqueries & Aggregations'
   - 'Database Design & Normalization'
   - 'Transactions & Concurrency'
   - 'Database Programmability' (Triggers, Views, Functions, Procedures)
   - 'Performance & Indexing'
   - 'Advanced & Distributed Databases'
3. Level Classification: Classify the card into one of these levels:
   - 'Junior': Fundamental syntax, basic queries, simple joins, basic keys.
   - 'Mid': Grouping, aggregation, subqueries, indexing concepts, constraints.
   - 'Senior': Triggers, transaction isolation levels, serializability, query plan optimization, recursive CTEs, locking, distributed architectures.

OUTPUT FORMAT:
You MUST return a JSON object containing a list of cards under the 'cards' key. Every card in the output must have:
- 'question'
- 'answer'
- 'category' (one of the 8 categories above)
- 'level' (Junior, Mid, or Senior)

JSON schema to match:
{
  "cards": [
    {
      "question": "string",
      "answer": "string",
      "category": "string",
      "level": "string"
    }
  ]
}

Here is the list of cards to process:
""" + json.dumps(cards_batch, indent=2)

    req_data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "responseMimeType": "application/json"
        }
    }
    
    data_bytes = json.dumps(req_data).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    req = urllib.request.Request(url, data=data_bytes, headers=headers, method="POST")
    
    max_retries = 5
    retry_delay = 5
    
    for attempt in range(max_retries):
        try:
            print(f"Sending batch {batch_num}/{total_batches} (Attempt {attempt + 1})...")
            with urllib.request.urlopen(req, timeout=30) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                candidates = res_data.get("candidates", [])
                if not candidates:
                    raise ValueError("No candidates returned from API.")
                content_text = candidates[0]["content"]["parts"][0]["text"]
                result = json.loads(content_text)
                return result.get("cards", [])
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8")
            print(f"  HTTP Error {e.code}: {e.reason}")
            if e.code in [429, 500, 503]:
                print(f"  Transient error. Sleeping for {retry_delay} seconds before retry...")
                time.sleep(retry_delay)
                retry_delay *= 2
            else:
                print(f"  Unrecoverable API error: {body}")
                raise e
        except Exception as e:
            print(f"  Connection error: {e}")
            print(f"  Sleeping for {retry_delay} seconds before retry...")
            time.sleep(retry_delay)
            retry_delay *= 2
            
    raise RuntimeError("Failed to complete request after maximum retries.")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pgres_dir = os.path.join(current_dir, "input", "pgres")
    final_dir = os.path.join(current_dir, "final")
    
    os.makedirs(final_dir, exist_ok=True)
    
    output_md = os.path.join(final_dir, "postgres_deck.md")
    output_apkg = os.path.join(final_dir, "postgres_deck.apkg")
    progress_file = os.path.join(final_dir, "progress_postgres.json")

    # 1. Parse API key
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key and os.path.exists(os.path.join(current_dir, ".env")):
        with open(os.path.join(current_dir, ".env"), "r") as env_f:
            for line in env_f:
                if line.startswith("GEMINI_API_KEY="):
                    api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
                    
    if not api_key:
        print("Error: GEMINI_API_KEY is not set in environment or .env file.")
        return

    # 2. Extract cards from PostgreSQL apkg files
    apkg_files = [
        os.path.join(pgres_dir, "Data_PostgreSQL.apkg"),
        os.path.join(pgres_dir, "SQL_Basics_with_Emphasis_on_SQLite_and_PostgreSQL.apkg")
    ]
    
    raw_cards = []
    for filepath in apkg_files:
        if os.path.exists(filepath):
            extracted = extract_cards_from_apkg(filepath)
            print(f"Extracted {len(extracted)} cards from {os.path.basename(filepath)}.")
            raw_cards.extend(extracted)
            
    if not raw_cards:
        print("No cards found in the PostgreSQL directory.")
        return
        
    print(f"Loaded {len(raw_cards)} total raw PostgreSQL cards.")

    # 3. Sort alphabetically by question to place similar cards adjacent to each other
    raw_cards.sort(key=lambda c: c["question"].lower())
    
    # 4. Batch cards (35 per batch to optimize tokens & quality)
    batch_size = 35
    batches = [raw_cards[i:i + batch_size] for i in range(0, len(raw_cards), batch_size)]
    total_batches = len(batches)
    
    processed_cards = []
    start_batch_idx = 1
    
    # Load existing progress if available
    if os.path.exists(progress_file):
        try:
            with open(progress_file, "r", encoding="utf-8") as pf:
                progress_data = json.load(pf)
                processed_cards = progress_data.get("processed_cards", [])
                start_batch_idx = progress_data.get("last_processed_batch_index", 0) + 1
                print(f"Loaded existing progress. Resuming from batch {start_batch_idx}/{total_batches}...")
        except Exception as e:
            print(f"Warning: could not load progress file: {e}. Starting from scratch.")
            processed_cards = []
            start_batch_idx = 1
            
    completed_all = True
    for i, batch in enumerate(batches, 1):
        if i < start_batch_idx:
            continue
            
        batch_input = []
        for idx, card in enumerate(batch, 1):
            batch_input.append({
                "id": idx,
                "question": card["question"],
                "answer": card["answer"]
            })
            
        try:
            results = call_gemini_api(api_key, batch_input, i, total_batches)
            print(f"  Successfully processed batch {i}. Extracted {len(results)} merged cards.")
            processed_cards.extend(results)
            
            # Save progress checkpoint
            try:
                with open(progress_file, "w", encoding="utf-8") as pf:
                    json.dump({
                        "last_processed_batch_index": i,
                        "processed_cards": processed_cards
                    }, pf, indent=2)
            except Exception as e:
                print(f"  Warning: could not save progress checkpoint: {e}")
                
        except Exception as e:
            print(f"  Error in batch {i}: {e}")
            print(f"  Stopping process at batch {i}. Checkpoint saved.")
            completed_all = False
            break
            
        # Rate limit cooldown (RPM is 15 on free tier, wait 5 seconds between calls)
        time.sleep(5)

    if not completed_all:
        print(f"\nExecution paused. Run again to resume from checkpoint: {progress_file}")
        return

    if not processed_cards:
        print("No cards were processed.")
        return

    # 5. Format final output Markdown
    print(f"Deduplicated and structured cards down to {len(processed_cards)} total items.")
    
    categories = {}
    for card in processed_cards:
        cat = card.get("category", "General SQL & Databases")
        level = card.get("level", "Mid")
        categories.setdefault(cat, {}).setdefault(level, []).append(card)

    md_content = """# PostgreSQL Consolidated Study Guide

A professionally structured study guide compiled from PostgreSQL Anki decks, deduplicated semantically, categorized, and graded by difficulty.

## Deck Metrics
- **Original Deck Cards**: """ + str(len(raw_cards)) + """
- **Final Deduplicated Cards**: """ + str(len(processed_cards)) + """

---
"""
    level_order = ["Junior", "Mid", "Senior"]
    level_emojis = {"Junior": "🟢", "Mid": "🟡", "Senior": "🔴"}
    
    for cat_name in sorted(categories.keys()):
        cat_data = categories[cat_name]
        total_cat_cards = sum(len(lvl_cards) for lvl_cards in cat_data.values())
        
        md_content += f"\n## 📂 Category: {cat_name} ({total_cat_cards} cards)\n"
        
        for level in level_order:
            lvl_cards = cat_data.get(level, [])
            if not lvl_cards:
                continue
                
            md_content += f"\n### {level_emojis[level]} {level} Level\n\n"
            for idx, card in enumerate(sorted(lvl_cards, key=lambda c: c["question"]), 1):
                q = card["question"].strip()
                a = card["answer"].strip()
                md_content += f"#### {idx}. {q}\n"
                md_content += f"**Answer:**\n{a}\n\n"
                
    with open(output_md, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    print(f"Markdown Guide successfully generated: {output_md}")

    # 6. Package and compile into Anki .apkg
    model_id = 1607392320
    deck_id = 2059400120
    
    anki_model = genanki.Model(
        model_id,
        'PostgreSQL Premium Study Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'SQL Card',
                'qfmt': '<div class="card-box question-style">{{Question}}</div>',
                'afmt': '<div class="card-box question-style">{{Question}}</div><hr id="answer"><div class="card-box answer-style">{{Answer}}</div>',
            },
        ],
        css="""
        .card {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 18px;
            color: #1e293b;
            background-color: #f8fafc;
            padding: 20px;
            display: flex;
            justify-content: center;
        }
        .card-box {
            max-width: 700px;
            width: 100%;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            padding: 24px;
            text-align: left;
            line-height: 1.6;
            margin: 10px auto;
        }
        .question-style {
            font-weight: 600;
            border-left: 5px solid #0066cc;
            color: #0f3d7a;
        }
        .answer-style {
            border-left: 5px solid #10b981;
            color: #0f172a;
        }
        hr#answer {
            border: 0;
            height: 1px;
            background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0));
            margin: 15px 0;
        }
        pre {
            background-color: #f1f5f9;
            border: 1px solid #e2e8f0;
            padding: 14px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: "Fira Code", Monaco, Consolas, "Courier New", monospace;
            font-size: 15px;
            color: #0f172a;
            line-height: 1.4;
        }
        code {
            font-family: "Fira Code", Monaco, Consolas, "Courier New", monospace;
            background-color: #e2e8f0;
            color: #0f172a;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.9em;
        }
        b {
            color: #0066cc;
        }
        """
    )

    anki_deck = genanki.Deck(
        deck_id,
        'SQL & Databases (PostgreSQL)'
    )

    for card in processed_cards:
        q_html = markdown_to_html(card['question'])
        a_html = markdown_to_html(card['answer'])
        
        cleaned_cat = re.sub(r'[^\w\s-]', '', card.get('category', 'General')).strip()
        cleaned_cat = re.sub(r'[\s-]+', '_', cleaned_cat)
        
        tags = [cleaned_cat, card.get('level', 'Mid'), 'PostgreSQL']
        
        note = genanki.Note(
            model=anki_model,
            fields=[q_html, a_html],
            tags=tags
        )
        anki_deck.add_note(note)

    try:
        genanki.Package(anki_deck).write_to_file(output_apkg)
        print("Anki Package successfully compiled!")
        print(f"  Final Markdown: {output_md}")
        print(f"  Final APKG: {output_apkg}")
    except Exception as e:
        print(f"Error packaging apkg file: {e}")
        
    # Clean up progress checkpoint file
    if os.path.exists(progress_file):
        try:
            os.remove(progress_file)
        except Exception:
            pass

if __name__ == '__main__':
    main()
