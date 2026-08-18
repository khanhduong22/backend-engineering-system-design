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
    deck_key = re.sub(r'[^\w]', '_', os.path.splitext(filename)[0])
    temp_dir = os.path.join(os.path.dirname(apkg_path), f"temp_extract_{deck_key}")
    
    try:
        os.makedirs(temp_dir, exist_ok=True)
        with zipfile.ZipFile(apkg_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    except Exception as e:
        print(f"  Error extracting zip {filename}: {e}")
        shutil.rmtree(temp_dir, ignore_errors=True)
        return []

    # Priority check for collection.anki21
    db_file = None
    for f in ['collection.anki21', 'collection.anki2']:
        p = os.path.join(temp_dir, f)
        if os.path.exists(p):
            db_file = p
            break
            
    if not db_file:
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
        except Exception:
            pass
            
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
            front = clean_html(fields[front_idx]) if front_idx < len(fields) else (clean_html(fields[0]) if fields else "")
            back = clean_html(fields[back_idx]) if back_idx < len(fields) else (clean_html(fields[1]) if len(fields) > 1 else (clean_html(fields[0]) if fields else ""))
            
            if front and len(front) > 3:
                cards_list.append({
                    'deck': deck_name,
                    'question': front,
                    'answer': back
                })
        conn.close()
    except Exception as e:
        print(f"  Error reading DB {filename}: {e}")
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
        
    return cards_list

def call_gemini_api(api_keys, cards_batch, domain_name, batch_num, total_batches):
    if isinstance(api_keys, str):
        api_keys = [api_keys]

    models_to_try = [
        "gemini-flash-lite-latest",
        "gemini-3.5-flash-lite",
        "gemini-3.5-flash"
    ]
    
    prompt = f"""You are a senior backend engineer, database architect, and technical educator specializing in {domain_name}. Your task is to process, refine, deduplicate, and grade a list of technical flashcards.

CRITICAL INSTRUCTIONS (MICRO-BATCH PRECISION):
1. Deduplicate & Merge: Combine cards that have the exact same semantic question or target concept. Keep the clearest question and merge any complementary details in the answer.
2. PRESERVE TECHNICAL DETAILS: Do NOT drop technical edge cases, CLI commands, code snippets, or system parameters. Minor duplicate variants of concepts MAY be preserved for memory reinforcement.
3. Categorize: Assign each card to a clean sub-category relevant to {domain_name}.
4. Level Classification: Grade each card as 'Junior', 'Mid', or 'Senior'.

OUTPUT FORMAT:
Return a JSON object with key 'cards':
{{
  "cards": [
    {{
      "question": "string",
      "answer": "string",
      "category": "string",
      "level": "Junior | Mid | Senior"
    }}
  ]
}}

Flashcards batch:
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
    
    for key_idx, k in enumerate(api_keys):
        for model_name in models_to_try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={k}"
            req = urllib.request.Request(url, data=data_bytes, headers=headers, method="POST")
            
            for attempt in range(2):
                try:
                    print(f"    [{domain_name}] Batch {batch_num}/{total_batches} using {model_name} (Key #{key_idx+1}, Attempt {attempt+1})...", flush=True)
                    with urllib.request.urlopen(req, timeout=30) as response:
                        res_data = json.loads(response.read().decode("utf-8"))
                        candidates = res_data.get("candidates", [])
                        if not candidates:
                            raise ValueError("No candidates returned")
                        content_text = candidates[0]["content"]["parts"][0]["text"]
                        result = json.loads(content_text)
                        time.sleep(2.0)
                        return result.get("cards", [])
                except urllib.error.HTTPError as e:
                    body = e.read().decode("utf-8")
                    if e.code in [429, 500, 503]:
                        print(f"      HTTP {e.code} Rate limit on Key #{key_idx+1} ({model_name}). Rotating to next key/model...", flush=True)
                        time.sleep(2)
                        break
                    else:
                        print(f"      HTTP Error {e.code} on Key #{key_idx+1} ({model_name}): {body[:100]}", flush=True)
                        break
                except Exception as e:
                    time.sleep(2)
                    break
                
    print(f"  Warning: Failed to process batch {batch_num} via API. Falling back to unmerged cards.", flush=True)
    fallback = []
    for card in cards_batch:
        fallback.append({
            "question": card["question"],
            "answer": card["answer"],
            "category": domain_name,
            "level": "Mid"
        })
    return fallback

def import_to_anki_connect(apkg_path, domain_code=None):
    url = "http://127.0.0.1:8765"
    payload = {
        "action": "importPackage",
        "version": 6,
        "params": {
            "path": os.path.abspath(apkg_path)
        }
    }
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            if res.get("error"):
                print(f"  AnkiConnect import warning for {os.path.basename(apkg_path)}: {res['error']}", flush=True)
            else:
                print(f"  Successfully imported {os.path.basename(apkg_path)} into Anki Desktop via AnkiConnect!", flush=True)
                
        # Organize subdecks ju, mid, sen if domain_code provided
        if domain_code and domain_code != "01_SQL_PostgreSQL_Mastery":
            def call_ac(action, params={}):
                p = json.dumps({'action': action, 'version': 6, 'params': params}).encode('utf-8')
                with urllib.request.urlopen(urllib.request.Request(url, data=p, headers={'Content-Type': 'application/json'})) as r:
                    return json.loads(r.read().decode('utf-8'))

            ju_name = "ju_optional" if "Networking" in domain_code else "ju"
            level_map = [("Junior", ju_name), ("Mid", "mid"), ("Senior", "sen")]
            for lvl_name, sub_name in level_map:
                subdeck = f"Backend Engineering::{domain_code}::{sub_name}"
                call_ac('createDeck', {'deck': subdeck})
                found = call_ac('findCards', {'query': f'tag:\"{domain_code}\" tag:\"{lvl_name}\"'})
                card_ids = found.get('result', [])
                if card_ids:
                    call_ac('changeDeck', {'cards': card_ids, 'deck': subdeck})
            print(f"  Organized tree structure Backend Engineering::{domain_code} ({ju_name}, mid, sen) in Anki Desktop!", flush=True)
            
    except Exception as e:
        print(f"  AnkiConnect import notice: Could not auto-import {os.path.basename(apkg_path)} ({e}). You can import manually.", flush=True)

def build_domain_apkg_and_md(final_dir, domain_code, domain_title, deck_id, cards, anki_model):
    md_file = os.path.join(final_dir, f"{domain_code}.md")
    apkg_file = os.path.join(final_dir, f"{domain_code}.apkg")
    
    # 1. Write Markdown
    categories = {}
    for card in cards:
        cat = card.get("category", domain_title)
        lvl = card.get("level", "Mid")
        categories.setdefault(cat, {}).setdefault(lvl, []).append(card)
        
    md_content = f"# {domain_code} - {domain_title} Study Guide\n\n"
    md_content += f"- **Total Cards**: {len(cards)}\n\n---\n"
    
    level_emojis = {"Junior": "🟢", "Mid": "🟡", "Senior": "🔴"}
    for cat_name in sorted(categories.keys()):
        cat_cards_dict = categories[cat_name]
        total_cat_cards = sum(len(lcards) for lcards in cat_cards_dict.values())
        md_content += f"\n## 📂 Category: {cat_name} ({total_cat_cards} cards)\n"
        
        for lvl in ["Junior", "Mid", "Senior"]:
            lcards = cat_cards_dict.get(lvl, [])
            if not lcards:
                continue
            md_content += f"\n### {level_emojis.get(lvl, '🟡')} {lvl} Level\n\n"
            for idx, card in enumerate(sorted(lcards, key=lambda c: (c.get("question") or c.get("Question") or "")), 1):
                q = (card.get("question") or card.get("Question") or "").strip()
                a = (card.get("answer") or card.get("Answer") or "").strip()
                if not q:
                    continue
                md_content += f"#### {idx}. {q}\n"
                md_content += f"**Answer:**\n{a}\n\n"
                
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"  Wrote Markdown: {md_file}")

    # 2. Package APKG with parent deck and subdecks ju, mid, sen
    deck_parent = genanki.Deck(deck_id, f"Backend Engineering::{domain_code}")
    deck_ju = genanki.Deck(deck_id + 1, f"Backend Engineering::{domain_code}::ju")
    deck_mid = genanki.Deck(deck_id + 2, f"Backend Engineering::{domain_code}::mid")
    deck_sen = genanki.Deck(deck_id + 3, f"Backend Engineering::{domain_code}::sen")
    
    decks_by_level = {
        "Junior": deck_ju,
        "Mid": deck_mid,
        "Senior": deck_sen
    }
    
    for card in cards:
        lvl = card.get("level", "Mid")
        if lvl not in decks_by_level:
            lvl = "Mid"
        target_deck = decks_by_level[lvl]
        
        q_val = (card.get("question") or card.get("Question") or "").strip()
        a_val = (card.get("answer") or card.get("Answer") or "").strip()
        if not q_val:
            continue
            
        q_html = markdown_to_html(q_val)
        a_html = markdown_to_html(a_val)
        cleaned_cat = re.sub(r'[^\w\s-]', '', card.get('category', 'General')).strip().replace(' ', '_')
        tags = [cleaned_cat, lvl, domain_code]
        
        note = genanki.Note(
            model=anki_model,
            fields=[q_html, a_html],
            tags=tags
        )
        target_deck.add_note(note)
        
    package = genanki.Package([deck_parent, deck_ju, deck_mid, deck_sen])
    package.write_to_file(apkg_file)
    print(f"  Compiled APKG with subdecks (ju, mid, sen): {apkg_file}", flush=True)
    
    # 3. Import to AnkiConnect
    import_to_anki_connect(apkg_file, domain_code)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(current_dir, "input")
    downloads_dir = os.path.expanduser("~/Downloads")
    final_dir = os.path.join(current_dir, "final")
    os.makedirs(final_dir, exist_ok=True)
    
    progress_file = os.path.join(final_dir, "progress_all_be.json")

    key_map = {}
    if os.path.exists(os.path.join(current_dir, ".env")):
        with open(os.path.join(current_dir, ".env"), "r") as env_f:
            for line in env_f:
                line = line.strip()
                if line.startswith("GEMINI_API_KEY") and "=" in line:
                    parts = line.split("=", 1)
                    var_name = parts[0].strip()
                    val = parts[1].strip().strip('"').strip("'")
                    if val:
                        key_map[var_name] = val
                        
    api_keys = []
    # New key (GEMINI_API_KEY2) FIRST, old key (GEMINI_API_KEY) as BACKUP
    if "GEMINI_API_KEY2" in key_map:
        api_keys.append(key_map["GEMINI_API_KEY2"])
    if "GEMINI_API_KEY" in key_map and key_map["GEMINI_API_KEY"] not in api_keys:
        api_keys.append(key_map["GEMINI_API_KEY"])
        
    for k in key_map.values():
        if k not in api_keys:
            api_keys.append(k)
            
    print(f"Loaded {len(api_keys)} Gemini API Keys for Pool Rotation (Primary: ...{api_keys[0][-6:]}).", flush=True)

    # 8 Single-Domain Definitions in High-ROI Order
    domain_configs = [
        {
            "code": "01_SQL_PostgreSQL_Mastery",
            "title": "SQL & PostgreSQL Mastery",
            "deck_id": 2059400201,
            "patterns": ["SQL", "postgres"]
        },
        {
            "code": "02_Storage_DDIA",
            "title": "Storage Engines & Distributed Data (DDIA)",
            "deck_id": 2059400203,
            "patterns": ["Designing_Data", "DDIA", "Storage"]
        },
        {
            "code": "03_Redis_Caching",
            "title": "Redis & In-Memory Caching Architecture",
            "deck_id": 2059400204,
            "patterns": ["Redis"]
        },
        {
            "code": "04_Kafka_EventDriven",
            "title": "Kafka & Event-Driven Systems",
            "deck_id": 2059400205,
            "patterns": ["Kafka"]
        },
        {
            "code": "05_SystemDesign_Architecture",
            "title": "System Design & Distributed Architecture",
            "deck_id": 2059400208,
            "patterns": ["Alex_Xu", "System_Design"]
        },
        {
            "code": "06_DesignPatterns_OOP",
            "title": "Software Design Patterns & Object-Oriented Design",
            "deck_id": 2059400206,
            "patterns": ["Design_Patterns", "DesignPatterns"]
        },
        {
            "code": "07_ComputerScience_SWE",
            "title": "CS Fundamentals & Software Engineering",
            "deck_id": 2059400207,
            "patterns": ["Software_Engineering", "Computer_Science", "Coding_Interview", "jwasham"]
        },
        {
            "code": "08_Networking_Security",
            "title": "Computer Networking & Security Protocols",
            "deck_id": 2059400202,
            "patterns": ["Networking", "Network"]
        }
    ]

    # Shared Anki Model
    model_id = 1607392400
    anki_model = genanki.Model(
        model_id,
        'BE Study Master Model',
        fields=[{'name': 'Question'}, {'name': 'Answer'}],
        templates=[{
            'name': 'BE Card',
            'qfmt': '<div class="card-box question-style">{{Question}}</div>',
            'afmt': '<div class="card-box question-style">{{Question}}</div><hr id="answer"><div class="card-box answer-style">{{Answer}}</div>',
        }],
        css="""
        .card { font-family: 'Inter', -apple-system, sans-serif; font-size: 18px; color: #1e293b; background-color: #f8fafc; padding: 20px; display: flex; justify-content: center; }
        .card-box { max-width: 700px; width: 100%; background: #ffffff; border-radius: 12px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); padding: 24px; text-align: left; line-height: 1.6; margin: 10px auto; }
        .question-style { font-weight: 600; border-left: 5px solid #2563eb; color: #1e3a8a; }
        .answer-style { border-left: 5px solid #10b981; color: #0f172a; }
        hr#answer { border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(0,0,0,0.1), rgba(0,0,0,0)); margin: 15px 0; }
        pre { background-color: #f1f5f9; border: 1px solid #e2e8f0; padding: 14px; border-radius: 8px; overflow-x: auto; font-family: "Fira Code", monospace; font-size: 15px; color: #0f172a; }
        code { font-family: "Fira Code", monospace; background-color: #e2e8f0; color: #0f172a; padding: 2px 6px; border-radius: 4px; font-size: 0.9em; }
        b { color: #2563eb; }
        """
    )

    # Scan for APKG files
    apkg_paths = []
    for search_dir in [input_dir, downloads_dir]:
        if os.path.exists(search_dir):
            for root, _, files in os.walk(search_dir):
                for f in files:
                    if f.endswith('.apkg'):
                        apkg_paths.append(os.path.join(root, f))

    print(f"Found {len(apkg_paths)} total APKG files.")

    # Load progress checkpoint
    progress = {}
    if os.path.exists(progress_file):
        try:
            with open(progress_file, "r", encoding="utf-8") as pf:
                progress = json.load(pf)
                print("Loaded progress checkpoint.")
        except Exception:
            progress = {}

    # Process domain by domain
    for domain in domain_configs:
        code = domain["code"]
        title = domain["title"]
        deck_id = domain["deck_id"]
        patterns = domain["patterns"]
        
        print(f"\n==========================================")
        print(f"Processing Domain: {code} - {title}")
        print(f"==========================================")
        
        # 1. Reuse existing SQL cards if domain 01
        if code == "01_SQL_PostgreSQL_Mastery" and os.path.exists(os.path.join(final_dir, "junior_deck.md")):
            print("Reusing existing compiled SQL & PostgreSQL cards from final/...")
            sql_cards = []
            for md_name in ["junior_deck.md", "mid_deck.md", "senior_deck.md", "postgres_deck.md"]:
                p = os.path.join(final_dir, md_name)
                if os.path.exists(p):
                    with open(p, "r", encoding="utf-8") as pf:
                        current_q = None
                        current_ans = []
                        in_ans = False
                        for line in pf:
                            if line.startswith("#### "):
                                if current_q:
                                    sql_cards.append({"question": current_q, "answer": "\n".join(current_ans).strip(), "category": "SQL & PostgreSQL", "level": "Mid"})
                                    current_ans = []
                                current_q = re.sub(r'^####\s*\d+\.\s*', '', line).strip()
                                in_ans = False
                            elif line.strip() == "**Answer:**":
                                in_ans = True
                            elif in_ans:
                                current_ans.append(line)
                        if current_q:
                            sql_cards.append({"question": current_q, "answer": "\n".join(current_ans).strip(), "category": "SQL & PostgreSQL", "level": "Mid"})
                            
            build_domain_apkg_and_md(final_dir, code, title, deck_id, sql_cards, anki_model)
            continue

        # Match files for domain
        matching_apkgs = []
        for p in apkg_paths:
            fname = os.path.basename(p)
            for pat in patterns:
                if pat.lower() in fname.lower() or pat.lower() in p.lower():
                    matching_apkgs.append(p)
                    break

        if not matching_apkgs:
            print(f"  No matching APKG files found for domain {code}.")
            continue

        raw_domain_cards = []
        for p in matching_apkgs:
            extracted = extract_cards_from_apkg(p)
            print(f"  Extracted {len(extracted)} raw cards from {os.path.basename(p)}.")
            raw_domain_cards.extend(extracted)

        if not raw_domain_cards:
            print(f"  No valid notes extracted for {code}.")
            continue

        print(f"  Total raw cards for {code}: {len(raw_domain_cards)}")
        raw_domain_cards.sort(key=lambda c: c["question"].lower())

        # Micro-batching payload: 18 cards/batch
        batch_size = 18
        batches = [raw_domain_cards[i:i + batch_size] for i in range(0, len(raw_domain_cards), batch_size)]
        total_batches = len(batches)
        
        domain_progress = progress.get(code, {})
        processed_domain_cards = domain_progress.get("processed_cards", [])
        start_batch_idx = domain_progress.get("last_batch_idx", 0) + 1

        if start_batch_idx > total_batches and processed_domain_cards:
            print(f"  Domain {code} already fully processed. Re-compiling output...")
            build_domain_apkg_and_md(final_dir, code, title, deck_id, processed_domain_cards, anki_model)
            continue

        print(f"  Processing {total_batches} batches (Starting from batch {start_batch_idx})...")
        for i, batch in enumerate(batches, 1):
            if i < start_batch_idx:
                continue

            batch_input = [{"id": idx, "question": card["question"], "answer": card["answer"]} for idx, card in enumerate(batch, 1)]
            try:
                results = call_gemini_api(api_keys, batch_input, title, i, total_batches)
                processed_domain_cards.extend(results)
                
                # Checkpoint
                progress[code] = {
                    "last_batch_idx": i,
                    "processed_cards": processed_domain_cards
                }
                with open(progress_file, "w", encoding="utf-8") as pf:
                    json.dump(progress, pf, indent=2)
            except Exception as e:
                print(f"  Error processing batch {i} for {code}: {e}")
                break
                
            time.sleep(3)

        build_domain_apkg_and_md(final_dir, code, title, deck_id, processed_domain_cards, anki_model)

    print("\n==========================================")
    print("Master Pipeline Execution Completed!")
    print(f"All 8 single-domain decks generated in {final_dir}")
    print("==========================================")

if __name__ == '__main__':
    main()
