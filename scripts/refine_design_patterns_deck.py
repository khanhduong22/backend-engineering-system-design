import os
import json
import time
import re
import shutil
import sqlite3
import zipfile
import tempfile
import urllib.request
import genanki

def req_anki(action, params={}):
    url = "http://127.0.0.1:8765"
    p = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=p, headers={"Content-Type": "application/json"})) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"AnkiConnect Error: {e}")
        return {}

def clean_html(raw_html):
    if not raw_html:
        return ""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', raw_html)
    cleantext = cleantext.replace('&nbsp;', ' ').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')
    return ' '.join(cleantext.split()).strip()

def get_field_mappings(models_json):
    mappings = {}
    try:
        models = json.loads(models_json)
    except Exception:
        return mappings

    for mid_str, m_data in models.items():
        try:
            mid = int(mid_str)
            fields = m_data.get('flds', [])
            if not fields:
                continue
            front_idx = 0
            front_keywords = ['front', 'question', 'vorderseite', 'prompt', 'term', 'expression', 'word', 'entry', 'title', 'header']
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
        shutil.rmtree(temp_dir, ignore_errors=True)
        return []

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
        pass
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    return cards_list

def call_gemini_merge_patterns(api_keys, cards_batch):
    if isinstance(api_keys, str):
        api_keys = [api_keys]

    models_to_try = [
        "gemini-flash-lite-latest",
        "gemini-3.5-flash-lite",
        "gemini-3.5-flash"
    ]
    
    prompt = """You are a Principal Software Architect and Design Patterns expert. Your task is to process, deduplicate, and merge a batch of Design Patterns and OOP flashcards.

CRITICAL MERGING & DEDUPLICATION INSTRUCTIONS:
1. MERGE DUPLICATES STRICTLY: Any cards asking about the exact same Design Pattern (e.g., Singleton, Factory Method, Abstract Factory, Observer, Strategy, Decorator, Adapter, Flyweight, Proxy, Bridge, Composite, Builder, Facade, Command, State, Template Method) or OOP concept MUST BE MERGED into 1 definitive card.
2. COMBINE ANSWER CONTENTS (BACK CARDS): When merging duplicate cards, DO NOT LOSE ANY EXPLANATION DETAILS OR CODE EXAMPLES. Merge all answer points into a single, rich, comprehensive answer covering:
   - Definition & Core Intent
   - Key Components / Mechanism
   - Code Example / Use Case
   - Trade-offs / Pros & Cons
3. Level Classification: Grade each card as 'Junior', 'Mid', or 'Senior'.
4. Language: English only.

OUTPUT FORMAT (JSON):
{
  "cards": [
    {
      "question": "string (Clean, definitive question)",
      "answer": "string (Merged, comprehensive answer combining all details)",
      "category": "Design Patterns & OOP",
      "level": "Junior | Mid | Senior"
    }
  ]
}

Flashcards batch to merge:
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
                    with urllib.request.urlopen(req, timeout=35) as response:
                        res_data = json.loads(response.read().decode("utf-8"))
                        candidates = res_data.get("candidates", [])
                        if not candidates:
                            raise ValueError("No candidates returned")
                        content_text = candidates[0]["content"]["parts"][0]["text"]
                        result = json.loads(content_text)
                        time.sleep(1.5)
                        return result.get("cards", [])
                except urllib.error.HTTPError as e:
                    if e.code in [429, 500, 503]:
                        time.sleep(2)
                        break
                    else:
                        break
                except Exception as e:
                    time.sleep(2)
                    break

    print("  Fallback: Returning unmerged batch.")
    return cards_batch

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(current_dir, "input")
    final_dir = os.path.join(current_dir, "final")
    progress_file = os.path.join(final_dir, "progress_all_be.json")

    api_keys = []
    if os.path.exists(os.path.join(current_dir, ".env")):
        with open(os.path.join(current_dir, ".env"), "r") as env_f:
            for line in env_f:
                line = line.strip()
                if line.startswith("GEMINI_API_KEY") and "=" in line:
                    k = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if k and k not in api_keys:
                        api_keys.append(k)

    key2 = "AIzaSyCmUfCKApT5a2vob1mQpJ1drTqzMOtOrOM"
    if key2 in api_keys:
        api_keys.remove(key2)
        api_keys.insert(0, key2)

    domain_code = "06_DesignPatterns_OOP"
    domain_title = "Software Design Patterns & Object-Oriented Design"
    deck_id = 2059400207

    # Find matching APKGs recursively
    matching_apkgs = []
    for root, dirs, files in os.walk(input_dir):
        for f in files:
            if f.endswith(".apkg") and ("Design_Patterns" in f or "design_patterns" in f or "Software_design" in f):
                matching_apkgs.append(os.path.join(root, f))

    print(f"Found {len(matching_apkgs)} APKGs for Design Patterns.")
    raw_cards = []
    for p in matching_apkgs:
        extracted = extract_cards_from_apkg(p)
        print(f"  Extracted {len(extracted)} raw cards from {os.path.basename(p)}.")
        raw_cards.extend(extracted)

    print(f"Total raw cards extracted: {len(raw_cards)}")
    # Sort by question text alphabetically to cluster duplicate/similar questions next to each other
    raw_cards.sort(key=lambda c: c["question"].lower())

    # Batch 16 cards per batch
    batch_size = 16
    merged_cards = []
    total_batches = (len(raw_cards) + batch_size - 1) // batch_size

    print(f"\n==========================================")
    print(f"Merging & Deduplicating {len(raw_cards)} raw cards for {domain_code} across {total_batches} batches...")
    print(f"==========================================")

    for i in range(0, len(raw_cards), batch_size):
        batch = raw_cards[i:i + batch_size]
        b_idx = (i // batch_size) + 1
        print(f"  [{domain_code}] Merging Batch {b_idx}/{total_batches}...", flush=True)
        res = call_gemini_merge_patterns(api_keys, batch)
        merged_cards.extend(res)

    print(f"\nDeduplication Result: {len(raw_cards)} raw cards -> {len(merged_cards)} unique, merged cards.")

    # Save to progress checkpoint
    with open(progress_file, "r") as f:
        progress = json.load(f)
    progress[domain_code] = {
        "last_batch_idx": total_batches + 1,
        "processed_cards": merged_cards
    }
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)

    # 1. Delete ALL existing Design Patterns notes in Anki Desktop
    print("Purging existing Design Patterns notes from Anki Desktop...")
    old_anki_cards = req_anki("findCards", {"query": f'deck:"Backend Engineering::{domain_code}*"'}).get("result", [])
    if old_anki_cards:
        info = req_anki("cardsInfo", {"cards": old_anki_cards}).get("result", [])
        old_note_ids = list(set(c["note"] for c in info if "note" in c))
        if old_note_ids:
            req_anki("deleteNotes", {"notes": old_note_ids})
            print(f"Deleted {len(old_note_ids)} old notes from Anki Desktop.")

    # 2. Write Markdown
    md_file = os.path.join(final_dir, f"{domain_code}.md")
    apkg_file = os.path.join(final_dir, f"{domain_code}.apkg")
    
    categories = {}
    for card in merged_cards:
        cat = card.get("category", domain_title)
        lvl = card.get("level", "Mid")
        categories.setdefault(cat, {}).setdefault(lvl, []).append(card)
        
    md_content = f"# {domain_code} - {domain_title} Study Guide\n\n"
    md_content += f"- **Total Cards**: {len(merged_cards)}\n\n---\n"
    
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
            for idx, card in enumerate(sorted(lcards, key=lambda c: (c.get("question") or "")), 1):
                q = (card.get("question") or "").strip()
                a = (card.get("answer") or "").strip()
                if not q:
                    continue
                md_content += f"#### {idx}. {q}\n"
                md_content += f"**Answer:**\n{a}\n\n"
                
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Wrote Markdown: {md_file}")

    # 3. Package APKG
    anki_model = genanki.Model(
        1607392319,
        "Backend Master Model",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
            {"name": "Category"},
            {"name": "Level"}
        ],
        templates=[
            {
                "name": "Backend Concept Card",
                "qfmt": """
                <div class="card">
                    <div class="header">
                        <span class="category">{{Category}}</span>
                        <span class="level {{Level}}">{{Level}}</span>
                    </div>
                    <div class="question">{{Question}}</div>
                </div>
                <style>
                    .card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 20px; color: #2d3748; background: #ffffff; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
                    .header { display: flex; justify-content: space-between; margin-bottom: 15px; font-size: 0.85em; text-transform: uppercase; letter-spacing: 0.05em; }
                    .category { font-weight: 700; color: #4a5568; background: #edf2f7; padding: 4px 10px; border-radius: 6px; }
                    .level { font-weight: 700; padding: 4px 10px; border-radius: 6px; color: white; }
                    .level.Junior { background: #38a169; }
                    .level.Mid { background: #d69e2e; }
                    .level.Senior { background: #e53e3e; }
                    .question { font-size: 1.25em; font-weight: 600; line-height: 1.5; color: #1a202c; }
                </style>
                """,
                "afmt": """
                <div class="card">
                    <div class="header">
                        <span class="category">{{Category}}</span>
                        <span class="level {{Level}}">{{Level}}</span>
                    </div>
                    <div class="question">{{Question}}</div>
                    <hr id="answer">
                    <div class="answer">{{Answer}}</div>
                </div>
                <style>
                    .card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 20px; color: #2d3748; background: #ffffff; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
                    .header { display: flex; justify-content: space-between; margin-bottom: 15px; font-size: 0.85em; text-transform: uppercase; letter-spacing: 0.05em; }
                    .category { font-weight: 700; color: #4a5568; background: #edf2f7; padding: 4px 10px; border-radius: 6px; }
                    .level { font-weight: 700; padding: 4px 10px; border-radius: 6px; color: white; }
                    .level.Junior { background: #38a169; }
                    .level.Mid { background: #d69e2e; }
                    .level.Senior { background: #e53e3e; }
                    .question { font-size: 1.25em; font-weight: 600; line-height: 1.5; color: #1a202c; margin-bottom: 15px; }
                    hr#answer { border: 0; height: 1px; background: #e2e8f0; margin: 20px 0; }
                    .answer { font-size: 1.05em; line-height: 1.6; color: #2d3748; white-space: pre-wrap; }
                </style>
                """
            }
        ]
    )

    deck_ju = genanki.Deck(deck_id + 1, f"Backend Engineering::{domain_code}::ju")
    deck_mid = genanki.Deck(deck_id + 2, f"Backend Engineering::{domain_code}::mid")
    deck_sen = genanki.Deck(deck_id + 3, f"Backend Engineering::{domain_code}::sen")
    
    decks_by_level = {
        "Junior": deck_ju,
        "Mid": deck_mid,
        "Senior": deck_sen
    }
    
    for card in merged_cards:
        q = (card.get("question") or "").strip()
        a = (card.get("answer") or "").strip()
        cat = card.get("category", domain_title)
        lvl = card.get("level", "Mid")
        if lvl not in decks_by_level:
            lvl = "Mid"
        if not q or not a:
            continue
        note = genanki.Note(
            model=anki_model,
            fields=[q, a, cat, lvl]
        )
        decks_by_level[lvl].add_note(note)
        
    pkg = genanki.Package([deck_ju, deck_mid, deck_sen])
    pkg.write_to_file(apkg_file)
    print(f"Compiled APKG: {apkg_file}")

    # 4. Import & Re-organize in Anki Desktop
    import_res = req_anki("importPackage", {"path": os.path.abspath(apkg_file)})
    if import_res.get("error") is None:
        print(f"Imported into Anki Desktop via AnkiConnect!")
        sub_names = ["ju", "mid", "sen"]
        for sub in sub_names:
            old_name = f"Backend Engineering::{domain_code}::{sub}"
            cards = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
            if cards:
                req_anki("changeDeck", {"cards": cards, "deck": old_name})
        print(f"Organized Anki Desktop tree: Backend Engineering::{domain_code} (ju, mid, sen)")

    print("\n==========================================")
    print("DESIGN PATTERNS DECK RE-MERGED & SYNCED TO ANKI DESKTOP!")
    print("==========================================")

if __name__ == "__main__":
    main()
