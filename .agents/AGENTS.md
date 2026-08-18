# Workspace Rules & AI Agent Directives (AGENTS.md)

## 1. Auto-Update Anki Deck Collection Summary
Whenever any Anki deck, note, or card collection in this workspace is created, modified, re-ordered, cleaned, or deduplicated:
- **Mandatory Action:** ALWAYS run `python3 scripts/summarize_all_be_decks.py` to regenerate `final/DECK_COLLECTION_SUMMARY.md`.
- **User Notification:** Provide a brief summary of the updated deck collection stats to the user after every change.

## 2. High-ROI Backend Engineering Study Order
Always maintain the 9-domain high-ROI study sequence:
1. `01_DesignPatterns_OOP` (GoF + SOLID + OOP + DDD)
2. `02_Redis_Caching` (Pure Redis & Caching)
3. `03_Kafka_EventDriven` (Kafka & Event Streaming)
4. `04_SQL_PostgreSQL_Mastery` (PostgreSQL Internals & SQL)
5. `05_Storage_DDIA` (Distributed Data & DDIA)
6. `06_SystemDesign_Architecture` (Pure System Design & Microservices)
7. `07_Networking_Security` (Networking & Security Protocols)
8. `08_ComputerScience_SWE_optional` (CS Core - Optional Reference)
9. `09_WebDev_GeneralCS_optional` (General Web Dev & API Params - Optional Reference)

## 3. Card UI Master Model v3 Standards
All cards must use `Backend Master Model v3` with:
- Dual Badges (`Category` + `SubCategory`) on top-left.
- Level Badge (`Junior` 🟢, `Mid` 🟡, `Senior` 🔴) on top-right.
- Book Source Citation at bottom footer.
- High-performance zero-lag CSS with lazy JS loading for Mermaid diagrams.
