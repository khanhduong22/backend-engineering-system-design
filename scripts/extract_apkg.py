import os
import sqlite3
import json
import re
import zipfile
import shutil
import glob

def clean_html(text):
    if not text:
        return ""
    # Replace common HTML tags with readable text
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<div>', '\n', text)
    text = re.sub(r'</div>', '', text)
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&amp;', '&')
    text = text.replace('&quot;', '"')
    # Remove any other HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Normalize line breaks
    text = re.sub(r'\n+', '\n', text).strip()
    return text

def format_markdown_table_cell(text):
    # Markdown tables do not support actual newlines in cells, so we replace them with HTML line breaks `<br>`
    cleaned = clean_html(text)
    return cleaned.replace('\n', '<br>')

def get_field_mappings(models_json):
    """
    Analyzes note models to find the indices of Front (Question) and Back (Answer) fields.
    """
    try:
        models = json.loads(models_json)
    except Exception:
        return {}
        
    mappings = {} # mid -> (front_idx, back_idx)
    for mid_str, model in models.items():
        try:
            mid = int(mid_str)
            fields = model.get('flds', [])
            
            # 1. Determine Front/Question field index
            front_idx = 0
            front_keywords = ['front', 'question', 'vorderseite', 'text', 'name', 'header', 'term', 'word']
            found_front = False
            for kw in front_keywords:
                for f in fields:
                    if kw in f.get('name', '').lower():
                        front_idx = f.get('ord', 0)
                        found_front = True
                        break
                if found_front:
                    break
                    
            # 2. Determine Back/Answer field index
            back_idx = 1 if len(fields) > 1 else 0
            back_keywords = ['back', 'answer', 'rückseite', 'definition', 'extra', 'explanation', 'meaning']
            found_back = False
            for kw in back_keywords:
                for f in fields:
                    if kw in f.get('name', '').lower():
                        back_idx = f.get('ord', 0)
                        found_back = True
                        break
                if found_back:
                    break
                    
            # Fallback if front and back mapped to the same index
            if front_idx == back_idx and len(fields) > 1:
                # Assign back_idx to the first index that isn't front_idx
                for f in fields:
                    if f.get('ord', 0) != front_idx:
                        back_idx = f.get('ord', 0)
                        break
                        
            mappings[mid] = (front_idx, back_idx)
        except Exception:
            continue
    return mappings

