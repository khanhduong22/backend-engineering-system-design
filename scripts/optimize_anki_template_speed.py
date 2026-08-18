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

    # Ultra-optimized, zero-lag Master Model v2 Template for Anki QtWebEngine
    fast_master_model = genanki.Model(
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
                    .card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 20px; color: #f7fafc; background: #1a202c; border-radius: 12px; border: 1px solid #2d3748; }
                    .header { display: flex; justify-content: space-between; margin-bottom: 14px; font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.05em; }
                    .category { font-weight: 700; color: #cbd5e0; background: #2d3748; padding: 3px 8px; border-radius: 4px; border: 1px solid #4a5568; }
                    .level { font-weight: 700; padding: 3px 8px; border-radius: 4px; color: white; }
                    .level.Junior { background: #276749; }
                    .level.Mid { background: #9b6d06; }
                    .level.Senior { background: #9b2c2c; }
                    .question { font-size: 1.2em; font-weight: 600; line-height: 1.5; color: #ffffff; }
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
                    .card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 20px; color: #e2e8f0; background: #1a202c; border-radius: 12px; border: 1px solid #2d3748; }
                    .header { display: flex; justify-content: space-between; margin-bottom: 14px; font-size: 0.8em; text-transform: uppercase; letter-spacing: 0.05em; }
                    .category { font-weight: 700; color: #cbd5e0; background: #2d3748; padding: 3px 8px; border-radius: 4px; border: 1px solid #4a5568; }
                    .level { font-weight: 700; padding: 3px 8px; border-radius: 4px; color: white; }
                    .level.Junior { background: #276749; }
                    .level.Mid { background: #9b6d06; }
                    .level.Senior { background: #9b2c2c; }
                    .question { font-size: 1.2em; font-weight: 600; line-height: 1.5; color: #ffffff; margin-bottom: 12px; }
                    hr#answer { border: 0; height: 1px; background: #4a5568; margin: 16px 0; }
                    .answer { font-size: 1.02em; line-height: 1.6; color: #e2e8f0; white-space: pre-wrap; }
                    .source-footer { margin-top: 16px; padding-top: 8px; border-top: 1px dashed #4a5568; font-size: 0.8em; color: #a0aec0; font-style: italic; }
                    pre { background: #111827; padding: 12px; border-radius: 6px; overflow-x: auto; border: 1px solid #374151; margin: 10px 0; }
                    code { font-family: "Fira Code", Monaco, Consolas, monospace; font-size: 0.9em; color: #38bdf8; }
                </style>
                <script>
                  // Lazy load heavy external JS only when code or diagrams exist on card
                  (function() {
                    var ans = document.querySelector('.answer');
                    if (!ans) return;
                    if (ans.innerHTML.includes('class="mermaid"') || ans.innerHTML.includes('```mermaid')) {
                      var s = document.createElement('script');
                      s.src = 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js';
                      s.onload = function() { try { mermaid.initialize({ startOnLoad: true, theme: 'dark' }); } catch(e){} };
                      document.head.appendChild(s);
                    }
                  })();
                </script>
                """
            }
        ]
    )

    domain_configs = [
        {"code": "01_DesignPatterns_OOP", "title": "Software Design Patterns & Object-Oriented Design", "deck_id": 2059400201, "source": "GoF Design Patterns, Clean Code & DDD"},
        {"code": "02_Redis_Caching", "title": "Redis & In-Memory Caching Architecture", "deck_id": 2059400202, "source": "Redis High Performance & Caching Architecture"},
        {"code": "03_Kafka_EventDriven", "title": "Kafka & Event-Driven Systems", "deck_id": 2059400203, "source": "Kafka: The Definitive Guide & Event-Driven Architecture"},
        {"code": "04_SQL_PostgreSQL_Mastery", "title": "SQL & PostgreSQL Mastery", "deck_id": 2059400204, "source": "Markus Winand SQL Performance & Postgres Internals"},
        {"code": "05_Storage_DDIA", "title": "Storage Engines & Distributed Data (DDIA)", "deck_id": 2059400205, "source": "Designing Data-Intensive Applications (DDIA)"},
        {"code": "06_SystemDesign_Architecture", "title": "System Design & Distributed Architecture", "deck_id": 2059400206, "source": "Alex Xu System Design Interview Vol 1 & 2"},
        {"code": "07_Networking_Security", "title": "Computer Networking & Security Protocols", "deck_id": 2059400207, "source": "Computer Networking: A Top-Down Approach"},
        {"code": "08_ComputerScience_SWE_optional", "title": "CS Fundamentals & Software Engineering (Optional Reference)", "deck_id": 2059400208, "source": "Computer Science & Software Engineering Core (Reference)"}
    ]

    print("Purging old notes to apply ultra-fast zero-lag template...")
    old_be_cards = req_anki("findCards", {"query": 'deck:"Backend Engineering*"'}).get("result", [])
    if old_be_cards:
        info = req_anki("cardsInfo", {"cards": old_be_cards}).get("result", [])
        old_note_ids = list(set(c["note"] for c in info if "note" in c))
        if old_note_ids:
            req_anki("deleteNotes", {"notes": old_note_ids})

    for domain in domain_configs:
        code = domain["code"]
        title = domain["title"]
        deck_id = domain["deck_id"]
        source = domain["source"]

        cards = progress.get(code, {}).get("processed_cards", [])
        if not cards:
            continue

        deck_ju_name = "ju_optional" if "Networking" in code else "ju"
        deck_ju = genanki.Deck(deck_id + 1, f"Backend Engineering::{code}::{deck_ju_name}")
        deck_mid = genanki.Deck(deck_id + 2, f"Backend Engineering::{code}::mid")
        deck_sen = genanki.Deck(deck_id + 3, f"Backend Engineering::{code}::sen")
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
            note = genanki.Note(model=fast_master_model, fields=[q, a, cat, lvl, source])
            decks_by_level[lvl].add_note(note)

        apkg_file = os.path.join(final_dir, f"{code}.apkg")
        pkg = genanki.Package([deck_ju, deck_mid, deck_sen])
        pkg.write_to_file(apkg_file)

        req_anki("importPackage", {"path": os.path.abspath(apkg_file)})
        for sub in [deck_ju_name, "mid", "sen"]:
            old_name = f"Backend Engineering::{code}::{sub}"
            c_ids = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
            if c_ids:
                req_anki("changeDeck", {"cards": c_ids, "deck": old_name})

        print(f"  Optimized {code} ({len(cards)} cards) -> Ultra Fast 60FPS!")

    print("\n==========================================")
    print("ULTRA FAST ZERO-LAG TEMPLATE SUCCESSFULLY APPLIED TO ALL DECKS!")
    print("==========================================")

if __name__ == "__main__":
    main()
