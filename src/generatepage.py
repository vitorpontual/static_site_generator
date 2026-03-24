from inline_markdown import extract_title
from markdown_block import markdown_to_html_node
import os

def generate_page(from_path, dest_path, template_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r', encoding="utf-8") as f:
        md_content = f.read()

    with open(template_path, 'r', encoding="utf-8") as f:
        template_content = f.read()
    
    html_node = markdown_to_html_node(md_content)
    html_content = html_node.to_html()

    title = extract_title(md_content)
    print(title)

    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f'Page generated successfully at {dest_path}')




