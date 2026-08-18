import os
import json
import re
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

def parse_markdown_deck(md_path, default_cat, default_subcat, default_lvl="Mid"):
    cards = []
    if not os.path.exists(md_path):
        return cards

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    current_cat = default_cat
    current_subcat = default_subcat
    current_lvl = default_lvl

    sections = content.split("#### ")
    for sec in sections[1:]:
        lines = sec.strip().split("\n")
        title_line = lines[0]
        q = re.sub(r"^\d+\.\s*", "", title_line).strip()

        answer_lines = []
        is_answer = False
        for l in lines[1:]:
            if l.startswith("## 📂 Category:"):
                cat_match = re.search(r"Category:\s*([^\(]+)", l)
                if cat_match:
                    raw_cat = cat_match.group(1).strip()
                    if " & " in raw_cat:
                        parts = raw_cat.split(" & ", 1)
                        current_cat = parts[0].upper()
                        current_subcat = parts[1].upper()
                    elif " - " in raw_cat:
                        parts = raw_cat.split(" - ", 1)
                        current_cat = parts[0].upper()
                        current_subcat = parts[1].upper()
                    else:
                        current_subcat = raw_cat.upper()
            elif l.startswith("### ") and "Level" in l:
                if "Junior" in l:
                    current_lvl = "Junior"
                elif "Senior" in l:
                    current_lvl = "Senior"
                elif "Mid" in l:
                    current_lvl = "Mid"
            elif l.startswith("**Answer:**"):
                is_answer = True
                continue
            elif is_answer:
                answer_lines.append(l)

        a = "\n".join(answer_lines).strip()
        if q and a:
            cards.append({
                "question": q,
                "answer": a,
                "category": current_cat,
                "subcategory": current_subcat,
                "level": current_lvl
            })

    return cards

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    final_dir = os.path.join(current_dir, "final")
    progress_file = os.path.join(final_dir, "progress_all_be.json")

    # Source file mapping to new domain codes
    target_domains = [
        {
            "src_md": "06_DesignPatterns_OOP.md",
            "new_code": "01_DesignPatterns_OOP",
            "title": "Software Design Patterns & Object-Oriented Design",
            "deck_id": 2059400201,
            "source": "GoF Design Patterns, Clean Code & DDD",
            "default_cat": "SOFTWARE DESIGN",
            "default_subcat": "PATTERNS & OOP"
        },
        {
            "src_md": "03_Redis_Caching.md",
            "new_code": "02_Redis_Caching",
            "title": "Redis & In-Memory Caching Architecture",
            "deck_id": 2059400202,
            "source": "Redis High Performance & Caching Architecture",
            "default_cat": "IN-MEMORY STORAGE",
            "default_subcat": "REDIS & CACHING"
        },
        {
            "src_md": "04_Kafka_EventDriven.md",
            "new_code": "03_Kafka_EventDriven",
            "title": "Kafka & Event-Driven Systems",
            "deck_id": 2059400203,
            "source": "Kafka: The Definitive Guide & Event-Driven Architecture",
            "default_cat": "EVENT-DRIVEN",
            "default_subcat": "APACHE KAFKA"
        },
        {
            "src_md": "01_SQL_PostgreSQL_Mastery.md",
            "new_code": "04_SQL_PostgreSQL_Mastery",
            "title": "SQL & PostgreSQL Mastery",
            "deck_id": 2059400204,
            "source": "Markus Winand SQL Performance & Postgres Internals",
            "default_cat": "DATABASE",
            "default_subcat": "POSTGRESQL & SQL"
        },
        {
            "src_md": "02_Storage_DDIA.md",
            "new_code": "05_Storage_DDIA",
            "title": "Storage Engines & Distributed Data (DDIA)",
            "deck_id": 2059400205,
            "source": "Designing Data-Intensive Applications (DDIA)",
            "default_cat": "DISTRIBUTED DATA",
            "default_subcat": "STORAGE ENGINES (DDIA)"
        },
        {
            "src_md": "05_SystemDesign_Architecture.md",
            "new_code": "06_SystemDesign_Architecture",
            "title": "System Design & Distributed Architecture",
            "deck_id": 2059400206,
            "source": "Alex Xu System Design Interview Vol 1 & 2",
            "default_cat": "ARCHITECTURE",
            "default_subcat": "SYSTEM DESIGN"
        },
        {
            "src_md": "08_Networking_Security.md",
            "new_code": "07_Networking_Security",
            "title": "Computer Networking & Security Protocols",
            "deck_id": 2059400207,
            "source": "Computer Networking: A Top-Down Approach",
            "default_cat": "NETWORKING",
            "default_subcat": "SECURITY PROTOCOLS"
        },
        {
            "src_md": "07_ComputerScience_SWE.md",
            "new_code": "08_ComputerScience_SWE_optional",
            "title": "CS Fundamentals & Software Engineering (Optional Reference)",
            "deck_id": 2059400208,
            "source": "Computer Science & Software Engineering Core (Reference)",
            "default_cat": "CS CORE",
            "default_subcat": "SOFTWARE ENGINEERING"
        }
    ]

    # Master Anki Model v3 with Category, SubCategory, Level, and Source
    master_model_v3 = genanki.Model(
        1607392320,
        "Backend Master Model v3",
        fields=[
            {"name": "Question"},
            {"name": "Answer"},
            {"name": "Category"},
            {"name": "SubCategory"},
            {"name": "Level"},
            {"name": "Source"}
        ],
        templates=[
            {
                "name": "Backend Master Card v3",
                "qfmt": """
                <div class="card">
                    <div class="header">
                        <div class="badges">
                            <span class="category">{{Category}}</span>
                            <span class="subcategory">{{SubCategory}}</span>
                        </div>
                        <span class="level {{Level}}">{{Level}}</span>
                    </div>
                    <div class="question">{{Question}}</div>
                </div>
                <style>
                    .card { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 20px; color: #f7fafc; background: #1a202c; border-radius: 12px; border: 1px solid #2d3748; }
                    .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; font-size: 0.78em; text-transform: uppercase; letter-spacing: 0.05em; }
                    .badges { display: flex; gap: 6px; align-items: center; flex-wrap: wrap; }
                    .category { font-weight: 700; color: #a0aec0; background: #2d3748; padding: 3px 8px; border-radius: 4px; border: 1px solid #4a5568; }
                    .subcategory { font-weight: 700; color: #63b3ed; background: #1a365d; padding: 3px 8px; border-radius: 4px; border: 1px solid #2b6cb0; }
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
                        <div class="badges">
                            <span class="category">{{Category}}</span>
                            <span class="subcategory">{{SubCategory}}</span>
                        </div>
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
                    .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; font-size: 0.78em; text-transform: uppercase; letter-spacing: 0.05em; }
                    .badges { display: flex; gap: 6px; align-items: center; flex-wrap: wrap; }
                    .category { font-weight: 700; color: #a0aec0; background: #2d3748; padding: 3px 8px; border-radius: 4px; border: 1px solid #4a5568; }
                    .subcategory { font-weight: 700; color: #63b3ed; background: #1a365d; padding: 3px 8px; border-radius: 4px; border: 1px solid #2b6cb0; }
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

    # 1. Purge all existing notes in Anki Desktop
    print("Purging all existing notes to apply Master Model v3 with Dual Badges...")
    old_be_cards = req_anki("findCards", {"query": 'deck:"Backend Engineering*"'}).get("result", [])
    if old_be_cards:
        info = req_anki("cardsInfo", {"cards": old_be_cards}).get("result", [])
        old_note_ids = list(set(c["note"] for c in info if "note" in c))
        if old_note_ids:
            req_anki("deleteNotes", {"notes": old_note_ids})
            print(f"Deleted {len(old_note_ids)} old notes from Anki Desktop.")

    new_progress = {}

    for dom in target_domains:
        src_md_path = os.path.join(final_dir, dom["src_md"])
        new_code = dom["new_code"]
        title = dom["title"]
        deck_id = dom["deck_id"]
        source = dom["source"]
        default_cat = dom["default_cat"]
        default_subcat = dom["default_subcat"]

        cards = parse_markdown_deck(src_md_path, default_cat, default_subcat)
        print(f"\nParsed {len(cards)} cards for {new_code} with Dual Badges [{default_cat}] [{default_subcat}]")

        new_progress[new_code] = {
            "last_batch_idx": 999,
            "processed_cards": cards
        }

        # Build APKG
        deck_ju_name = "ju_optional" if "Networking" in new_code else "ju"
        deck_ju = genanki.Deck(deck_id + 1, f"Backend Engineering::{new_code}::{deck_ju_name}")
        deck_mid = genanki.Deck(deck_id + 2, f"Backend Engineering::{new_code}::mid")
        deck_sen = genanki.Deck(deck_id + 3, f"Backend Engineering::{new_code}::sen")
        decks_by_level = {"Junior": deck_ju, "Mid": deck_mid, "Senior": deck_sen}

        for card in cards:
            q = card["question"]
            a = card["answer"]
            cat = card.get("category") or default_cat
            subcat = card.get("subcategory") or default_subcat
            lvl = card.get("level") or "Mid"
            if lvl not in decks_by_level:
                lvl = "Mid"
            note = genanki.Note(model=master_model_v3, fields=[q, a, cat, subcat, lvl, source])
            decks_by_level[lvl].add_note(note)

        apkg_file = os.path.join(final_dir, f"{new_code}.apkg")
        pkg = genanki.Package([deck_ju, deck_mid, deck_sen])
        pkg.write_to_file(apkg_file)

        req_anki("importPackage", {"path": os.path.abspath(apkg_file)})
        for sub in [deck_ju_name, "mid", "sen"]:
            old_name = f"Backend Engineering::{new_code}::{sub}"
            c_ids = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
            if c_ids:
                req_anki("changeDeck", {"cards": c_ids, "deck": old_name})

        print(f"Successfully imported {new_code} into Anki Desktop!")

    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(new_progress, f, indent=2)

    print("\n==========================================")
    print("MASTER MODEL V3 WITH DUAL BADGES (CATEGORY + SUBCATEGORY) SUCCESSFULLY APPLIED!")
    print("==========================================")

if __name__ == "__main__":
    main()
