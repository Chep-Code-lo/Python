import pymupdf4llm
import os

pdf_path = "Báo cáo python.pdf"
md_path = "Báo_cáo_python.md"
image_path = "images"

if not os.path.exists(image_path):
    os.makedirs(image_path)

if os.path.exists(pdf_path):
    print(f"Converting {pdf_path} to Markdown with images...")
    # pymupdf4llm.to_markdown supports write_images=True to extract images
    md_text = pymupdf4llm.to_markdown(pdf_path, write_images=True, image_path=image_path, image_format="png")
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    print(f"Successfully converted to {md_path} with images in {image_path}/")
else:
    print(f"File {pdf_path} not found.")
