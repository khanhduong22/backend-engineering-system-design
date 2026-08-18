import os
import re
import json
import urllib.request
import urllib.error
import time

def parse_consolidated_deck(filepath):
    cards = []
    current_deck = "Unknown"
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return []
        
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("## Deck:"):
                # Extract deck name, e.g. "## Deck: SQL (54 cards)"
                match = re.search(r'## Deck:\s*(.*?)\s*\(\d+\s*cards\)', line)
                if match:
                    current_deck = match.group(1)
            elif line.startswith("|") and not line.startswith("|---"):
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 4:
                    idx = parts[1]
                    if idx.isdigit(): # Skip header row
                        question = parts[2].replace("<br>", "\n")
                        answer = parts[3].replace("<br>", "\n")
                        cards.append({
                            "original_deck": current_deck,
                            "question": question,
                            "answer": answer
                        })
    return cards

def call_gemini_api(api_key, cards_batch, batch_num, total_batches):
    # Recommended model in skill: gemini-3.1-flash-lite-preview
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent?key=" + api_key
    
    prompt = """You are a professional database administrator and educator. Your task is to clean, deduplicate, categorize, and classify the difficulty of a list of SQL/Database flashcards.

INPUT FORMAT:
You will receive a JSON list of flashcards. Each card has a temporary 'id', 'question', and 'answer'.

TASKS:
1. Deduplicate: Identify cards with the same semantic meaning or very similar questions. Merge them into a single card.
   - Keep the most clear and descriptive question.
   - Combine details from both answers if they complement each other to create a thorough, high-quality answer.
2. Categorize: Assign each card to exactly one of the following categories:
   - 'Basic SQL & Syntax'
   - 'Joins & Set Operators'
   - 'Subqueries & Aggregations'
   - 'Database Design & Normalization'
   - 'Transactions & Concurrency'
   - 'Database Programmability' (Triggers, Views, Functions, Procedures)
   - 'Performance & Indexing'
   - 'Advanced & Distributed Databases'
3. Level Classification: Classify the card into one of these levels:
   - 'Junior': Fundamental syntax, basic queries, simple joins, basic keys.
   - 'Mid': Grouping, aggregation, subqueries, indexing concepts, constraints.
   - 'Senior': Triggers, transaction isolation levels, serializability, query plan optimization, recursive CTEs, locking, distributed architectures.

OUTPUT FORMAT:
You MUST return a JSON object containing a list of cards under the 'cards' key. Every card in the output must have:
- 'question'
- 'answer'
- 'category' (one of the 8 categories above)
- 'level' (Junior, Mid, or Senior)

JSON schema to match:
{
  "cards": [
    {
      "question": "string",
      "answer": "string",
      "category": "string",
      "level": "string"
    }
  ]
}

Here is the list of cards to process:
""" + json.dumps(cards_batch, indent=2)

    req_data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "responseMimeType": "application/json"
        }
    }
    
    data_bytes = json.dumps(req_data).encode("utf-8")
    
    headers = {
        "Content-Type": "application/json"
    }
    
    req = urllib.request.Request(url, data=data_bytes, headers=headers, method="POST")
    
    # Exponential backoff retry logic
    max_retries = 5
    retry_delay = 5
    
    for attempt in range(max_retries):
        try:
            print(f"Sending batch {batch_num}/{total_batches} (Attempt {attempt + 1})...")
            with urllib.request.urlopen(req, timeout=30) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                
                # Extract response text
                candidates = res_data.get("candidates", [])
                if not candidates:
                    raise ValueError("No candidates returned from API.")
                
                content_text = candidates[0]["content"]["parts"][0]["text"]
                result = json.loads(content_text)
                return result.get("cards", [])
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8")
            print(f"  HTTP Error {e.code}: {e.reason}")
            # Retry on rate limit (429) or server errors (500, 503)
            if e.code in [429, 500, 503]:
                print(f"  Transient error. Sleeping for {retry_delay} seconds before retry...")
                time.sleep(retry_delay)
                retry_delay *= 2
            else:
                print(f"  Unrecoverable API error: {body}")
                raise e
        except Exception as e:
            print(f"  Connection error: {e}")
            print(f"  Sleeping for {retry_delay} seconds before retry...")
            time.sleep(retry_delay)
            retry_delay *= 2
            
    raise RuntimeError("Failed to complete request after maximum retries.")

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "output", "consolidated_deck.md")
    output_file = os.path.join(current_dir, "output", "final_consolidated_deck.md")
    progress_file = os.path.join(current_dir, "output", "progress_consolidated.json")
    
    # 1. Parse API key
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key and os.path.exists(os.path.join(current_dir, ".env")):
        with open(os.path.join(current_dir, ".env"), "r") as env_f:
            for line in env_f:
                if line.startswith("GEMINI_API_KEY="):
                    api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
                    break
                    
    if not api_key:
        print("Error: GEMINI_API_KEY is not set in environment or .env file.")
        print("Please set it in a .env file: GEMINI_API_KEY=your_api_key_here")
        return

    # 2. Parse existing consolidated deck
    print("Parsing consolidated_deck.md...")
    cards = parse_consolidated_deck(input_file)
    print(f"Loaded {len(cards)} total cards.")
    
    if not cards:
        return

    # 3. Sort alphabetically by question to place similar cards adjacent to each other
    cards.sort(key=lambda c: c["question"].lower())
    
    # 4. Batch cards (35 per batch to optimize tokens & quality)
    batch_size = 35
    batches = [cards[i:i + batch_size] for i in range(0, len(cards), batch_size)]
    total_batches = len(batches)
    
    processed_cards = []
    start_batch_idx = 1
    
    # Load existing progress if available
    if os.path.exists(progress_file):
        try:
            with open(progress_file, "r", encoding="utf-8") as pf:
                progress_data = json.load(pf)
                processed_cards = progress_data.get("processed_cards", [])
                start_batch_idx = progress_data.get("last_processed_batch_index", 0) + 1
                print(f"Loaded existing progress from {progress_file}. Resuming from batch {start_batch_idx}/{total_batches}...")
        except Exception as e:
            print(f"Warning: could not load progress file: {e}. Starting from scratch.")
            processed_cards = []
            start_batch_idx = 1
            
    completed_all = True
    for i, batch in enumerate(batches, 1):
        if i < start_batch_idx:
            continue
            
        # Format batch for prompt
        batch_input = []
        for idx, card in enumerate(batch, 1):
            batch_input.append({
                "id": idx,
                "question": card["question"],
                "answer": card["answer"]
            })
            
        try:
            results = call_gemini_api(api_key, batch_input, i, total_batches)
            print(f"  Successfully processed batch {i}. Extracted {len(results)} merged cards.")
            processed_cards.extend(results)
            
            # Save progress checkpoint
            try:
                with open(progress_file, "w", encoding="utf-8") as pf:
                    json.dump({
                        "last_processed_batch_index": i,
                        "processed_cards": processed_cards
                    }, pf, indent=2)
            except Exception as e:
                print(f"  Warning: could not save progress checkpoint: {e}")
                
        except Exception as e:
            print(f"  Error in batch {i}: {e}")
            print(f"  Stopping process at batch {i}. Checkpoint saved.")
            completed_all = False
            break
            
        # Rate limit cooldown (RPM is 15 on free tier, wait 5 seconds between calls)
        time.sleep(5)

    if not completed_all:
        print(f"\nExecution paused due to error. Resumable checkpoint saved at: {progress_file}")
        print("Please rerun the script to resume.")
        return

    if not processed_cards:
        print("No cards were processed.")
        return

    # 5. Format final output
    print(f"Deduplicated and structured cards down to {len(processed_cards)} total items.")
    
    # Group by category, then by level
    categories = {}
    for card in processed_cards:
        cat = card.get("category", "General SQL & Databases")
        level = card.get("level", "Mid")
        categories.setdefault(cat, {}).setdefault(level, []).append(card)

    md_content = """# Final Consolidated SQL & Database Knowledge Base

A professionally structured study guide compiled from multiple Anki decks, deduplicated semantically, categorized, and graded by difficulty.

## Deck Metrics
- **Original Deck Cards**: """ + str(len(cards)) + """
- **Final Deduplicated Cards**: """ + str(len(processed_cards)) + """

---
"""
    # Order levels
    level_order = ["Junior", "Mid", "Senior"]
    level_emojis = {"Junior": "🟢", "Mid": "🟡", "Senior": "🔴"}
    
    for cat_name in sorted(categories.keys()):
        cat_data = categories[cat_name]
        total_cat_cards = sum(len(lvl_cards) for lvl_cards in cat_data.values())
        
        md_content += f"\n## 📂 Category: {cat_name} ({total_cat_cards} cards)\n"
        
        for level in level_order:
            lvl_cards = cat_data.get(level, [])
            if not lvl_cards:
                continue
                
            md_content += f"\n### {level_emojis[level]} {level} Level\n\n"
            for idx, card in enumerate(sorted(lvl_cards, key=lambda c: c["question"]), 1):
                q = card["question"].strip()
                a = card["answer"].strip()
                md_content += f"#### {idx}. {q}\n"
                md_content += f"**Answer:**\n{a}\n\n"
                
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(md_content)
        
    print(f"\nFinal study guide successfully generated: {output_file}")
    
    # Clean up progress checkpoint file
    if os.path.exists(progress_file):
        try:
            os.remove(progress_file)
            print("Cleaned up progress checkpoint file.")
        except Exception as e:
            print(f"Warning: could not delete progress file: {e}")

if __name__ == '__main__':
    main()
