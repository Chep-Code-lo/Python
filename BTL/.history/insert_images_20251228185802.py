import re

file_path = "Báo_cáo_python.md"
output_path = "Báo_cáo_python_with_images.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Map Figure numbers to image files
figure_map = {
    "Hình 4": "images/job_distribution.png",
    "Hình 6": "images/salary_by_job.png",
    "Hình 8": "images/experience_distribution.png",
    "Hình 10": "images/salary_by_experience.png",
    "Hình 12": "images/industry_type.png",
    "Hình 14": "images/skills_tools.png",
}

# Map Section headers to image files (for Conclusion)
section_map = {
    "1. Top 3 Vị trí tuyển dụng nhiều nhất": "images/top_3_jobs_count.png",
    "2. Mức lương của Top 3 vị trí": "images/top_3_jobs_salary.png",
    "3. Lương theo cấp độ kinh nghiệm": "images/salary_by_exp_summary.png",
    "4. Top 5 Kỹ năng cần thiết": "images/top_5_skills.png",
    "3.5. Xây dựng mô hình và Chức năng dự đoán": "images/prediction_example.png"
}

# Insert images for Figures
# We look for the pattern "Hình X." in the text (excluding the TOC/List of Figures)
# A simple heuristic: if we find "Hình X." at the start of a line (or after some spaces), 
# we insert the image BEFORE it.
# Note: The List of Figures also has "Hình X.", so we should skip the first occurrence if it's in the TOC.
# But the TOC usually has dots "..."
# Let's try to replace in the body.

lines = content.split("\n")
new_lines = []
toc_passed = False

for line in lines:
    # Check if we passed the TOC/List of Figures
    if "**PHẦN NỘI DUNG**" in line or "CHƯƠNG 1" in line:
        toc_passed = True
        
    inserted = False
    if toc_passed:
        # Check for Figure captions
        for fig_key, img_file in figure_map.items():
            if fig_key in line and "..." not in line:
                # Found a figure caption in the body
                # Insert image before the caption
                new_lines.append(f"![{fig_key}]({img_file})\n")
                new_lines.append(line + "\n")
                inserted = True
                break
        
        # Check for Section headers
        if not inserted:
            for sec_key, img_file in section_map.items():
                if sec_key in line:
                    new_lines.append(line + "\n")
                    new_lines.append(f"\n![{sec_key}]({img_file})\n")
                    inserted = True
                    break
    
    if not inserted:
        new_lines.append(line + "\n")

# Join lines
new_content = "".join(new_lines)

# Special case for feature_importance.png if not used
if "feature_importance.png" not in new_content:
    # Try to find a place for it, maybe "độ quan trọng"
    if "độ quan trọng" in new_content:
        new_content = new_content.replace("độ quan trọng", "độ quan trọng\n\n![Feature Importance](images/feature_importance.png)\n")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Saved to {output_path}")
