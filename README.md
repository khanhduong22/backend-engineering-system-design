# 🚀 Senior Backend Engineering & System Design Mastery

> **Author:** [Duong Phuc Khanh](https://github.com/khanhduong22)  
> **Repository:** 16-Week Senior Backend & System Design Mastery — 10,000+ Anki Active Recall Cards, 8 Core PoC Building Blocks & 8 Showcase API Services.

---

## 📚 1. ANKI DECK COLLECTION OVERVIEW (10,092 CARDS)

This repository contains a curated, 9-domain high-ROI study collection for Senior Backend Engineers and System Architects. All cards use **Backend Master Model v3** with Dual Badges (`Category` + `SubCategory`), Level Badges (`Junior` 🟢, `Mid` 🟡, `Senior` 🔴), and Book Source Footers.

```
Backend Engineering Collection
 ├── 01_DesignPatterns_OOP (61 cards) [GoF + SOLID + OOP + DDD]
 ├── 02_Redis_Caching (112 cards) [Pure Redis & Caching 100%]
 ├── 03_Kafka_EventDriven (140 cards) [Kafka & Event Streaming]
 ├── 04_SQL_PostgreSQL_Mastery (1,172 cards) [PostgreSQL Internals & SQL Tuning]
 ├── 05_Storage_DDIA (745 cards) [Distributed Storage & DDIA]
 ├── 06_SystemDesign_Architecture (651 cards) [Pure System Design & Alex Xu Scenarios]
 ├── 07_Networking_Security (1,382 cards) [Networking & Security Protocols]
 ├── 08_ComputerScience_SWE_optional (5,033 cards) [CS Core - Optional Reference]
 └── 09_WebDev_GeneralCS_optional (788 cards) [General Web & API Params - Optional Reference]
```

Full details and category breakdowns are maintained in [`final/DECK_COLLECTION_SUMMARY.md`](final/DECK_COLLECTION_SUMMARY.md).

---

## 🗺️ 2. 16-WEEK AGILE ROLLING ROADMAP (2-PHASE ARCHITECTURE)

See the full 16-week execution plan in [`SENIOR_ENGINEERING_ROADMAP_16WEEKS.md`](SENIOR_ENGINEERING_ROADMAP_16WEEKS.md).

### 🛠️ Phase 1: 8 Core PoC Building Blocks (Weeks 1 - 8)
1. **PoC 1 (Redis Mutex & Lua Script):** Anti-Over-selling Flash Sale Engine (`DECR` atomic script).
2. **PoC 2 (Idempotency Engine):** Redis `X-Idempotency-Key` Anti-Duplicate Payment/Webhook Middleware.
3. **PoC 3 (Async Queue Buffer):** BullMQ/Kafka Worker + Manual ACK + Dead Letter Queue (DLQ).
4. **PoC 4 (Postgres Query Tuning):** 1M Rows Stress Test + `EXPLAIN (ANALYZE, BUFFERS)` + Index Optimization.
5. **PoC 5 (Rate Limiter Gateway):** Token Bucket / Sliding Window Traffic Throttling Middleware.
6. **PoC 6 (Snowflake Unique ID):** Distributed 64-bit Unique ID Generator.
7. **PoC 7 (Real-time WebSockets):** Socket.io + Redis PubSub + Multi-room State Management.
8. **PoC 8 (Search Engine & BloomFilter):** Meilisearch + Redis BloomFilter + GIN Indexing.

### 🏗️ Phase 2: 8 Showcase API Services (Weeks 9 - 16)
1. **App 1:** Flash Sale & E-Commerce Core API
2. **App 2:** Real-Time Chat & Notification API
3. **App 3:** High-Speed Search & Product Catalog API
4. **App 4:** Payment Gateway & Webhook Aggregator API
5. **App 5:** Short-Link Analytics API (Linkpul-style)
6. **App 6:** Real-Time Fintech & Stock Ticker API (Index-style)
7. **App 7:** Proximity & Driver Dispatch API (Uber-style)
8. **App 8:** Microservices Order Saga & Transactional Outbox System API

---

## ⚙️ 3. REPOSITORY STRUCTURE

```
.
├── .agents/
│   └── AGENTS.md                  # Workspace rules & auto-update directives
├── final/                          # Compiled APKG files, Markdown decks & Summary
│   ├── DECK_COLLECTION_SUMMARY.md
│   ├── 01_DesignPatterns_OOP.apkg
│   └── ...
├── scripts/                        # Automation & data pipeline scripts
│   ├── summarize_all_be_decks.py
│   ├── clean_redis_deck_pure.py
│   └── ...
├── SENIOR_ENGINEERING_ROADMAP_16WEEKS.md
├── README.md
└── .gitignore
```

---

## 📜 LICENSE

MIT License - Feel free to use for personal study and architecture reference.
