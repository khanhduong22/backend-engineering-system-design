import os
import re
import json
import shutil

# 1. Dynamically import or install genanki
try:
    import genanki
except ImportError:
    print("Installing 'genanki' library for Anki packaging...")
    import subprocess
    import sys
    import site
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--break-system-packages", "--user", "genanki"])
        user_site = site.getusersitepackages()
        if user_site not in sys.path:
            sys.path.append(user_site)
        import genanki
        print("genanki successfully installed.")
    except Exception as e:
        print(f"Error installing genanki: {e}")
        print("Please run: pip install genanki")
        sys.exit(1)

def parse_final_markdown(filepath):
    """
    Parses the structured final consolidated markdown file.
    """
    cards = []
    current_category = "General"
    current_level = "Mid"
    current_question = None
    current_answer_lines = []
    in_answer = False
    
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return []
        
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            
            # Match Category
            if line.startswith("## 📂 Category:"):
                # Save previous card first
                if current_question:
                    cards.append({
                        "category": current_category,
                        "level": current_level,
                        "question": current_question,
                        "answer": "\n".join(current_answer_lines).strip()
                    })
                    current_question = None
                    current_answer_lines = []
                    in_answer = False
                
                match = re.search(r'## 📂 Category:\s*(.*?)(?:\s*\(\d+\s*cards\))?$', line)
                if match:
                    current_category = match.group(1).strip()
                    
            # Match Level
            elif line.startswith("### ") and "Level" in line:
                # Save previous card first
                if current_question:
                    cards.append({
                        "category": current_category,
                        "level": current_level,
                        "question": current_question,
                        "answer": "\n".join(current_answer_lines).strip()
                    })
                    current_question = None
                    current_answer_lines = []
                    in_answer = False
                
                if "Junior" in line:
                    current_level = "Junior"
                elif "Mid" in line:
                    current_level = "Mid"
                elif "Senior" in line:
                    current_level = "Senior"
                    
            # Match Question
            elif line.startswith("#### "):
                # Save previous card first
                if current_question:
                    cards.append({
                        "category": current_category,
                        "level": current_level,
                        "question": current_question,
                        "answer": "\n".join(current_answer_lines).strip()
                    })
                    current_question = None
                    current_answer_lines = []
                    in_answer = False
                
                match = re.match(r'####\s*\d+\.\s*(.*)', line)
                if match:
                    current_question = match.group(1).strip()
                    
            # Match Answer Start
            elif stripped == "**Answer:**":
                in_answer = True
                
            # Match Answer Content
            elif in_answer:
                current_answer_lines.append(line)
                
    # Add the last card
    if current_question:
        cards.append({
            "category": current_category,
            "level": current_level,
            "question": current_question,
            "answer": "\n".join(current_answer_lines).strip()
        })
        
    return cards

def markdown_to_html(text):
    """
    Converts markdown formatting to clean HTML suitable for Anki templates.
    """
    if not text:
        return ""
        
    # Helper to convert SQL and generic code blocks to HTML pre/code elements
    def replace_code_block(match):
        code = match.group(1)
        # Escape HTML tags inside code blocks
        code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return f'<pre><code>{code.strip()}</code></pre>'
        
    # Multi-line code blocks
    text = re.sub(r'```(?:\w+)?\n(.*?)\n```', replace_code_block, text, flags=re.DOTALL)
    
    # Inline code: `code`
    text = re.sub(r'`([^`\n]+)`', r'<code>\1</code>', text)
    
    # Bold text: **bold**
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    
    # Split by <pre> and </pre> to add <br> linebreaks ONLY to non-code blocks
    parts = re.split(r'(<pre>.*?</pre>)', text, flags=re.DOTALL)
    for i in range(len(parts)):
        if not parts[i].startswith("<pre>"):
            parts[i] = parts[i].replace('\n', '<br>')
            
    return "".join(parts)

def write_markdown_deck(filepath, level_name, cards):
    """
    Writes a subset of cards to a beautifully formatted markdown file.
    """
    # Group by category
    categories = {}
    for card in cards:
        categories.setdefault(card["category"], []).append(card)
        
    md_content = f"# SQL & Database Study Guide - {level_name} Level\n\n"
    md_content += f"- **Total Cards**: {len(cards)}\n\n"
    md_content += "---\n"
    
    level_emojis = {"Junior": "🟢", "Mid": "🟡", "Senior": "🔴"}
    emoji = level_emojis.get(level_name, "⚪")
    
    for cat_name in sorted(categories.keys()):
        cat_cards = categories[cat_name]
        md_content += f"\n## 📂 Category: {cat_name} ({len(cat_cards)} cards)\n"
        md_content += f"\n### {emoji} {level_name} Level\n\n"
        
        for idx, card in enumerate(sorted(cat_cards, key=lambda c: c["question"]), 1):
            q = card["question"].strip()
            a = card["answer"].strip()
            md_content += f"#### {idx}. {q}\n"
            md_content += f"**Answer:**\n{a}\n\n"
            
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md_content)

