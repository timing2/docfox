import os
from pathlib import Path

pages_dir = Path(__file__).resolve().parent / "pages"

def read_md_files_to_dicts(pages_dir):
    md_files_data = []
    for file in os.listdir(pages_dir):
        if file.endswith('.md'):
            parts = file.split('-', 1)
            index = parts[0]
            name = parts[1].rsplit('.', 1)[0]
            with open(os.path.join(pages_dir, file), 'r', encoding='utf-8') as f:
                content = f.read()
            md_files_data.append({"index": index, "name": name, "content": content})
    return md_files_data

md_files_data = read_md_files_to_dicts(pages_dir)

print(md_files_data)

for p in md_files_data:
    print(f"\nIndex: {p['index']}\t Name: {p['name']}")
    print(f"Content:\n{p['content']}")

