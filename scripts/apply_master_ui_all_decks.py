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

    # Master Anki Model with Category, Level, Source, Highlight.js, and Mermaid support
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

    domain_sources = {
        "01_SQL_PostgreSQL_Mastery": "Markus Winand SQL Performance & Postgres Internals",
        "02_Storage_DDIA": "Designing Data-Intensive Applications (DDIA)",
        "03_Redis_Caching": "Redis High Performance & Caching Architecture",
        "04_Kafka_EventDriven": "Kafka: The Definitive Guide & Event-Driven Architecture",
        "05_SystemDesign_Architecture": "Alex Xu System Design Interview Vol 1 & 2",
        "06_DesignPatterns_OOP": "GoF Design Patterns, Clean Code & DDD",
        "07_ComputerScience_SWE": "Computer Science & Software Engineering Core",
        "08_Networking_Security": "Computer Networking: A Top-Down Approach"
    }

    domain_configs = [
        {"code": "01_SQL_PostgreSQL_Mastery", "title": "SQL & PostgreSQL Mastery", "deck_id": 2059400201},
        {"code": "02_Storage_DDIA", "title": "Storage Engines & Distributed Data (DDIA)", "deck_id": 2059400203},
        {"code": "03_Redis_Caching", "title": "Redis & In-Memory Caching Architecture", "deck_id": 2059400204},
        {"code": "04_Kafka_EventDriven", "title": "Kafka & Event-Driven Systems", "deck_id": 2059400205},
        {"code": "05_SystemDesign_Architecture", "title": "System Design & Distributed Architecture", "deck_id": 2059400206},
        {"code": "06_DesignPatterns_OOP", "title": "Software Design Patterns & Object-Oriented Design", "deck_id": 2059400207},
        {"code": "07_ComputerScience_SWE", "title": "CS Fundamentals & Software Engineering", "deck_id": 2059400208},
        {"code": "08_Networking_Security", "title": "Computer Networking & Security Protocols", "deck_id": 2059400209}
    ]

    for domain in domain_configs:
        code = domain["code"]
        title = domain["title"]
        deck_id = domain["deck_id"]
        source = domain_sources.get(code, "Backend Master Collection")

        cards = progress.get(code, {}).get("processed_cards", [])
        if not cards and code == "01_SQL_PostgreSQL_Mastery":
            # Parse SQL cards if empty in progress
            md_file = os.path.join(final_dir, f"{code}.md")
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

        if not cards:
            print(f"Skipping empty deck {code}.")
            continue

        print(f"\n==========================================")
        print(f"Upgrading UI & Building Master Deck for {code} ({len(cards)} cards)...")
        print(f"==========================================")

        # 1. Purge old notes in Anki Desktop
        old_anki_cards = req_anki("findCards", {"query": f'deck:"Backend Engineering::{code}*"'}).get("result", [])
        if old_anki_cards:
            info = req_anki("findCards", {"query": f'deck:"Backend Engineering::{code}*"'})
            notes_info = req_anki("cardsInfo", {"cards": old_anki_cards}).get("result", [])
            old_note_ids = list(set(c["note"] for c in notes_info if "note" in c))
            if old_note_ids:
                req_anki("deleteNotes", {"notes": old_note_ids})
                print(f"  Deleted {len(old_note_ids)} old notes from Anki Desktop.")

        # 2. Build Subdecks
        deck_ju_name = "ju_optional" if code == "08_Networking_Security" else "ju"
        deck_ju = genanki.Deck(deck_id + 1, f"Backend Engineering::{code}::{deck_ju_name}")
        deck_mid = genanki.Deck(deck_id + 2, f"Backend Engineering::{code}::mid")
        deck_sen = genanki.Deck(deck_id + 3, f"Backend Engineering::{code}::sen")

        decks_by_level = {
            "Junior": deck_ju,
            "Mid": deck_mid,
            "Senior": deck_sen
        }

        for card in cards:
            q = (card.get("question") or card.get("Question") or "").strip()
            a = (card.get("answer") or card.get("Answer") or "").strip()
            cat = card.get("category") or title.split("-")[0].strip()
            lvl = card.get("level") or "Mid"
            if lvl not in decks_by_level:
                lvl = "Mid"
            if not q or not a:
                continue

            note = genanki.Note(
                model=master_model,
                fields=[q, a, cat, lvl, source]
            )
            decks_by_level[lvl].add_note(note)

        apkg_file = os.path.join(final_dir, f"{code}.apkg")
        pkg = genanki.Package([deck_ju, deck_mid, deck_sen])
        pkg.write_to_file(apkg_file)
        print(f"  Compiled APKG: {apkg_file}")

        # 3. Import & Re-organize in Anki Desktop
        import_res = req_anki("importPackage", {"path": os.path.abspath(apkg_file)})
        if import_res.get("error") is None:
            sub_names = [deck_ju_name, "mid", "sen"]
            for sub in sub_names:
                old_name = f"Backend Engineering::{code}::{sub}"
                c_ids = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
                if c_ids:
                    req_anki("changeDeck", {"cards": c_ids, "deck": old_name})
            print(f"  Organized Anki Desktop tree: Backend Engineering::{code} ({deck_ju_name}, mid, sen)")

    print("\n==========================================")
    print("MASTER DARK UI WITH HIGHLIGHT.JS, MERMAID & SOURCES APPLIED TO ALL DECKS!")
    print("==========================================")

if __name__ == "__main__":
    main()
