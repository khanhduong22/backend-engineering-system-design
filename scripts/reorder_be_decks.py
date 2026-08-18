import os
import json
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

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    final_dir = os.path.join(current_dir, "final")
    progress_file = os.path.join(final_dir, "progress_all_be.json")

    with open(progress_file, "r") as f:
        progress = json.load(f)

    # Key mapping between potential old keys and new domain codes
    new_domain_order = [
        {"keys": ["01_DesignPatterns_OOP", "06_DesignPatterns_OOP"], "new_code": "01_DesignPatterns_OOP", "title": "Software Design Patterns & Object-Oriented Design", "deck_id": 2059400201},
        {"keys": ["02_Redis_Caching", "03_Redis_Caching"], "new_code": "02_Redis_Caching", "title": "Redis & In-Memory Caching Architecture", "deck_id": 2059400202},
        {"keys": ["03_Kafka_EventDriven", "04_Kafka_EventDriven"], "new_code": "03_Kafka_EventDriven", "title": "Kafka & Event-Driven Systems", "deck_id": 2059400203},
        {"keys": ["04_SQL_PostgreSQL_Mastery", "01_SQL_PostgreSQL_Mastery"], "new_code": "04_SQL_PostgreSQL_Mastery", "title": "SQL & PostgreSQL Mastery", "deck_id": 2059400204},
        {"keys": ["05_Storage_DDIA", "02_Storage_DDIA"], "new_code": "05_Storage_DDIA", "title": "Storage Engines & Distributed Data (DDIA)", "deck_id": 2059400205},
        {"keys": ["06_SystemDesign_Architecture", "05_SystemDesign_Architecture"], "new_code": "06_SystemDesign_Architecture", "title": "System Design & Distributed Architecture", "deck_id": 2059400206},
        {"keys": ["07_Networking_Security", "08_Networking_Security"], "new_code": "07_Networking_Security", "title": "Computer Networking & Security Protocols", "deck_id": 2059400207},
        {"keys": ["08_ComputerScience_SWE_optional", "07_ComputerScience_SWE"], "new_code": "08_ComputerScience_SWE_optional", "title": "CS Fundamentals & Software Engineering (Optional Reference)", "deck_id": 2059400208}
    ]

    domain_sources = {
        "01_DesignPatterns_OOP": "GoF Design Patterns, Clean Code & DDD",
        "02_Redis_Caching": "Redis High Performance & Caching Architecture",
        "03_Kafka_EventDriven": "Kafka: The Definitive Guide & Event-Driven Architecture",
        "04_SQL_PostgreSQL_Mastery": "Markus Winand SQL Performance & Postgres Internals",
        "05_Storage_DDIA": "Designing Data-Intensive Applications (DDIA)",
        "06_SystemDesign_Architecture": "Alex Xu System Design Interview Vol 1 & 2",
        "07_Networking_Security": "Computer Networking: A Top-Down Approach",
        "08_ComputerScience_SWE_optional": "Computer Science & Software Engineering Core (Reference)"
    }

    # 1. Purge entire old Backend Engineering deck tree in Anki Desktop
    print("Purging old Backend Engineering deck tree from Anki Desktop...")
    old_be_cards = req_anki("findCards", {"query": 'deck:"Backend Engineering*"'}).get("result", [])
    if old_be_cards:
        info = req_anki("cardsInfo", {"cards": old_be_cards}).get("result", [])
        old_note_ids = list(set(c["note"] for c in info if "note" in c))
        if old_note_ids:
            req_anki("deleteNotes", {"notes": old_note_ids})
            print(f"Deleted {len(old_note_ids)} old notes from Anki Desktop.")

    # Delete standalone decks
    standalone_decks = [d for d in req_anki("deckNames").get("result", []) if "SQL_Master" in d]
    if standalone_decks:
        req_anki("deleteDecks", {"decks": standalone_decks, "cardsToo": True})

    # Master Anki Model v2
    master_model = genanki.Model(
        1607392319,
        "Backend Master Model v2",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
            {"name": "Category"},
            {"name": "Level"},
            {"name": "Source"}
        ],
        templates=[
            {
                "name": "Backend Master Card",
                "qfmt": """
                <div class="card">
                    <div class="header">
                        <span class="category">{{Category}}</span>
                        <span class="level {{Level}}">{{Level}}</span>
                    </div>
                    <div class="question">{{Question}}</div>
                </div>
                <style>
                    .card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 22px; color: #f7fafc; background: #1a202c; border-radius: 14px; border: 1px solid #2d3748; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3); }
                    .header { display: flex; justify-content: space-between; margin-bottom: 16px; font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.08em; }
                    .category { font-weight: 700; color: #cbd5e0; background: #2d3748; padding: 4px 10px; border-radius: 6px; border: 1px solid #4a5568; }
                    .level { font-weight: 700; padding: 4px 10px; border-radius: 6px; color: white; text-shadow: 0 1px 2px rgba(0,0,0,0.5); }
                    .level.Junior { background: #276749; border: 1px solid #38a169; }
                    .level.Mid { background: #9b6d06; border: 1px solid #d69e2e; }
                    .level.Senior { background: #9b2c2c; border: 1px solid #e53e3e; }
                    .question { font-size: 1.25em; font-weight: 600; line-height: 1.5; color: #ffffff; }
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
                    {{#Source}}
                    <div class="source-footer">📖 Source: {{Source}}</div>
                    {{/Source}}
                </div>
                <style>
                    @import url('https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/atom-one-dark.min.css');
                    .card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 22px; color: #e2e8f0; background: #1a202c; border-radius: 14px; border: 1px solid #2d3748; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3); }
                    .header { display: flex; justify-content: space-between; margin-bottom: 16px; font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.08em; }
                    .category { font-weight: 700; color: #cbd5e0; background: #2d3748; padding: 4px 10px; border-radius: 6px; border: 1px solid #4a5568; }
                    .level { font-weight: 700; padding: 4px 10px; border-radius: 6px; color: white; text-shadow: 0 1px 2px rgba(0,0,0,0.5); }
                    .level.Junior { background: #276749; border: 1px solid #38a169; }
                    .level.Mid { background: #9b6d06; border: 1px solid #d69e2e; }
                    .level.Senior { background: #9b2c2c; border: 1px solid #e53e3e; }
                    .question { font-size: 1.25em; font-weight: 600; line-height: 1.5; color: #ffffff; margin-bottom: 15px; }
                    hr#answer { border: 0; height: 1px; background: #4a5568; margin: 20px 0; }
                    .answer { font-size: 1.05em; line-height: 1.6; color: #e2e8f0; white-space: pre-wrap; }
                    .source-footer { margin-top: 20px; padding-top: 10px; border-top: 1px dashed #4a5568; font-size: 0.8em; color: #a0aec0; font-style: italic; }
                    pre { background: #111827; padding: 14px; border-radius: 8px; overflow-x: auto; border: 1px solid #374151; }
                    code { font-family: "Fira Code", Monaco, Consolas, "Courier New", monospace; font-size: 0.9em; }
                </style>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
                <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
                <script>
                  try {
                    hljs.highlightAll();
                    mermaid.initialize({ startOnLoad: true, theme: 'dark' });
                  } catch(e) {}
                </script>
                """
            }
        ]
    )

    new_progress = {}

    for item in new_domain_order:
        possible_keys = item["keys"]
        new_code = item["new_code"]
        title = item["title"]
        deck_id = item["deck_id"]
        source = domain_sources.get(new_code, "Backend Master Collection")

        cards = []
        for k in possible_keys:
            if k in progress and progress[k].get("processed_cards"):
                cards = progress[k]["processed_cards"]
                break

        if not cards and "SQL" in new_code:
            md_file = os.path.join(final_dir, f"{new_code}.md")
            if not os.path.exists(md_file):
                md_file = os.path.join(final_dir, "01_SQL_PostgreSQL_Mastery.md")
            if os.path.exists(md_file):
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()
                sections = content.split("#### ")
                for sec in sections[1:]:
                    lines = sec.strip().split("\n")
                    q = lines[0].strip()
                    ans_lines = [l for l in lines[1:] if not l.startswith("**Answer:**")]
                    a = "\n".join(ans_lines).strip()
                    if q and a:
                        cards.append({"question": q, "answer": a, "category": "SQL & PostgreSQL", "level": "Mid"})

        print(f"\n==========================================")
        print(f"Re-indexing ➔ {new_code} ({len(cards)} cards)...")
        print(f"==========================================")

        new_progress[new_code] = {
            "last_batch_idx": 999,
            "processed_cards": cards
        }

        # Build Markdown
        md_file = os.path.join(final_dir, f"{new_code}.md")
        categories = {}
        for card in cards:
            cat = card.get("category", title)
            lvl = card.get("level", "Mid")
            categories.setdefault(cat, {}).setdefault(lvl, []).append(card)

        md_content = f"# {new_code} - {title} Study Guide\n\n- **Total Cards**: {len(cards)}\n\n---\n"
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
                for idx, card in enumerate(sorted(lcards, key=lambda c: c.get("question", "")), 1):
                    md_content += f"#### {idx}. {card.get('question', '').strip()}\n**Answer:**\n{card.get('answer', '').strip()}\n\n"

        with open(md_file, "w", encoding="utf-8") as f:
            f.write(md_content)

        # Build APKG
        deck_ju_name = "ju_optional" if "Networking" in new_code else "ju"
        deck_ju = genanki.Deck(deck_id + 1, f"Backend Engineering::{new_code}::{deck_ju_name}")
        deck_mid = genanki.Deck(deck_id + 2, f"Backend Engineering::{new_code}::mid")
        deck_sen = genanki.Deck(deck_id + 3, f"Backend Engineering::{new_code}::sen")
        decks_by_level = {"Junior": deck_ju, "Mid": deck_mid, "Senior": deck_sen}

        for card in cards:
            q = (card.get("question") or card.get("Question") or "").strip()
            a = (card.get("answer") or card.get("Answer") or "").strip()
            cat = card.get("category") or title.split("-")[0].strip()
            lvl = card.get("level") or "Mid"
            if lvl not in decks_by_level:
                lvl = "Mid"
            if not q or not a:
                continue
            note = genanki.Note(model=master_model, fields=[q, a, cat, lvl, source])
            decks_by_level[lvl].add_note(note)

        apkg_file = os.path.join(final_dir, f"{new_code}.apkg")
        pkg = genanki.Package([deck_ju, deck_mid, deck_sen])
        pkg.write_to_file(apkg_file)

        # Import & Organize in Anki Desktop
        req_anki("importPackage", {"path": os.path.abspath(apkg_file)})
        for sub in [deck_ju_name, "mid", "sen"]:
            old_name = f"Backend Engineering::{new_code}::{sub}"
            c_ids = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
            if c_ids:
                req_anki("changeDeck", {"cards": c_ids, "deck": old_name})

        print(f"Successfully re-ordered & imported {new_code} into Anki Desktop!")

    # Save new progress checkpoint
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(new_progress, f, indent=2)

    print("\n==========================================")
    print("BACKEND ENGINEERING TREE SUCCESSFULLY RE-ORDERED TO USER HIGH-ROI SEQUENCE!")
    print("==========================================")

if __name__ == "__main__":
    main()
