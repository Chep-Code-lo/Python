import json
import os
import glob

# 1. Process the Notebook
notebook_path = r"e:\PYTHON\BTL\AI_Job_Market_Analysis.ipynb"
if os.path.exists(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    changed = False
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            new_source = []
            for line in cell['source']:
                if 'plt.savefig' not in line and 'savefig' not in line:
                    new_source.append(line)
                else:
                    changed = True
            cell['source'] = new_source

    if changed:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"Updated {notebook_path}")
    else:
        print(f"No changes in {notebook_path}")

# 2. Process the Markdown file
md_path = r"e:\PYTHON\BTL\BAO_CAO_DU_AN.md"
if os.path.exists(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    changed = False
    for line in lines:
        if 'plt.savefig' not in line and 'savefig' not in line:
            new_lines.append(line)
        else:
            changed = True
            
    if changed:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated {md_path}")
    else:
        print(f"No changes in {md_path}")

# 3. Delete PNG files
images_dir = r"e:\PYTHON\BTL\images"
png_files = glob.glob(os.path.join(images_dir, "*.png"))
for png in png_files:
    try:
        os.remove(png)
        print(f"Deleted {png}")
    except Exception as e:
        print(f"Error deleting {png}: {e}")
