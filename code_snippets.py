import re
import flet as ft

""" Parse markdown and get codeblocks """
def extract_text_and_code_blocks(input_text):
    # Regular expression to match code blocks
    code_block_pattern = r"```(?:[\w+#]+)?\n([\s\S]*?)\n```"
    # Find all code blocks
    code_blocks = re.findall(code_block_pattern, input_text)

    # Replace code blocks with a placeholder to split the text
    placeholder = "{code_block}"
    text_with_placeholders = re.sub(code_block_pattern, placeholder, input_text)

    # Split the text on the placeholder
    text_parts = text_with_placeholders.split(placeholder)

    # Merge text and code blocks into tuples
    text_list = []
    for text, code in zip(text_parts, code_blocks + [""]): # Add empty string to handle the last text part
        text = text.strip()
        code = code.strip()
        if text:
            text_list.append((text, "text"))
        if code:
            text_list.append((code, "code"))

    return text_list

# Example usage of the function
text_list = extract_text_and_code_blocks(markdown_text)

for index, text in enumerate(text_list):
    #parse single `
    modified_text = re.sub(r'(?<!`)\`(?!`)', '***', text[0])
    print(f"Index: {index}\tType: {text[1]}\n{modified_text}\n")


""" Other snippets """

# code_textfield
ft.TextField(
    read_only=True,
    bgcolor="#161B22",
    color="white",
    content_padding=20,
    multiline=True,
    disabled=False,
    value="""import flet as ft
from pathlib import Path

root_path = Path(__file__).resolve().parent
content_path = root_path / 'content'
md1_file = content_path / 'Doc' / 'Markdown example.md' """,
        )





    #routing
    """ def route_change(e: ft.RouteChangeEvent): 
        page.add(ft.Text(f"New route: {e.route}"))

    def go_store(e):
        page.route = "/store"
        page.update()

    page.on_route_change = route_change
    page.add(ft.ElevatedButton("Go to Store", on_click=go_store))
    page.route = "/docs" 
    print(page.route) """