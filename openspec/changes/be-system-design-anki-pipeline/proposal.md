# OpenSpec Proposal: Backend & System Design Anki Pipeline (v2.0)

## Executive Summary

This updated proposal defines the refined domain deck architecture, 3-phase learning roadmap, and precise AI deduplication pipeline for processing 14,610 raw Anki notes across 49 `.apkg` packages.

Prioritizing **Maximum Knowledge Retention** over aggressive pruning, the pipeline targets **~5,000 to 6,000 high-yield cards** across **8 single-domain decks** ordered sequentially by learning phase over a **5 to 6 month timeline**.

---

## Technical Options Comparison

| Option | Pros | Cons | Performance & Complexity | Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| **Option A: 6 Mixed Decks** | Combines related subjects into fewer files. | Blurs domain boundaries (e.g. Design Patterns mixed with CS fundamentals); harder to focus. | Moderate complexity. | Superseded |
| **Option B: 8 Single-Domain Phase-Ordered Decks** | **100% single-domain focus**; zero domain mixing; aligned chronologically with learning phases (`01_` to `08_`); preserves high coverage (~5,000 cards). | Requires 8 output files. | Optimal readability & learning retention. | **RECOMMENDED (Selected)** |

---

## Capability Requirements (Gherkin Syntax)

### Requirement 1: Micro-Batching for High-Precision Processing
```gherkin
GIVEN a set of extracted flashcard notes
WHEN the AI deduplication pipeline processes batches
THEN it MUST use small payloads of 15 to 20 cards per request using gemini-3.6-flash-lite
AND it MUST NOT drop technical edge cases or obscure code snippets
AND minor duplicate variants MAY be preserved for memory reinforcement.
```

### Requirement 2: Phase-Ordered Domain Naming
```gherkin
GIVEN the 8 single-domain deck definitions
WHEN output files are generated in final/
THEN they MUST use numeric phase prefixes ('01_', '02_', ..., '08_') matching the learning roadmap.
```

---

## 8 Single-Domain Decks & Phase Naming

### Giai đoạn 1: Nền tảng (Foundations)
1. **`01_SQL_PostgreSQL_Mastery.apkg`** (~1,165 cards — Compatible with the 4 decks currently being studied in `final/`).
2. **`02_Networking_Security.apkg`** (~1,000 cards — Computer Networking Top-Down, TCP/IP, HTTP/2/3, TLS, Auth).

### Giai đoạn 2: Infra & Datastores (Storage & Messaging)
3. **`03_Storage_DDIA.apkg`** (~650 cards — DDIA, B-Tree vs LSM, Replication, Partitioning, Consensus Raft/Paxos).
4. **`04_Redis_Caching.apkg`** (~200 cards — Redis In-Memory Data Structures, Eviction Policies, Cache Patterns).
5. **`05_Kafka_EventDriven.apkg`** (~200 cards — Kafka Architecture, Partitioning, Consumer Groups, DLQ, CDC).

### Giai đoạn 3: Architecture & Software Engineering
6. **`06_DesignPatterns_OOP.apkg`** (~300 cards — GoF Design Patterns, SOLID Principles, Refactoring).
7. **`07_ComputerScience_SWE.apkg`** (~1,500 cards — CS Fundamentals, Data Structures & Algorithms, OS, Git, Shell).
8. **`08_SystemDesign_Architecture.apkg`** (~1,200 cards — Alex Xu System Design, System Design Primer, Microservices).

Total Target Capacity: **~5,000 to 6,000 High-Yield Cards** (Preserving ~35-40% of rich raw content).
