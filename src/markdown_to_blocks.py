
def markdown_to_blocks(md):
    raw_blocks = md.split("\n\n")
    filtered_blocks = []

    for block in raw_blocks:
        cleaned_block = block.strip()

        if cleaned_block == "":
            continue
        
        filtered_blocks.append(cleaned_block)

    return filtered_blocks
