from markdown_block import markdown_to_html_node
import os

def generate_page(from_path, dest_path, template_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r', encoding="utf-8") as f:
        md_content = f.read()

    with open(template_path, 'r', encoding="utf-8") as f:
        template = f.read()
    
    html_node = markdown_to_html_node(md_content)
    html_content = html_node.to_html()

    title = extract_title(md_content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath) 

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)

    print(f'Page generated successfully at {dest_path}')

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# ") and not line.startswith("##"):
            return line[2:]
    raise ValueError("no  title found")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            if filename.endswith(".md"):
                dest_path = dest_path[:-3] + ".html"
                generate_page(from_path, dest_path, template_path, basepath)

        else:
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            generate_pages_recursive(from_path, template_path, dest_path,basepath)
