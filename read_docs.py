import os
from pathlib import Path

pages_dir = Path(__file__).resolve().parent / "documentation"

def read_md_files_with_subdirs(pages_dir):
    md_files_data = []
    # Check both the directory itself and its immediate subdirectories
    for root, dirs, files in os.walk(pages_dir):
        # Limit to only one level of subdirectories
        depth = os.path.relpath(root, pages_dir).count(os.sep)
        if depth == 0:
            parent = None  # This is the root directory
        elif depth == 1:
            parent = os.path.basename(root)  # Name of the subdirectory

        if depth > 1:
            continue  # Skip deeper subdirectories

        for file in files:
            if file.endswith('.md'):
                parts = file.split('-', 1)
                index = parts[0]
                name = parts[1].rsplit('.', 1)[0]
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                file_data = {"index": index, "name": name, "content": content}
                if parent:
                    file_data["parent"] = parent
                md_files_data.append(file_data)

    return md_files_data

md_files_data = read_md_files_with_subdirs(pages_dir)

for p in md_files_data:
    parent_info = f"Parent: {p['parent']}\t" if "parent" in p else ""
    print(f"\n{parent_info}Index: {p['index']}\t Name: {p['name']}")
    print(f"Content:\n{p['content']}")
