import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Churn_Modelling.csv", header=0, index_col="RowNumber")

print("Shape:", df.shape)
print(df.head())

desc_num = df.describe()
print("\n=== Describe (numeric) ===")
print(desc_num)

desc_all = df.describe(include="all")
print("\n=== Describe (all columns) ===")
print(desc_all)

mean_credit_by_geo = df.groupby("Geography")["CreditScore"].mean().sort_values(ascending=False)
print("\n=== Mean CreditScore by Geography ===")
print(mean_credit_by_geo)

df["AgeGroup"] = pd.qcut(df["Age"], q=5, duplicates="drop")

print("\n=== AgeGroup value counts (check ~20% each) ===")
print(df["AgeGroup"].value_counts(dropna=False))

age_counts = df["AgeGroup"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.bar(age_counts.index.astype(str), age_counts.values)
plt.title("Number of Customers by Age Group (Equal Frequency - 5 groups)")
plt.xlabel("Age Group (Interval)")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