def build_apkg(filepath, deck_id, deck_name, cards, anki_model):
    """
    Compiles a list of cards into an Anki Package (.apkg) file.
    """
    anki_deck = genanki.Deck(deck_id, deck_name)
    
    for card in cards:
        q_html = markdown_to_html(card['question'])
        a_html = markdown_to_html(card['answer'])
        
        cleaned_cat = re.sub(r'[^\w\s-]', '', card['category']).strip()
        cleaned_cat = re.sub(r'[\s-]+', '_', cleaned_cat)
        
        tags = [cleaned_cat, card['level']]
        
        note = genanki.Note(
            model=anki_model,
            fields=[q_html, a_html],
            tags=tags
        )
        anki_deck.add_note(note)
        
    genanki.Package(anki_deck).write_to_file(filepath)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "output", "final_consolidated_deck.md")
    final_dir = os.path.join(current_dir, "final")
    
    # Create final output folder
    os.makedirs(final_dir, exist_ok=True)
    
    final_md = os.path.join(final_dir, "final_consolidated_deck.md")
    final_apkg = os.path.join(final_dir, "final_consolidated_deck.apkg")
    
    # 2. Copy the final markdown file to the final/ folder
    print(f"Copying final markdown to {final_md}...")
    try:
        shutil.copy2(input_file, final_md)
    except Exception as e:
        print(f"Error copying markdown file: {e}")
        return

    # 3. Parse cards
    print("Parsing study guide...")
    cards = parse_final_markdown(final_md)
    print(f"Parsed {len(cards)} cards for packaging.")
    
    if not cards:
        print("No cards found to pack.")
        return

    # 4. Define premium Anki CSS & Model
    model_id = 1607392319
    
    anki_model = genanki.Model(
        model_id,
        'SQL Premium Study Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'SQL Card',
                'qfmt': '<div class="card-box question-style">{{Question}}</div>',
                'afmt': '<div class="card-box question-style">{{Question}}</div><hr id="answer"><div class="card-box answer-style">{{Answer}}</div>',
            },
        ],
        css="""
        .card {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 18px;
            color: #1e293b;
            background-color: #f8fafc;
            padding: 20px;
            display: flex;
            justify-content: center;
        }
        .card-box {
            max-width: 700px;
            width: 100%;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            padding: 24px;
            text-align: left;
            line-height: 1.6;
            margin: 10px auto;
        }
        .question-style {
            font-weight: 600;
            border-left: 5px solid #3b82f6;
            color: #1e3a8a;
        }
        .answer-style {
            border-left: 5px solid #10b981;
            color: #0f172a;
        }
        hr#answer {
            border: 0;
            height: 1px;
            background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0));
            margin: 15px 0;
        }
        pre {
            background-color: #f1f5f9;
            border: 1px solid #e2e8f0;
            padding: 14px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: "Fira Code", Monaco, Consolas, "Courier New", monospace;
            font-size: 15px;
            color: #0f172a;
            line-height: 1.4;
        }
        code {
            font-family: "Fira Code", Monaco, Consolas, "Courier New", monospace;
            background-color: #e2e8f0;
            color: #0f172a;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.9em;
        }
        b {
            color: #2563eb;
        }
        """
    )

    # 5. Build Master Deck
    print(f"Packaging and saving Master Deck to {final_apkg}...")
    try:
        build_apkg(final_apkg, 2059400110, 'SQL & Databases (Consolidated)', cards, anki_model)
    except Exception as e:
        print(f"Error packaging master apkg: {e}")

    # 6. Group cards by level
    levels = {"Junior": [], "Mid": [], "Senior": []}
    for card in cards:
        level = card.get("level", "Mid")
        if level in levels:
            levels[level].append(card)
            
    # Deck IDs for levels
    level_deck_ids = {
        "Junior": 2059400111,
        "Mid": 2059400112,
        "Senior": 2059400113
    }

    # 7. Generate level-specific files
    for level, level_cards in levels.items():
        if not level_cards:
            continue
            
        level_lower = level.lower()
        
        # Paths
        lvl_md_path = os.path.join(final_dir, f"{level_lower}_deck.md")
        lvl_apkg_path = os.path.join(final_dir, f"{level_lower}_deck.apkg")
        
        # Write Markdown file
        print(f"Generating {level} Markdown file: {lvl_md_path}...")
        write_markdown_deck(lvl_md_path, level, level_cards)
        
        # Write APKG file
        print(f"Packaging and saving {level} Deck to {lvl_apkg_path}...")
        try:
            build_apkg(lvl_apkg_path, level_deck_ids[level], f"SQL & Databases ({level})", level_cards, anki_model)
        except Exception as e:
            print(f"Error packaging {level} apkg: {e}")

    print("\nSuccessfully compiled all packages!")
    print(f"  Final Output Directory: {final_dir}")

if __name__ == '__main__':
    main()
