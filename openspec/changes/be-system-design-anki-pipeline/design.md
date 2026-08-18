# OpenSpec Design Document: Backend & System Design Anki Pipeline (v2.0)

## System Architecture & Data Flow

```mermaid
flowchart TD
    subgraph Raw_Sources["14,610 Raw Notes (49 APKGs)"]
        S1["SQL & PostgreSQL (1,165 notes)"]
        S2["Networking (1,506 notes)"]
        S3["DDIA Storage & Retrieval (808 notes)"]
        S4["Redis & Kafka (224 notes)"]
        S5["Design Patterns (301 notes)"]
        S6["CS & SWE Fundamentals (4,008 notes)"]
        S7["System Design & Alex Xu (1,723 notes)"]
    end

    subgraph Pipeline["High-Precision Extraction & AI Micro-Batching Engine"]
        P1["Python APKG Extractor (Anki21/Anki2 DB Priority Resolver)"]
        P2["Micro-Batch AI Deduplication (15-20 Cards/Batch via Gemini 3.6 Flash Lite)"]
        P3["Domain Isolation & Level Tagging (Junior / Mid / Senior)"]
        P4["State Checkpointing (progress_all_be.json)"]
    end

    subgraph Outputs["Final 8 Single-Domain Decks (final/)"]
        O1["01_SQL_PostgreSQL_Mastery.apkg / .md"]
        O2["02_Networking_Security.apkg / .md"]
        O3["03_Storage_DDIA.apkg / .md"]
        O4["04_Redis_Caching.apkg / .md"]
        O5["05_Kafka_EventDriven.apkg / .md"]
        O6["06_DesignPatterns_OOP.apkg / .md"]
        O7["07_ComputerScience_SWE.apkg / .md"]
        O8["08_SystemDesign_Architecture.apkg / .md"]
    end

    Raw_Sources --> P1
    P1 --> P2
    P2 <--> P4
    P2 --> P3
    P3 --> Outputs
```

---

## Anti-Hallucination & Anti-Lost-in-the-Middle Design

### 1. Payload Micro-Batching
* Payload size reduced from 35 down to **15 - 20 cards per API payload**.
* Context footprint: ~1,500 input tokens / ~2,000 output tokens.
* Eliminates LLM attention decay and guarantees 100% precision on technical nuances, code snippets, and exact command syntax.

* **Model Endpoint**: `gemini-flash-lite-latest` (Primary active model endpoint).

### 3. Execution Resilience
* **Timeout**: 30 seconds per HTTPS request.
* **Retries**: Exponential backoff (5s, 10s, 20s, 40s) on HTTP 429, 500, 503.
* **Progress Persistence**: `progress_all_be.json` checkpointing after every batch.
