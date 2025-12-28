import re

file_path = r"e:\PYTHON\BTL\Báo_cáo_python.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the start and end of the List of Figures section
start_marker = "**DANH MỤC HÌNH ẢNH**"
end_marker = "**DANH MỤC BẢNG**"

# Find the section
start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    section_content = content[start_idx + len(start_marker):end_idx]
    
    # Extract lines starting with "Hình"
    # We want to capture lines like "Hình 1. Code đọc dữ liệu"
    # But avoid lines that are just captions for images if they are duplicates?
    # Actually, in the messy section, we have:
    # ```python ... ```
    # Hình 1. Code đọc dữ liệu
    #
    # We just want to keep the "Hình X..." lines.
    
    clean_lines = []
    for line in section_content.split('\n'):
        line = line.strip()
        if line.startswith("Hình") and not line.startswith("!["):
            # Remove any trailing page numbers or dots if they look messy, 
            # but for now let's just keep the text.
            # Also remove any markdown image syntax if it leaked in.
            if "![" not in line:
                clean_lines.append(line)
    
    # Reconstruct the section
    new_section = "\n\n" + "\n\n".join(clean_lines) + "\n\n"
    
    # Replace the old section
    new_content = content[:start_idx + len(start_marker)] + new_section + content[end_idx:]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print("Successfully cleaned List of Figures.")
else:
    print("Could not find the List of Figures section markers.")
