import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Churn_Customer.csv", header=0, index_col="RowNumber")
thong_ke = df.describe(include="all")
print(thong_ke)

credit_score_follow_geography = df.groupby("Geography")["CreditScore"].mean()
print(credit_score_follow_geography)

df["Agegroup"] = pd.qcut(df["Age"], q=5, duplicates="drop")
