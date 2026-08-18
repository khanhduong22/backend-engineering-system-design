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

    # 1. Fetch all cards from standalone SQL_Master deck
    sql_master_cards = req_anki("findCards", {"query": 'deck:"SQL_Master*"'}).get("result", [])
    sql_master_info = req_anki("cardsInfo", {"cards": sql_master_cards}).get("result", []) if sql_master_cards else []

    extracted_sql_cards = []
    seen_q = set()

    for c in sql_master_info:
        fields = c.get("fields", {})
        q = fields.get("Question", {}).get("value", "") or fields.get("Front", {}).get("value", "")
        a = fields.get("Answer", {}).get("value", "") or fields.get("Back", {}).get("value", "")
        d_name = c.get("deckName", "")

        q_clean = q.strip()
        a_clean = a.strip()
        if not q_clean or q_clean.lower() in seen_q:
            continue
        seen_q.add(q_clean.lower())

        # Determine level/category
        lvl = "Mid"
        if "ju" in d_name.lower():
            lvl = "Junior"
        elif "sen" in d_name.lower():
            lvl = "Senior"
        elif "mid" in d_name.lower():
            lvl = "Mid"

        cat = "SQL & PostgreSQL"
        if "pgrest" in d_name.lower() or "postgrest" in q_clean.lower() or "postgres" in q_clean.lower():
            cat = "PostgreSQL Internals"

        extracted_sql_cards.append({
            "question": q_clean,
            "answer": a_clean,
            "category": cat,
            "level": lvl
        })

    print(f"Extracted & Deduplicated {len(extracted_sql_cards)} cards from standalone SQL_Master deck.")

    # 2. Master Anki Model v2
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

    domain_code = "04_SQL_PostgreSQL_Mastery"
    deck_id = 2059400204
    source = "Markus Winand SQL Performance & Postgres Internals"

    # Purge old 04 deck in Anki Desktop
    print("Purging existing Backend Engineering::04_SQL_PostgreSQL_Mastery notes...")
    old_04_cards = req_anki("findCards", {"query": f'deck:"Backend Engineering::{domain_code}*"'}).get("result", [])
    if old_04_cards:
        notes_info = req_anki("cardsInfo", {"cards": old_04_cards}).get("result", [])
        old_note_ids = list(set(c["note"] for c in notes_info if "note" in c))
        if old_note_ids:
            req_anki("deleteNotes", {"notes": old_note_ids})

    deck_ju = genanki.Deck(deck_id + 1, f"Backend Engineering::{domain_code}::ju")
    deck_mid = genanki.Deck(deck_id + 2, f"Backend Engineering::{domain_code}::mid")
    deck_sen = genanki.Deck(deck_id + 3, f"Backend Engineering::{domain_code}::sen")
    decks_by_level = {"Junior": deck_ju, "Mid": deck_mid, "Senior": deck_sen}

    for card in extracted_sql_cards:
        q = card["question"]
        a = card["answer"]
        cat = card["category"]
        lvl = card["level"]
        note = genanki.Note(model=master_model, fields=[q, a, cat, lvl, source])
        decks_by_level[lvl].add_note(note)

    apkg_file = os.path.join(final_dir, f"{domain_code}.apkg")
    pkg = genanki.Package([deck_ju, deck_mid, deck_sen])
    pkg.write_to_file(apkg_file)

    req_anki("importPackage", {"path": os.path.abspath(apkg_file)})

    # Delete standalone SQL_Master deck completely
    print("Deleting standalone SQL_Master deck from Anki Desktop...")
    standalone_decks = [d for d in req_anki("deckNames").get("result", []) if "SQL_Master" in d]
    if standalone_decks:
        req_anki("deleteDecks", {"decks": standalone_decks, "cardsToo": True})

    # Update progress checkpoint
    with open(progress_file, "r") as f:
        progress = json.load(f)

    progress[domain_code] = {
        "last_batch_idx": 999,
        "processed_cards": extracted_sql_cards
    }

    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)

    print("\n==========================================")
    print("STANDALONE SQL_MASTER FULLY MERGED INTO Backend Engineering::04_SQL_PostgreSQL_Mastery (ju, mid, sen)!")
    print("==========================================")

if __name__ == "__main__":
    main()
