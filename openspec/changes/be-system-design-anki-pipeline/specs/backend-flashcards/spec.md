# Capability Specification: Backend & System Design Flashcard Mastery (v2.0)

## ADDED CAPABILITY: Automated Single-Domain Backend Flashcard Ingestion

### Scenario 1: Micro-batching ingestion and domain separation
```gherkin
GIVEN a set of 49 raw .apkg files containing 14,610 notes
WHEN the master pipeline process_all_be_decks.py is executed
THEN it MUST parse all notes from collection.anki21 and collection.anki2
AND it MUST process cards in micro-batches of 15 to 20 cards using gemini-3.6-flash-lite
AND it MUST preserve technical edge cases, aiming for ~5,000 to 6,000 high-yield cards
AND it MUST organize output into 8 single-domain decks in final/ named with phase prefixes '01_' to '08_'.
```

### Scenario 2: Extended learning pacing over 5 to 6 months
```gherkin
GIVEN a user committing to 30 new cards/day and 90 to 120 reviews/day
WHEN studying the 8 single-domain decks sequentially across 3 phases
THEN the entire ~5,000-card repository MUST be fully mastered in 5 to 6 months (150 to 180 days)
AND daily study time MUST remain within 20 to 30 minutes per day.
```
