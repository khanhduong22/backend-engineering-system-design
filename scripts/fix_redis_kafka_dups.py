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

    # 1. PURGE ALL OLD NOTES FOR REDIS & KAFKA IN ANKI DESKTOP
    for code in ["03_Redis_Caching", "04_Kafka_EventDriven"]:
        print(f"Purging all old notes for {code} from Anki Desktop...")
        old_cards = req_anki("findCards", {"query": f'deck:"Backend Engineering::{code}*"'}).get("result", [])
        if old_cards:
            info = req_anki("cardsInfo", {"cards": old_cards}).get("result", [])
            old_note_ids = list(set(c["note"] for c in info if "note" in c))
            if old_note_ids:
                req_anki("deleteNotes", {"notes": old_note_ids})
                print(f"  Deleted {len(old_note_ids)} old notes for {code}.")

    # 2. FILTER & DEDUPLICATE CARDS IN PYTHON
    redis_raw = progress.get("03_Redis_Caching", {}).get("processed_cards", [])
    kafka_raw = progress.get("04_Kafka_EventDriven", {}).get("processed_cards", [])

    # Combine all candidate cards from both decks
    all_candidate_cards = redis_raw + kafka_raw

    redis_clean = []
    kafka_clean = []

    seen_redis_q = set()
    seen_kafka_q = set()

    for c in all_candidate_cards:
        q = (c.get("question") or "").strip()
        a = (c.get("answer") or "").strip()
        if not q or not a:
            continue
        
        q_lower = q.lower()

        is_kafka = any(k in q_lower or k in a.lower() for k in ["kafka", "zookeeper", "kraft", "partition", "consumer group", "producer", "broker", "offset", "topic", "rebalance", "isr", "ack"])
        is_redis = any(k in q_lower or k in a.lower() for k in ["redis", "cache", "caching", "rdb", "aof", "sentinel", "hotkey", "bigkey", "eviction", "memcached", "bloom filter", "pipeline", "skiplist", "ziplist", "sds"])

        if is_redis and not is_kafka:
            if q_lower not in seen_redis_q:
                seen_redis_q.add(q_lower)
                redis_clean.append(c)
        elif is_kafka and not is_redis:
            if q_lower not in seen_kafka_q:
                seen_kafka_q.add(q_lower)
                kafka_clean.append(c)
        else:
            # Dual or general: check primary title
            if "kafka" in q_lower or "zookeeper" in q_lower:
                if q_lower not in seen_kafka_q:
                    seen_kafka_q.add(q_lower)
                    kafka_clean.append(c)
            else:
                if q_lower not in seen_redis_q:
                    seen_redis_q.add(q_lower)
                    redis_clean.append(c)

    print(f"\nFiltered & Cleaned Cards:")
    print(f"  03_Redis_Caching: {len(redis_clean)} unique cards (Zero Kafka overlap, Zero duplicates)")
    print(f"  04_Kafka_EventDriven: {len(kafka_clean)} unique cards (Zero Redis overlap, Zero duplicates)")

    # Update progress checkpoint
    progress["03_Redis_Caching"]["processed_cards"] = redis_clean
    progress["04_Kafka_EventDriven"]["processed_cards"] = kafka_clean
    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)

    # 3. BUILD APKGS & IMPORT TO ANKI DESKTOP
    domains_to_build = [
        {"code": "03_Redis_Caching", "title": "Redis & In-Memory Caching Architecture", "deck_id": 2059400204, "cards": redis_clean},
        {"code": "04_Kafka_EventDriven", "title": "Kafka & Event-Driven Systems", "deck_id": 2059400205, "cards": kafka_clean}
    ]

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

    for domain in domains_to_build:
        code = domain["code"]
        title = domain["title"]
        deck_id = domain["deck_id"]
        cards = domain["cards"]

        md_file = os.path.join(final_dir, f"{code}.md")
        apkg_file = os.path.join(final_dir, f"{code}.apkg")

        # Markdown
        categories = {}
        for card in cards:
            cat = card.get("category", title)
            lvl = card.get("level", "Mid")
            categories.setdefault(cat, {}).setdefault(lvl, []).append(card)

        md_content = f"# {code} - {title} Study Guide\n\n- **Total Cards**: {len(cards)}\n\n---\n"
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

        # APKG
        deck_ju = genanki.Deck(deck_id + 1, f"Backend Engineering::{code}::ju")
        deck_mid = genanki.Deck(deck_id + 2, f"Backend Engineering::{code}::mid")
        deck_sen = genanki.Deck(deck_id + 3, f"Backend Engineering::{code}::sen")
        decks_by_level = {"Junior": deck_ju, "Mid": deck_mid, "Senior": deck_sen}

        for card in cards:
            q = card.get("question", "").strip()
            a = card.get("answer", "").strip()
            cat = card.get("category", title)
            lvl = card.get("level", "Mid")
            if lvl not in decks_by_level:
                lvl = "Mid"
            note = genanki.Note(model=anki_model, fields=[q, a, cat, lvl])
            decks_by_level[lvl].add_note(note)

        pkg = genanki.Package([deck_ju, deck_mid, deck_sen])
        pkg.write_to_file(apkg_file)

        # Import & Organize in Anki Desktop
        req_anki("importPackage", {"path": os.path.abspath(apkg_file)})
        for sub in ["ju", "mid", "sen"]:
            old_name = f"Backend Engineering::{code}::{sub}"
            c_ids = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
            if c_ids:
                req_anki("changeDeck", {"cards": c_ids, "deck": old_name})

        print(f"Successfully re-built & imported clean {code} into Anki Desktop!")

    print("\n==========================================")
    print("REDIS & KAFKA DECKS PURGED & RE-BUILT WITH ZERO DUPLICATES!")
    print("==========================================")

if __name__ == "__main__":
    main()
