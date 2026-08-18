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

def parse_sql_md(md_path):
    cards = []
    if not os.path.exists(md_path):
        return cards
        
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    current_level = "Mid"
    current_category = "SQL & PostgreSQL"

    sections = content.split("#### ")
    for sec in sections[1:]:
        lines = sec.strip().split("\n")
        title_line = lines[0]
        # Clean title number e.g. "1. Advanced SQL Tips" -> "Advanced SQL Tips"
        q = re.sub(r"^\d+\.\s*", "", title_line).strip()

        answer_lines = []
        is_answer = False
        for l in lines[1:]:
            if l.startswith("**Answer:**"):
                is_answer = True
                continue
            if is_answer:
                answer_lines.append(l)

        a = "\n".join(answer_lines).strip()
        if q and a:
            cards.append({
                "question": q,
                "answer": a,
                "category": current_category,
                "level": current_level
            })
            
    return cards

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    final_dir = os.path.join(current_dir, "final")
    md_file = os.path.join(final_dir, "01_SQL_PostgreSQL_Mastery.md")
    apkg_file = os.path.join(final_dir, "01_SQL_PostgreSQL_Mastery.apkg")

    domain_code = "01_SQL_PostgreSQL_Mastery"
    domain_title = "SQL & PostgreSQL Mastery"
    deck_id = 2059400201

    sql_cards = parse_sql_md(md_file)
    print(f"Parsed {len(sql_cards)} cards from {md_file}")

    if not sql_cards:
        print("No cards parsed.")
        return

    # Purge old notes from Anki Desktop
    print("Purging existing SQL notes from Anki Desktop...")
    old_cards = req_anki("findCards", {"query": f'deck:"Backend Engineering::{domain_code}*"'}).get("result", [])
    if old_cards:
        info = req_anki("cardsInfo", {"cards": old_cards}).get("result", [])
        old_note_ids = list(set(c["note"] for c in info if "note" in c))
        if old_note_ids:
            req_anki("deleteNotes", {"notes": old_note_ids})
            print(f"Deleted {len(old_note_ids)} old SQL notes from Anki Desktop.")

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

    for card in sql_cards:
        q = card.get("question", "").strip()
        a = card.get("answer", "").strip()
        cat = card.get("category") or "SQL & PostgreSQL"
        lvl = card.get("level") or "Mid"
        if lvl not in decks_by_level:
            lvl = "Mid"
        if not q or not a:
            continue
        note = genanki.Note(model=anki_model, fields=[q, a, cat, lvl])
        decks_by_level[lvl].add_note(note)

    pkg = genanki.Package([deck_ju, deck_mid, deck_sen])
    pkg.write_to_file(apkg_file)
    print(f"Compiled APKG: {apkg_file}")

    req_anki("importPackage", {"path": os.path.abspath(apkg_file)})
    for sub in ["ju", "mid", "sen"]:
        old_name = f"Backend Engineering::{domain_code}::{sub}"
        c_ids = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
        if c_ids:
            req_anki("changeDeck", {"cards": c_ids, "deck": old_name})

    print(f"Successfully upgraded UI for {domain_code} in Anki Desktop!")

if __name__ == "__main__":
    main()
