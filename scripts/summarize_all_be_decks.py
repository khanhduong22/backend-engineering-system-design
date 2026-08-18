import os
import json
import re

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Handle running from scripts/ or root
    if os.path.exists(os.path.join(current_dir, "final")):
        final_dir = os.path.join(current_dir, "final")
    else:
        final_dir = os.path.join(current_dir, "..", "final")

    progress_file = os.path.join(final_dir, "progress_all_be.json")

    with open(progress_file, "r") as f:
        progress = json.load(f)

    summary_md = "# 📚 BACKEND ENGINEERING ANKI COLLECTION SUMMARY REPORT\n\n"
    summary_md += "Report generated directly by inspecting all active decks and cards in your local collection.\n\n"
    summary_md += "---\n\n"

    deck_meta = [
        {"code": "01_DesignPatterns_OOP", "title": "Software Design Patterns & Object-Oriented Design"},
        {"code": "02_Redis_Caching", "title": "Redis & In-Memory Caching Architecture"},
        {"code": "03_Kafka_EventDriven", "title": "Kafka & Event-Driven Systems"},
        {"code": "04_SQL_PostgreSQL_Mastery", "title": "SQL & PostgreSQL Mastery"},
        {"code": "05_Storage_DDIA", "title": "Storage Engines & Distributed Data (DDIA)"},
        {"code": "06_SystemDesign_Architecture", "title": "System Design & Distributed Architecture"},
        {"code": "07_Networking_Security", "title": "Computer Networking & Security Protocols"},
        {"code": "08_ComputerScience_SWE_optional", "title": "CS Fundamentals & Software Engineering (Optional)"},
        {"code": "09_WebDev_GeneralCS_optional", "title": "General Web Dev & API Params (Optional)"}
    ]

    total_all_cards = 0

    for item in deck_meta:
        code = item["code"]
        title = item["title"]
        cards = progress.get(code, {}).get("processed_cards", [])
        total_all_cards += len(cards)

        summary_md += f"## 📂 Deck {code}: {title}\n"
        summary_md += f"- **Total Cards**: `{len(cards)}`\n"

        # Level breakdown
        levels = {"Junior": 0, "Mid": 0, "Senior": 0}
        subcats = {}
        for c in cards:
            lvl = c.get("level", "Mid")
            levels[lvl] = levels.get(lvl, 0) + 1
            subcat = c.get("subcategory") or c.get("category") or "GENERAL"
            subcats[subcat] = subcats.get(subcat, 0) + 1

        summary_md += f"- **Level Breakdown**: 🟢 Junior: `{levels['Junior']}` | 🟡 Mid: `{levels['Mid']}` | 🔴 Senior: `{levels['Senior']}`\n"
        summary_md += "- **SubCategory Breakdown**:\n"
        for sc_name, sc_count in sorted(subcats.items(), key=lambda x: x[1], reverse=True):
            summary_md += f"  - `{sc_name}`: {sc_count} cards\n"

        summary_md += "\n---\n\n"

    summary_md += f"### 🏆 GRAND TOTAL CARDS ACROSS COLLECTION: `{total_all_cards}` CARDS\n"

    summary_file = os.path.join(final_dir, "DECK_COLLECTION_SUMMARY.md")
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(summary_md)

    print(f"Updated DECK_COLLECTION_SUMMARY.md with all {len(deck_meta)} decks! Grand total: {total_all_cards} cards.")

if __name__ == "__main__":
    main()
