import re

file_path = "Báo_cáo_python.md"
output_path = "Báo_cáo_python.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define code snippets to insert
code_snippets = {
    "Hình 1. Code đọc dữ liệu": """```python
import pandas as pd
df = pd.read_csv('data/ai_job_market.csv')
df[['min_sal', 'max_sal']] = df['salary_range_usd'].str.split('-', expand=True).astype(float)
df['salary'] = (df['min_sal'] + df['max_sal']) / 2
df['posted_date'] = pd.to_datetime(df['posted_date'])
print(f"Loaded {len(df)} jobs | Salary range: ${df['salary'].min():,.0f} - ${df['salary'].max():,.0f}")
```""",
    "Hình 2. Code làm sạch dữ liệu": """```python
# (Code xử lý dữ liệu đã được thực hiện ở bước đọc dữ liệu)
df[['min_sal', 'max_sal']] = df['salary_range_usd'].str.split('-', expand=True).astype(float)
df['salary'] = (df['min_sal'] + df['max_sal']) / 2
df['posted_date'] = pd.to_datetime(df['posted_date'])
```""",
    "Hình 3. Code tạo biểu đồ phân bố số lượng việc làm theo chức danh": """```python
plt.figure(figsize=(10, 6))
df['job_title'].value_counts().head(8).plot(kind='barh', color='steelblue')
plt.title('Top Vị Trí Công Việc', fontweight='bold')
plt.ylabel('')
plt.tight_layout()
plt.show()
```""",
    "Hình 5. Code biểu đồ mức lương trung bình giữa các vị trí phổ biến": """```python
plt.figure(figsize=(10, 6))
df.groupby('job_title')['salary'].mean().sort_values().tail(8).plot(kind='barh', color='coral')
plt.title('Lương TB Theo Vị Trí', fontweight='bold')
plt.ylabel('')
plt.tight_layout()
plt.show()
```""",
    "Hình 7. Code biểu đồ phân bố kinh nghiệm": """```python
plt.figure(figsize=(8, 8))
df['experience_level'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Phân Bố Kinh Nghiệm', fontweight='bold')
plt.ylabel('')
plt.tight_layout()
plt.show()
```""",
    "Hình 9. Mã nguồn biểu đồ mức lương theo kinh nghiệm": """```python
plt.figure(figsize=(8, 6))
df.groupby('experience_level')['salary'].mean().sort_values().plot(kind='bar', color='mediumseagreen')
plt.title('Lương TB Theo Kinh Nghiệm', fontweight='bold')
plt.xlabel('')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
```""",
    "Hình 11. Mã nguồn Biểu đồ cột": """```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ind_data = df.groupby('industry')['salary'].agg(['count', 'mean']).sort_values('count', ascending=False)
axes[0].bar(ind_data.index, ind_data['count'], color='mediumpurple')
axes[0].set_title('Số Việc Làm Theo Ngành', fontweight='bold')

emp_data = df.groupby('employment_type')['salary'].agg(['count', 'mean']).sort_values('mean', ascending=False)
axes[1].barh(emp_data.index, emp_data['mean'], color='teal')
axes[1].set_title('Lương TB Theo Loại Việc', fontweight='bold')

plt.tight_layout()
plt.show()
```""",
    "Hình 13. Mã nguồn biểu đồ thanh ngang": """```python
all_skills = [s.strip() for skills in df['skills_required'].dropna() for s in skills.split(',')]
all_tools = [t.strip() for tools in df['tools_preferred'].dropna() for t in tools.split(',')]

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

top_skills = pd.Series(Counter(all_skills)).sort_values(ascending=True).tail(12)
top_skills.plot(kind='barh', ax=axes[0], color='steelblue')

top_tools = pd.Series(Counter(all_tools)).sort_values(ascending=True).tail(10)
top_tools.plot(kind='barh', ax=axes[1], color='darkorange')

plt.tight_layout()
plt.show()
```""",
    "Hình 15. Mã nguồn biểu đồ nhiệt": """```python
top_jobs = df['job_title'].value_counts().head(6).index
pivot = df[df['job_title'].isin(top_jobs)].pivot_table(
    values='salary', index='job_title', columns='experience_level', aggfunc='mean'
)

plt.figure(figsize=(10, 5))
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='YlGnBu', cbar_kws={'label': 'Salary (USD)'})
plt.title('Lương Theo Vị Trí & Kinh Nghiệm', fontweight='bold')
plt.tight_layout()
plt.show()
```""",
    "Hình 17. Mã nguồn Label Encoding": """```python
features = ['job_title', 'experience_level', 'employment_type', 'industry', 'company_size']
encoders = {}
for col in features:
    encoders[col] = LabelEncoder()
    df_ml[col + '_enc'] = encoders[col].fit_transform(df_ml[col])
```""",
    "Hình 18. Mã nguồn chia tập dữ liệu": """```python
X = df_ml[[f + '_enc' for f in features]]
y = df_ml['salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```""",
    "Hình 20. Mã nguồn huấn luyện": """```python
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"R² Score: {r2:.3f}")
print(f"MAE: ${mae:,.0f}")
```""",
    "Hình 21. Mã nguồn biểu đồ dự đoán": """```python
def predict_salary(job, exp, emp_type, industry, size):
    # ... (code dự đoán)
    return model.predict(x)[0]

# ... (code vẽ biểu đồ dự đoán)
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(range(len(predictions)), predictions, color=colors)
```"""
}

# Also map missing images that we found in the grep search but didn't map before
image_map = {
    "Hình 16": "images/salary_heatmap.png",
    "Hình 19": "images/feature_importance.png"
}

lines = content.split("\n")
new_lines = []

for line in lines:
    inserted = False
    
    # Check for Code Snippets
    for key, code in code_snippets.items():
        if key in line and "..." not in line: # Avoid TOC
            # Insert code BEFORE the caption
            new_lines.append(code + "\n")
            new_lines.append(line + "\n")
            inserted = True
            break
            
    # Check for Images
    if not inserted:
        for key, img_path in image_map.items():
            if key in line and "..." not in line:
                # Insert image BEFORE the caption
                new_lines.append(f"![{key}]({img_path})\n")
                new_lines.append(line + "\n")
                inserted = True
                break
    
    if not inserted:
        new_lines.append(line + "\n")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("".join(new_lines))

print("Inserted code snippets and remaining images.")
