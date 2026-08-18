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

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    final_dir = os.path.join(current_dir, "final")
    progress_file = os.path.join(final_dir, "progress_all_be.json")

    with open(progress_file, "r") as f:
        progress = json.load(f)

    # Keywords to purge from Redis deck
    bigdata_keywords = [
        'hdfs', 'sqoop', 'yarn', 'kerberos', 'hadoop', 'spark', 'mapreduce',
        'hive', 'pig', 'flume', 'nifi', 'hbase', 'oozie', 'cloudera', 'impala', 'drill'
    ]

    domain_code = "02_Redis_Caching"
    old_code_alias = "03_Redis_Caching"

    raw_cards = []
    if domain_code in progress and progress[domain_code].get("processed_cards"):
        raw_cards = progress[domain_code]["processed_cards"]
    elif old_code_alias in progress and progress[old_code_alias].get("processed_cards"):
        raw_cards = progress[old_code_alias]["processed_cards"]

    # Fallback to markdown if progress empty
    if not raw_cards:
        md_file = os.path.join(final_dir, "03_Redis_Caching.md")
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
                    raw_cards.append({"question": q, "answer": a, "category": "IN-MEMORY STORAGE", "subcategory": "REDIS & CACHING", "level": "Mid"})

    print(f"Loaded {len(raw_cards)} initial cards for Redis deck.")

    pure_redis_cards = []
    purged_cards = []

    for card in raw_cards:
        q = (card.get("question") or card.get("Question") or "").strip()
        a = (card.get("answer") or card.get("Answer") or "").strip()
        text = (q + " " + a).lower()

        # Check if card is Big Data / Hadoop and NOT related to Redis or general caching
        is_bad = any(k in text for k in bigdata_keywords) and not ('redis' in text or 'cache' in text or 'memcached' in text)
        if is_bad:
            purged_cards.append(q)
        else:
            card["category"] = "IN-MEMORY STORAGE"
            card["subcategory"] = "REDIS & CACHING"
            pure_redis_cards.append(card)

    print(f"\nPURGED {len(purged_cards)} Big Data / Hadoop cards from Redis deck.")
    print(f"RETAINED {len(pure_redis_cards)} PURE Redis & Caching Master Cards!")

    # 1. Purge old notes from Anki Desktop
    old_anki_cards = req_anki("findCards", {"query": f'deck:"Backend Engineering::{domain_code}*"'}).get("result", [])
    if old_anki_cards:
        info = req_anki("cardsInfo", {"cards": old_anki_cards}).get("result", [])
        old_note_ids = list(set(c["note"] for c in info if "note" in c))
        if old_note_ids:
            req_anki("deleteNotes", {"notes": old_note_ids})
            print(f"Deleted {len(old_note_ids)} old notes from Anki Desktop.")

    # 2. Master Model v3
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

    deck_id = 2059400202
    source = "Redis High Performance & Caching Architecture"

    deck_ju = genanki.Deck(deck_id + 1, f"Backend Engineering::{domain_code}::ju")
    deck_mid = genanki.Deck(deck_id + 2, f"Backend Engineering::{domain_code}::mid")
    deck_sen = genanki.Deck(deck_id + 3, f"Backend Engineering::{domain_code}::sen")
    decks_by_level = {"Junior": deck_ju, "Mid": deck_mid, "Senior": deck_sen}

    for card in pure_redis_cards:
        q = (card.get("question") or card.get("Question") or "").strip()
        a = (card.get("answer") or card.get("Answer") or "").strip()
        cat = "IN-MEMORY STORAGE"
        subcat = "REDIS & CACHING"
        lvl = card.get("level") or "Mid"
        if lvl not in decks_by_level:
            lvl = "Mid"
        if not q or not a:
            continue
        note = genanki.Note(model=master_model_v3, fields=[q, a, cat, subcat, lvl, source])
        decks_by_level[lvl].add_note(note)

    apkg_file = os.path.join(final_dir, f"{domain_code}.apkg")
    md_file = os.path.join(final_dir, f"{domain_code}.md")

    # Save APKG
    pkg = genanki.Package([deck_ju, deck_mid, deck_sen])
    pkg.write_to_file(apkg_file)

    # Save Markdown
    md_content = f"# {domain_code} - Redis & In-Memory Caching Study Guide\n\n- **Total Pure Cards**: {len(pure_redis_cards)}\n\n---\n"
    md_content += "\n## 📂 Category: IN-MEMORY STORAGE & REDIS & CACHING\n"
    for lvl in ["Junior", "Mid", "Senior"]:
        lcards = [c for c in pure_redis_cards if c.get("level") == lvl]
        if not lcards:
            continue
        md_content += f"\n### {lvl} Level ({len(lcards)} cards)\n\n"
        for idx, card in enumerate(sorted(lcards, key=lambda c: c.get("question", "")), 1):
            md_content += f"#### {idx}. {card.get('question', '').strip()}\n**Answer:**\n{card.get('answer', '').strip()}\n\n"

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(md_content)

    # Import into Anki Desktop
    req_anki("importPackage", {"path": os.path.abspath(apkg_file)})
    for sub in ["ju", "mid", "sen"]:
        old_name = f"Backend Engineering::{domain_code}::{sub}"
        c_ids = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
        if c_ids:
            req_anki("changeDeck", {"cards": c_ids, "deck": old_name})

    # Update progress checkpoint
    progress[domain_code] = {
        "last_batch_idx": 999,
        "processed_cards": pure_redis_cards
    }
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)

    print(f"\n==========================================")
    print(f"REDIS DECK CLEANED & SYNCED TO ANKI DESKTOP: {len(pure_redis_cards)} PURE CARDS!")
    print(f"==========================================")

if __name__ == "__main__":
    main()
