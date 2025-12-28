import pymupdf4llm
import os

pdf_path = "Báo cáo python.pdf"
temp_md_path = "temp_check.md"

if os.path.exists(pdf_path):
    print(f"Converting {pdf_path} to Markdown for checking...")
    md_text = pymupdf4llm.to_markdown(pdf_path)
    
    with open(temp_md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    print(f"Converted to {temp_md_path}")
else:
    print(f"File {pdf_path} not found.")
