# Implementation Tasks: Backend & System Design Anki Pipeline (v2.0)

## Phase 1: Ingestion & Extraction Engine
- [ ] 1.1 Configure `process_all_be_decks.py` to scan `/Users/kido/Documents/anki/input` and `/Users/kido/Downloads`.
- [ ] 1.2 Implement Anki 2.1 (`collection.anki21`) priority extraction with fallback to `collection.anki2`.
- [ ] 1.3 Normalize field mappings across all 49 `.apkg` packages.

## Phase 2: Micro-Batching AI Deduplication Engine
- [ ] 2.1 Integrate `gemini-3.6-flash-lite` API payload micro-batching (15-20 cards/batch).
- [ ] 2.2 Enforce strict technical coverage preservation prompt (preventing aggressive pruning).
- [ ] 2.3 Add retry backoff logic for HTTP 429/500/503 and 30s connection timeout.
- [ ] 2.4 Write persistent checkpointing state (`progress_all_be.json`).

## Phase 3: Final 8 Single-Domain Markdown & APKG Compilation
- [ ] 3.1 Partition deduplicated cards into 8 Single-Domain Phase-Ordered Decks (`01_` to `08_`).
- [ ] 3.2 Preserve existing SQL/Postgres progress in `01_SQL_PostgreSQL_Mastery`.
- [ ] 3.3 Generate formatted Markdown study guides in `final/`.
- [ ] 3.4 Compile styled `.apkg` packages with `genanki` into `final/`.

## Phase 4: Review & Quality Assurance
- [ ] 4.1 Verify card counts, tag assignments, and code block formatting.
- [ ] 4.2 Test import into Anki Desktop / AnkiWeb PWA.
