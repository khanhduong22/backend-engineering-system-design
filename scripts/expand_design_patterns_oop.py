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

def call_gemini_refine_oop(api_keys, cards_batch, concept_name):
    if isinstance(api_keys, str):
        api_keys = [api_keys]

    models_to_try = [
        "gemini-flash-lite-latest",
        "gemini-3.5-flash-lite",
        "gemini-3.5-flash"
    ]
    
    prompt = f"""You are a Principal Software Architect and OOP/Clean Code/DDD expert.
Your task is to merge, refine, and consolidate flashcard variants for: "{concept_name}".

STRICT INSTRUCTIONS FOR "{concept_name}":
1. CONSOLIDATE INTO 1 OR 2 HIGH-VALUE MASTER CARDS MAXIMUM.
   - Question: Clear, definitive technical question about {concept_name}.
   - Answer MUST combine:
     - Core Definition & Fundamental Concept
     - Real-world Code Example or Architecture Pattern
     - Trade-offs / Best Practices / How to avoid anti-patterns
2. Preserve all code snippets and key software architecture details.
3. Level Classification: Grade each card as 'Junior', 'Mid', or 'Senior'.
4. Language: English only.

OUTPUT FORMAT (JSON):
{{
  "cards": [
    {{
      "question": "string",
      "answer": "string",
      "category": "OOP & Clean Architecture",
      "level": "Junior | Mid | Senior"
    }}
  ]
}}

Flashcard variants to consolidate:
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

    # Fallback if API fails
    return cards_batch[:2]

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

    with open(progress_file, "r") as f:
        progress = json.load(f)

    # 1. Load existing 39 Design Patterns cards
    existing_pattern_cards = progress.get("06_DesignPatterns_OOP", {}).get("processed_cards", [])
    print(f"Loaded {len(existing_pattern_cards)} existing Design Pattern master cards.")

    # 2. Extract OOP / Code Smells / DDD cards from Domain 07
    cs_cards = progress.get("07_ComputerScience_SWE", {}).get("processed_cards", [])
    print(f"Loaded {len(cs_cards)} cards from 07_ComputerScience_SWE.")

    oop_topics = {
        "OOP 4 Pillars & Fundamentals": ["polymorphism", "encapsulation", "abstraction", "inheritance", "object oriented"],
        "Composition vs Inheritance & Coupling": ["composition", "coupling", "cohesion", "demeter", "liskov"],
        "Code Smells & Clean Code": ["code smell", "god object", "feature envy", "primitive obsession", "clean code", "duplicated code"],
        "Refactoring Patterns": ["refactoring", "extract method", "replace conditional"],
        "Domain-Driven Design (DDD)": ["domain-driven", "ddd", "aggregate", "value object", "entity", "anemic", "bounded context"],
        "Dependency Injection & IoC": ["dependency injection", "inversion of control", "ioc"]
    }

    topic_groups = {}
    for c in cs_cards:
        q = (c.get("question") or "").strip()
        a = (c.get("answer") or "").strip()
        text = (q + " " + a).lower()

        for t_name, keywords in oop_topics.items():
            if any(k in text for k in keywords):
                topic_groups.setdefault(t_name, []).append(c)
                break

    print(f"\nGrouped OOP cards into {len(topic_groups)} topic clusters:")
    for t_name, g_cards in topic_groups.items():
        print(f"  - {t_name}: {len(g_cards)} raw cards")

    # 3. Consolidate OOP clusters using Gemini AI
    new_oop_master_cards = []
    for t_name, g_cards in sorted(topic_groups.items()):
        print(f"\n  Consolidating cluster: '{t_name}' ({len(g_cards)} cards)...", flush=True)
        # Sub-batch if large
        sub_batch_size = 15
        for i in range(0, len(g_cards), sub_batch_size):
            sub = g_cards[i:i + sub_batch_size]
            res = call_gemini_refine_oop(api_keys, sub, t_name)
            for rc in res:
                rc["category"] = f"OOP & {t_name.split('&')[0].strip()}"
                new_oop_master_cards.append(rc)

    print(f"\nExtracted & Consolidated {len(new_oop_master_cards)} new OOP/Clean Code/DDD Master Cards.")

    # 4. Merge with existing Design Patterns master cards
    combined_master_cards = existing_pattern_cards + new_oop_master_cards

    # Deduplicate combined questions
    seen_q = set()
    final_cards = []
    for c in combined_master_cards:
        q = (c.get("question") or "").strip()
        if not q or q.lower() in seen_q:
            continue
        seen_q.add(q.lower())
        final_cards.append(c)

    domain_code = "06_DesignPatterns_OOP"
    domain_title = "Software Design Patterns & Object-Oriented Design"
    deck_id = 2059400207

    print(f"\nFinal Expanded {domain_code}: {len(final_cards)} total Master Cards.")

    # Update progress checkpoint
    progress[domain_code]["processed_cards"] = final_cards
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)

    # 5. PURGE ALL OLD NOTES IN ANKI DESKTOP
    print("\nPurging existing notes for 06_DesignPatterns_OOP from Anki Desktop...")
    old_anki_cards = req_anki("findCards", {"query": f'deck:"Backend Engineering::{domain_code}*"'}).get("result", [])
    if old_anki_cards:
        info = req_anki("cardsInfo", {"cards": old_anki_cards}).get("result", [])
        old_note_ids = list(set(c["note"] for c in info if "note" in c))
        if old_note_ids:
            req_anki("deleteNotes", {"notes": old_note_ids})
            print(f"Deleted {len(old_note_ids)} old notes from Anki Desktop.")

    # 6. WRITE MARKDOWN & BUILD APKG
    md_file = os.path.join(final_dir, f"{domain_code}.md")
    apkg_file = os.path.join(final_dir, f"{domain_code}.apkg")

    categories = {}
    for card in final_cards:
        cat = card.get("category", domain_title)
        lvl = card.get("level", "Mid")
        categories.setdefault(cat, {}).setdefault(lvl, []).append(card)

    md_content = f"# {domain_code} - {domain_title} Study Guide\n\n"
    md_content += f"- **Total Master Cards**: {len(final_cards)}\n\n---\n"

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

    # Build APKG with beautiful Model Template
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
    decks_by_level = {"Junior": deck_ju, "Mid": deck_mid, "Senior": deck_sen}

    for card in final_cards:
        q = (card.get("question") or "").strip()
        a = (card.get("answer") or "").strip()
        cat = card.get("category", domain_title)
        lvl = card.get("level", "Mid")
        if lvl not in decks_by_level:
            lvl = "Mid"
        if not q or not a:
            continue
        note = genanki.Note(model=anki_model, fields=[q, a, cat, lvl])
        decks_by_level[lvl].add_note(note)

    pkg = genanki.Package([deck_ju, deck_mid, deck_sen])
    pkg.write_to_file(apkg_file)
    print(f"Compiled APKG: {apkg_file}")

    # 7. IMPORT TO ANKI DESKTOP
    import_res = req_anki("importPackage", {"path": os.path.abspath(apkg_file)})
    if import_res.get("error") is None:
        print(f"Imported into Anki Desktop via AnkiConnect!")
        for sub in ["ju", "mid", "sen"]:
            old_name = f"Backend Engineering::{domain_code}::{sub}"
            c_ids = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
            if c_ids:
                req_anki("changeDeck", {"cards": c_ids, "deck": old_name})
        print(f"Organized Anki Desktop tree: Backend Engineering::{domain_code} (ju, mid, sen)")

    print("\n==========================================")
    print("DOMAIN 06 SUCCESSFULLY EXPANDED WITH OOP, CODE SMELLS & DDD MASTER CARDS!")
    print("==========================================")

if __name__ == "__main__":
    main()
