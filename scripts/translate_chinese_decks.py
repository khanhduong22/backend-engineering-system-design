import os
import json
import time
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

def call_gemini_translate(api_keys, cards_batch, domain_name):
    if isinstance(api_keys, str):
        api_keys = [api_keys]

    models_to_try = [
        "gemini-flash-lite-latest",
        "gemini-3.5-flash-lite",
        "gemini-3.5-flash"
    ]
    
    prompt = f"""You are a senior backend engineer, database architect, and expert technical translator specializing in {domain_name}.

CRITICAL INSTRUCTIONS:
1. TRANSLATE TO ENGLISH: If any question or answer contains Chinese, Japanese, or non-English text, TRANSLATE IT FULLY INTO CLEAR, ACCURATE, PROFESSIONAL TECHNICAL ENGLISH.
2. PRESERVE TECHNICAL PRECISION: Keep all technical terminology (e.g., Redis RDB, AOF, Sentinel, Cluster, Kafka Partition, Consumer Group, ISR, ACK, Zookeeper), CLI commands, code snippets, and parameters intact.
3. Deduplicate & Merge: If cards in this batch ask the exact same question, merge them into 1 best card.
4. Categorize & Level: Grade each card as 'Junior', 'Mid', or 'Senior'.
5. ABSOLUTE REQUIREMENT: The final question and answer MUST be 100% in ENGLISH. No Chinese characters permitted in output.

OUTPUT FORMAT (JSON):
{{
  "cards": [
    {{
      "question": "string (English only)",
      "answer": "string (English only)",
      "category": "string",
      "level": "Junior | Mid | Senior"
    }}
  ]
}}

Flashcards batch to translate & refine:
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
                    with urllib.request.urlopen(req, timeout=30) as response:
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

    print("  Fallback: Could not translate batch via API.")
    return cards_batch

def build_and_sync_deck(domain_code, domain_title, deck_id, cards, final_dir):
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
            for idx, card in enumerate(sorted(lcards, key=lambda c: (c.get("question") or "")), 1):
                q = (card.get("question") or "").strip()
                a = (card.get("answer") or "").strip()
                if not q:
                    continue
                md_content += f"#### {idx}. {q}\n"
                md_content += f"**Answer:**\n{a}\n\n"
                
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"  Wrote Markdown: {md_file}")

    # 2. Package APKG
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
    
    for card in cards:
        q = (card.get("question") or card.get("Question") or "").strip()
        a = (card.get("answer") or card.get("Answer") or "").strip()
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
    print(f"  Compiled APKG: {apkg_file}")

    # 3. Import & Re-organize in Anki Desktop
    import_res = req_anki("importPackage", {"path": os.path.abspath(apkg_file)})
    if import_res.get("error") is None:
        print(f"  Imported into Anki Desktop via AnkiConnect!")
        sub_names = ["ju", "mid", "sen"]
        for sub in sub_names:
            old_name = f"Backend Engineering::{domain_code}::{sub}"
            cards = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
            if cards:
                req_anki("changeDeck", {"cards": cards, "deck": old_name})
        print(f"  Organized Anki Desktop tree: Backend Engineering::{domain_code} (ju, mid, sen)")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
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

    # Put GEMINI_API_KEY2 first
    key2 = os.getenv("GEMINI_API_KEY", "")
    if key2 in api_keys:
        api_keys.remove(key2)
        api_keys.insert(0, key2)

    with open(progress_file, "r") as f:
        progress = json.load(f)

    target_domains = [
        {"code": "03_Redis_Caching", "title": "Redis & In-Memory Caching Architecture", "deck_id": 2059400204},
        {"code": "04_Kafka_EventDriven", "title": "Kafka & Event-Driven Systems", "deck_id": 2059400205}
    ]

    for domain in target_domains:
        code = domain["code"]
        title = domain["title"]
        deck_id = domain["deck_id"]

        cards = progress.get(code, {}).get("processed_cards", [])
        print(f"\n==========================================")
        print(f"Translating Chinese cards for {code} ({len(cards)} total cards)...")
        print(f"==========================================")

        # Batch 15 cards
        batch_size = 15
        new_translated_cards = []
        
        for i in range(0, len(cards), batch_size):
            batch = cards[i:i + batch_size]
            b_idx = (i // batch_size) + 1
            tot_b = (len(cards) + batch_size - 1) // batch_size
            
            print(f"  [{code}] Translating Batch {b_idx}/{tot_b}...", flush=True)
            translated = call_gemini_translate(api_keys, batch, title)
            new_translated_cards.extend(translated)

        # Save to progress
        progress[code]["processed_cards"] = new_translated_cards
        with open(progress_file, "w", encoding="utf-8") as f:
            json.dump(progress, f, indent=2)

        # Build and Sync
        build_and_sync_deck(code, title, deck_id, new_translated_cards, final_dir)

    print("\n==========================================")
    print("ALL CHINESE CARDS TRANSLATED TO ENGLISH & SYNCED TO ANKI DESKTOP!")
    print("==========================================")

if __name__ == "__main__":
    main()
