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

def call_gemini_merge_pattern_group(api_keys, pattern_name, cards_group):
    if isinstance(api_keys, str):
        api_keys = [api_keys]

    models_to_try = [
        "gemini-flash-lite-latest",
        "gemini-3.5-flash-lite",
        "gemini-3.5-flash"
    ]
    
    prompt = f"""You are a Principal Software Architect and Design Patterns expert.
Your task is to merge all flashcard variants related to the design pattern / concept: "{pattern_name}".

STRICT MERGING RULES FOR "{pattern_name}":
1. CONSOLIDATE INTO 1 OR 2 DEFINITIVE CARDS MAXIMUM:
   - Card 1 (Primary Master Card): Comprehensive guide to {pattern_name}. Question: "What is the {pattern_name} design pattern, how does it work, and when should it be used?"
     Answer MUST combine:
     - Core Intent & Problem Solved
     - Key Components & Structure
     - Concrete Code Example / Use Case
     - Pros, Cons & Trade-offs
   - Card 2 (Optional - Comparison / Anti-pattern): ONLY create a 2nd card if there is a distinct comparison or non-use scenario (e.g., "{pattern_name} vs Strategy" or "When NOT to use {pattern_name}").
2. DO NOT LOSE ANY TECHNICAL DETAILS: Preserve code snippets, UML structural notes, and key trade-offs from the input cards into the merged answer.
3. Level Classification: Grade each merged card as 'Junior', 'Mid', or 'Senior'.
4. Language: English only.

OUTPUT FORMAT (JSON):
{{
  "cards": [
    {{
      "question": "string",
      "answer": "string",
      "category": "Design Patterns & OOP",
      "level": "Junior | Mid | Senior"
    }}
  ]
}}

Input cards for {pattern_name}:
""" + json.dumps(cards_group, indent=2)

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
                        time.sleep(1.2)
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

    print(f"  Fallback for {pattern_name}: returning 1 merged fallback card.")
    # Simple fallback merge
    combined_q = f"What is the {pattern_name} design pattern, how does it work, and when should it be used?"
    combined_a = "\n\n".join([f"• {c.get('question')}:\n{c.get('answer')}" for c in cards_group])
    return [{
        "question": combined_q,
        "answer": combined_a,
        "category": "Design Patterns & OOP",
        "level": "Mid"
    }]

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

    key2 = os.getenv("GEMINI_API_KEY", "")
    if key2 in api_keys:
        api_keys.remove(key2)
        api_keys.insert(0, key2)

    domain_code = "06_DesignPatterns_OOP"
    domain_title = "Software Design Patterns & Object-Oriented Design"
    deck_id = 2059400207

    with open(progress_file, "r") as f:
        progress = json.load(f)

    existing_cards = progress.get(domain_code, {}).get("processed_cards", [])
    print(f"Loaded {len(existing_cards)} existing cards for {domain_code}.")

    patterns = [
        'Singleton', 'Factory Method', 'Abstract Factory', 'Builder', 'Prototype',
        'Adapter', 'Bridge', 'Composite', 'Decorator', 'Facade', 'Flyweight', 'Proxy',
        'Chain of Responsibility', 'Command', 'Interpreter', 'Iterator', 'Mediator',
        'Memento', 'Observer', 'State', 'Strategy', 'Template Method', 'Visitor',
        'SOLID', 'Uniform Access'
    ]

    pattern_groups = {}
    uncategorized = []

    for c in existing_cards:
        q = (c.get("question") or "").strip()
        a = (c.get("answer") or "").strip()
        text = (q + " " + a).lower()
        
        matched = False
        for p in patterns:
            if p.lower() in text:
                pattern_groups.setdefault(p, []).append(c)
                matched = True
                break
        if not matched:
            uncategorized.append(c)

    print(f"\nGrouped into {len(pattern_groups)} Pattern groups and {len(uncategorized)} general OOP cards.")

    final_merged_cards = []

    # Process each pattern group through Gemini AI
    for p_name in sorted(pattern_groups.keys()):
        p_cards = pattern_groups[p_name]
        print(f"  Merging Pattern '{p_name}' ({len(p_cards)} variant cards)...", flush=True)
        merged = call_gemini_merge_pattern_group(api_keys, p_name, p_cards)
        final_merged_cards.extend(merged)

    # Process uncategorized if any
    if uncategorized:
        print(f"  Merging {len(uncategorized)} general OOP cards...", flush=True)
        merged_general = call_gemini_merge_pattern_group(api_keys, "General OOP Concepts", uncategorized)
        final_merged_cards.extend(merged_general)

    print(f"\nFinal Semantic Consolidation Result: {len(existing_cards)} variant cards -> {len(final_merged_cards)} master cards.")

    # Save to progress checkpoint
    progress[domain_code]["processed_cards"] = final_merged_cards
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)

    # 1. PURGE ALL OLD NOTES IN ANKI DESKTOP
    print("\nPurging all old Design Patterns notes from Anki Desktop...")
    old_anki_cards = req_anki("findCards", {"query": f'deck:"Backend Engineering::{domain_code}*"'}).get("result", [])
    if old_anki_cards:
        info = req_anki("cardsInfo", {"cards": old_anki_cards}).get("result", [])
        old_note_ids = list(set(c["note"] for c in info if "note" in c))
        if old_note_ids:
            req_anki("deleteNotes", {"notes": old_note_ids})
            print(f"Deleted {len(old_note_ids)} old notes from Anki Desktop.")

    # 2. WRITE MARKDOWN
    md_file = os.path.join(final_dir, f"{domain_code}.md")
    apkg_file = os.path.join(final_dir, f"{domain_code}.apkg")
    
    categories = {}
    for card in final_merged_cards:
        cat = card.get("category", domain_title)
        lvl = card.get("level", "Mid")
        categories.setdefault(cat, {}).setdefault(lvl, []).append(card)
        
    md_content = f"# {domain_code} - {domain_title} Study Guide\n\n"
    md_content += f"- **Total Master Cards**: {len(final_merged_cards)}\n\n---\n"
    
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

    # 3. PACKAGE APKG
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
    
    for card in final_merged_cards:
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

    # 4. IMPORT & RE-ORGANIZE IN ANKI DESKTOP
    import_res = req_anki("importPackage", {"path": os.path.abspath(apkg_file)})
    if import_res.get("error") is None:
        print(f"Imported into Anki Desktop via AnkiConnect!")
        sub_names = ["ju", "mid", "sen"]
        for sub in sub_names:
            old_name = f"Backend Engineering::{domain_code}::{sub}"
            c_ids = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
            if c_ids:
                req_anki("changeDeck", {"cards": c_ids, "deck": old_name})
        print(f"Organized Anki Desktop tree: Backend Engineering::{domain_code} (ju, mid, sen)")

    print("\n==========================================")
    print("DESIGN PATTERNS SEMANTICALLY CONSOLIDATED & SYNCED TO ANKI DESKTOP!")
    print("==========================================")

if __name__ == "__main__":
    main()
