import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import re

# Load data
df = pd.read_csv('Data/ai_job_market.csv')

# Parse salary_range_usd to get salary
def parse_salary(s):
    if pd.isna(s):
        return None
    nums = re.findall(r'\d+', str(s).replace(',', ''))
    if len(nums) >= 2:
        return (int(nums[0]) + int(nums[1])) / 2
    elif len(nums) == 1:
        return int(nums[0])
    return None

df['salary'] = df['salary_range_usd'].apply(parse_salary)
df_ml = df.copy()

# Features
features = ['job_title', 'experience_level', 'employment_type', 'industry', 'company_size']
for col in features:
    df_ml[col] = df_ml[col].fillna('Unknown')
df_ml = df_ml.dropna(subset=['salary'])

print(f"Total samples: {len(df_ml)}")

# Encoding
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X = encoder.fit_transform(df_ml[features])
y = df_ml['salary'].values

print(f"Features after encoding: {X.shape[1]}")

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = ElasticNet(alpha=0.5, l1_ratio=0.5, max_iter=10000, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"R2: {r2_score(y_test, y_pred):.4f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred):,.0f}")

# Get common jobs  
common_jobs = df_ml['job_title'].value_counts().head(3).index.tolist()
print(f"Top 3 jobs: {common_jobs}")

# Predict function
def predict_salary(job, exp, emp_type, industry, size):
    input_data = pd.DataFrame({
        'job_title': [job],
        'experience_level': [exp],
        'employment_type': [emp_type],
        'industry': [industry],
        'company_size': [size]
    })
    x_encoded = encoder.transform(input_data)
    return max(model.predict(x_encoded)[0], 0)

# Test predictions
print("\n=== Predictions ===")
tests = [
    (common_jobs[0], 'Senior', 'Full-time', 'Tech', 'Large'),
    (common_jobs[1], 'Mid', 'Full-time', 'Tech', 'Large'),
    (common_jobs[2], 'Entry', 'Full-time', 'Tech', 'Mid'),
]

for job, exp, emp, ind, size in tests:
    sal = predict_salary(job, exp, emp, ind, size)
    print(f"  {job} ({exp}, {emp}, {ind}, {size}): ${sal:,.0f}")
