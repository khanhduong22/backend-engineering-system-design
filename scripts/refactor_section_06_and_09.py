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

    # Raw cards in Section 06
    code_06 = "06_SystemDesign_Architecture"
    raw_06_cards = progress.get(code_06, {}).get("processed_cards", [])

    if not raw_06_cards:
        md_file = os.path.join(final_dir, "05_SystemDesign_Architecture.md")
        if not os.path.exists(md_file):
            md_file = os.path.join(final_dir, "06_SystemDesign_Architecture.md")
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
                    raw_06_cards.append({"question": q, "answer": a, "category": "ARCHITECTURE", "level": "Mid"})

    print(f"Loaded {len(raw_06_cards)} total raw cards from Section 06.")

    system_design_keywords = [
        'design a', 'how to design', 'rate limiter', 'url shortener', 'chat system',
        'notification system', 'news feed', 'web crawler', 'youtube', 'drive', 'payment',
        'leaderboard', 'microservice', 'saga', 'circuit breaker', 'service discovery',
        'api gateway', 'event sourcing', 'cqrs', 'outbox', 'distributed transaction', '2pc',
        'idempotency', 'nginx', 'tomcat', 'load balance', 'reverse proxy', 'haproxy', 'cdn',
        'consistent hashing', 'sharding', 'partitioning', 'replication', 'prometheus',
        'grafana', 'tracing', 'opentelemetry', 'log', 'metrics', 'apm', 'signoz', 'health check',
        'slo', 'sli', 'sla', 'bulkhead', 'token bucket', 'leaky bucket', 'sliding window'
    ]

    pure_06_cards = []
    optional_09_cards = []

    for card in raw_06_cards:
        q = (card.get("question") or card.get("Question") or "").strip()
        a = (card.get("answer") or card.get("Answer") or "").strip()
        text = (q + " " + a).lower()

        is_sys_design = any(k in text for k in system_design_keywords)
        if is_sys_design:
            # Determine subcategory
            subcat = "SYSTEM DESIGN ARCHITECTURE"
            if any(k in text for k in ['design a', 'how to design', 'rate limiter', 'url shortener', 'chat system', 'notification', 'news feed', 'web crawler', 'youtube', 'payment', 'leaderboard']):
                subcat = "SYSTEM DESIGN INTERVIEWS (ALEX XU)"
            elif any(k in text for k in ['microservice', 'saga', 'circuit breaker', 'service discovery', 'api gateway', 'event sourcing', 'cqrs', 'outbox']):
                subcat = "MICROSERVICES ARCHITECTURE"
            elif any(k in text for k in ['load balance', 'reverse proxy', 'nginx', 'tomcat', 'haproxy', 'cdn', 'consistent hashing']):
                subcat = "LOAD BALANCING & GATEWAYS"
            elif any(k in text for k in ['prometheus', 'grafana', 'tracing', 'opentelemetry', 'log', 'metrics', 'signoz', 'slo', 'sla']):
                subcat = "OBSERVABILITY & MONITORING"
            elif any(k in text for k in ['bulkhead', 'token bucket', 'leaky bucket', 'sliding window', 'rate limit', 'fault tolerance', 'idempotency']):
                subcat = "RESILIENCE & FAULT TOLERANCE"

            card["category"] = "ARCHITECTURE"
            card["subcategory"] = subcat
            pure_06_cards.append(card)
        else:
            card["category"] = "WEB DEV & CS"
            card["subcategory"] = "GENERAL WEB & API DEVELOPMENT"
            optional_09_cards.append(card)

    print(f"\nExtracted {len(pure_06_cards)} Pure System Design Master Cards for Section 06.")
    print(f"Moved {len(optional_09_cards)} General Web Dev cards to Section 09 (Optional Reference).")

    # Master Model v3
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

    # 1. Purge old notes for 06 from Anki Desktop
    print("Purging old 06 notes from Anki Desktop...")
    old_06_cards = req_anki("findCards", {"query": f'deck:"Backend Engineering::{code_06}*"'}).get("result", [])
    if old_06_cards:
        info = req_anki("cardsInfo", {"cards": old_06_cards}).get("result", [])
        old_note_ids = list(set(c["note"] for c in info if "note" in c))
        if old_note_ids:
            req_anki("deleteNotes", {"notes": old_note_ids})

    # Build Section 06 APKG
    deck_id_06 = 2059400206
    source_06 = "Alex Xu System Design Interview Vol 1 & 2"
    deck_ju_06 = genanki.Deck(deck_id_06 + 1, f"Backend Engineering::{code_06}::ju")
    deck_mid_06 = genanki.Deck(deck_id_06 + 2, f"Backend Engineering::{code_06}::mid")
    deck_sen_06 = genanki.Deck(deck_id_06 + 3, f"Backend Engineering::{code_06}::sen")
    decks_06 = {"Junior": deck_ju_06, "Mid": deck_mid_06, "Senior": deck_sen_06}

    for card in pure_06_cards:
        q = (card.get("question") or "").strip()
        a = (card.get("answer") or "").strip()
        cat = card.get("category") or "ARCHITECTURE"
        subcat = card.get("subcategory") or "SYSTEM DESIGN"
        lvl = card.get("level") or "Mid"
        if lvl not in decks_06:
            lvl = "Mid"
        if not q or not a:
            continue
        note = genanki.Note(model=master_model_v3, fields=[q, a, cat, subcat, lvl, source_06])
        decks_06[lvl].add_note(note)

    apkg_06 = os.path.join(final_dir, f"{code_06}.apkg")
    pkg_06 = genanki.Package([deck_ju_06, deck_mid_06, deck_sen_06])
    pkg_06.write_to_file(apkg_06)

    # Build Section 09 APKG
    code_09 = "09_WebDev_GeneralCS_optional"
    deck_id_09 = 2059400209
    source_09 = "General Web Development & CS Fundamentals (Optional Reference)"
    deck_ju_09 = genanki.Deck(deck_id_09 + 1, f"Backend Engineering::{code_09}::ju")
    deck_mid_09 = genanki.Deck(deck_id_09 + 2, f"Backend Engineering::{code_09}::mid")
    deck_sen_09 = genanki.Deck(deck_id_09 + 3, f"Backend Engineering::{code_09}::sen")
    decks_09 = {"Junior": deck_ju_09, "Mid": deck_mid_09, "Senior": deck_sen_09}

    for card in optional_09_cards:
        q = (card.get("question") or "").strip()
        a = (card.get("answer") or "").strip()
        cat = "WEB DEV & CS"
        subcat = "GENERAL WEB & API DEVELOPMENT"
        lvl = card.get("level") or "Mid"
        if lvl not in decks_09:
            lvl = "Mid"
        if not q or not a:
            continue
        note = genanki.Note(model=master_model_v3, fields=[q, a, cat, subcat, lvl, source_09])
        decks_09[lvl].add_note(note)

    apkg_09 = os.path.join(final_dir, f"{code_09}.apkg")
    pkg_09 = genanki.Package([deck_ju_09, deck_mid_09, deck_sen_09])
    pkg_09.write_to_file(apkg_09)

    # Import both into Anki Desktop
    req_anki("importPackage", {"path": os.path.abspath(apkg_06)})
    for sub in ["ju", "mid", "sen"]:
        old_name = f"Backend Engineering::{code_06}::{sub}"
        c_ids = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
        if c_ids:
            req_anki("changeDeck", {"cards": c_ids, "deck": old_name})

    req_anki("importPackage", {"path": os.path.abspath(apkg_09)})
    for sub in ["ju", "mid", "sen"]:
        old_name = f"Backend Engineering::{code_09}::{sub}"
        c_ids = req_anki("findCards", {"query": f'deck:"{old_name}"'}).get("result", [])
        if c_ids:
            req_anki("changeDeck", {"cards": c_ids, "deck": old_name})

    # Update progress checkpoint
    progress[code_06] = {
        "last_batch_idx": 999,
        "processed_cards": pure_06_cards
    }
    progress[code_09] = {
        "last_batch_idx": 999,
        "processed_cards": optional_09_cards
    }

    with open(progress_file, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2)

    print("\n==========================================")
    print("SECTION 06 SUCCESSFULLY REFACTORED (PURE SYSTEM DESIGN) & SECTION 09 CREATED!")
    print("==========================================")

if __name__ == "__main__":
    main()
