import re

input_file = "Báo_cáo_python.md"
output_file = "Báo_cáo_python_cleaned.md"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
title_found = False
title_content = []
in_garbage_table = True
student_table_started = False

# Regex to find the title content inside the table row
title_pattern = re.compile(r"\*\*BỘ GIÁO DỤC VÀ ĐÀO TẠO\*\*(.*?)_Thành phố Hồ Chí Minh, tháng 12 năm 2025_", re.DOTALL)

# Regex to clean TOC dots and page numbers
toc_pattern = re.compile(r"(\.{5,})\s*\d+$")

for line in lines:
    # Check for the start of the student table, which marks the end of the garbage table
    if "|MSSV|Họ tên|" in line:
        in_garbage_table = False
        student_table_started = True
    
    if in_garbage_table:
        # Try to extract title info if not found yet
        if not title_found and "**BỘ GIÁO DỤC VÀ ĐÀO TẠO**" in line:
            # The content is likely in one line or split. 
            # Based on the preview, it's in one cell: ||||<br> <br>**BỘ GIÁO DỤC...
            # Let's extract the text between the first ** and the end of the cell/line
            match = re.search(r"(\*\*BỘ GIÁO DỤC VÀ ĐÀO TẠO\*\*.*)", line)
            if match:
                raw_title = match.group(1)
                # Clean up the extracted title
                # Remove table cell markers if any at the end
                raw_title = raw_title.split("|")[0] 
                # Replace <br> with newlines
                formatted_title = raw_title.replace("<br>", "\n\n")
                # Add to new_lines
                new_lines.append(formatted_title + "\n\n---\n\n")
                title_found = True
        continue
    
    # Process the rest of the lines
    if student_table_started:
        # Clean TOC lines
        clean_line = toc_pattern.sub("", line.strip())
        if clean_line:
             new_lines.append(clean_line + "\n")
        else:
            # Keep empty lines for spacing, but limit them
            if new_lines and new_lines[-1].strip() != "":
                new_lines.append("\n")

# Write to output file
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print(f"Cleaned markdown saved to {output_file}")
