import pymupdf4llm
import os

pdf_path = "Báo cáo python.pdf"
md_path = "Báo_cáo_python.md"

if os.path.exists(pdf_path):
    print(f"Converting {pdf_path} to Markdown...")
    md_text = pymupdf4llm.to_markdown(pdf_path)
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    print(f"Successfully converted to {md_path}")
else:
    print(f"File {pdf_path} not found.")