def process_apkg(apkg_path, output_dir):
    filename = os.path.basename(apkg_path)
    deck_key = os.path.splitext(filename)[0]
    temp_dir = os.path.join(os.path.dirname(apkg_path), f"temp_extract_{deck_key}")
    
    print(f"Processing {filename}...")
    
    # 1. Extract zip
    try:
        os.makedirs(temp_dir, exist_ok=True)
        with zipfile.ZipFile(apkg_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
    except Exception as e:
        print(f"  Error extracting zip: {e}")
        shutil.rmtree(temp_dir, ignore_errors=True)
        return []

    # 2. Find SQLite database (check Anki 2.1 collection.anki21 first)
    db_file = None
    for f in ['collection.anki21', 'collection.anki2']:
        p = os.path.join(temp_dir, f)
        if os.path.exists(p):
            db_file = p
            break
            
    if not db_file:
        print("  Error: SQLite collection database not found in package.")
        shutil.rmtree(temp_dir, ignore_errors=True)
        return []

    # 3. Read SQLite
    cards_list = []
    deck_name = deck_key
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        # Get note models and mappings
        field_mappings = {}
        try:
            cursor.execute('select models from col')
            row = cursor.fetchone()
            if row:
                field_mappings = get_field_mappings(row[0])
                
                # Also try to retrieve deck name
                cursor.execute('select decks from col')
                deck_row = cursor.fetchone()
                if deck_row:
                    decks = json.loads(deck_row[0])
                    deck_names = [d['name'] for d in decks.values() if d.get('name') != 'Default']
                    if deck_names:
                        deck_name = deck_names[0]
        except Exception as e:
            print(f"  Warning retrieving models metadata: {e}")
            
        # Get cards and notes
        cursor.execute('''
            select n.mid, n.flds
            from notes n
            join cards c on c.nid = n.id
            order by n.id
        ''')
        
        for row in cursor.fetchall():
            mid, flds = row
            fields = flds.split('\x1f')
            
            # Map front and back based on note's model ID
            front_idx, back_idx = field_mappings.get(mid, (0, 1 if len(fields) > 1 else 0))
            
            # Protect against index out of range
            front = fields[front_idx] if front_idx < len(fields) else (fields[0] if fields else "")
            back = fields[back_idx] if back_idx < len(fields) else (fields[1] if len(fields) > 1 else (fields[0] if fields else ""))
            
            cards_list.append({
                'deck': deck_name,
                'question': front,
                'answer': back
            })
            
        conn.close()
    except Exception as e:
        print(f"  Error reading database: {e}")
    finally:
        # Clean up temp dir
        shutil.rmtree(temp_dir, ignore_errors=True)

    if not cards_list:
        print("  No cards extracted.")
        return []

    # 4. Write individual MD file
    individual_md = os.path.join(output_dir, f"{deck_key}.md")
    try:
        with open(individual_md, 'w', encoding='utf-8') as f:
            f.write(f"# Deck: {deck_name}\n\n")
            f.write(f"- **Source File**: {filename}\n")
            f.write(f"- **Total Cards**: {len(cards_list)}\n\n")
            f.write("| # | Question / Front | Answer / Back |\n")
            f.write("|---|---|---|\n")
            for idx, card in enumerate(cards_list, 1):
                q = format_markdown_table_cell(card['question'])
                a = format_markdown_table_cell(card['answer'])
                f.write(f"| {idx} | {q} | {a} |\n")
        print(f"  Saved individual deck to {individual_md}")
    except Exception as e:
        print(f"  Error writing individual markdown: {e}")

    return cards_list

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, "output")
    os.makedirs(output_dir, exist_ok=True)

    # Recursively find all *.apkg files under current directory
    pattern = os.path.join(current_dir, "**", "*.apkg")
    all_apkg_paths = glob.glob(pattern, recursive=True)
    
    # Filter out files in output or temp extraction directories
    apkg_files = []
    for path in all_apkg_paths:
        abs_path = os.path.abspath(path)
        # Skip output directory and temp directories
        if "temp_extract_" in abs_path or abs_path.startswith(os.path.abspath(output_dir)):
            continue
        apkg_files.append(abs_path)

    if not apkg_files:
        print("No .apkg files found in the directory or subdirectories.")
        return

    print(f"Found {len(apkg_files)} .apkg file(s) to process.")
    
    all_cards = []
    for apkg in sorted(apkg_files):
        cards = process_apkg(apkg, output_dir)
        all_cards.extend(cards)

    if not all_cards:
        print("No cards were extracted from any packages.")
        return

    # Write consolidated MD file
    consolidated_md = os.path.join(output_dir, "consolidated_deck.md")
    try:
        with open(consolidated_md, 'w', encoding='utf-8') as f:
            f.write("# Consolidated Anki Deck\n\n")
            f.write(f"Consolidation of all questions from {len(apkg_files)} deck(s).\n\n")
            f.write(f"- **Total Consolidated Cards**: {len(all_cards)}\n\n")
            
            # Group by deck name
            decks_dict = {}
            for card in all_cards:
                decks_dict.setdefault(card['deck'], []).append(card)
                
            for deck_name, cards in sorted(decks_dict.items()):
                f.write(f"## Deck: {deck_name} ({len(cards)} cards)\n\n")
                f.write("| # | Question / Front | Answer / Back |\n")
                f.write("|---|---|---|\n")
                for idx, card in enumerate(cards, 1):
                    q = format_markdown_table_cell(card['question'])
                    a = format_markdown_table_cell(card['answer'])
                    f.write(f"| {idx} | {q} | {a} |\n")
                f.write("\n")
                
        print(f"\nSuccessfully created consolidated deck: {consolidated_md}")
    except Exception as e:
        print(f"Error writing consolidated markdown: {e}")

if __name__ == '__main__':
    main()
