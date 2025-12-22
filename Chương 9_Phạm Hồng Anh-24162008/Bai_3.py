import pandas as pd

file_path = "u.user"

df = pd.read_csv(file_path, sep="|", header=0)  
print("Số dòng, số cột:", df.shape)
print(df.head())

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df = df.dropna(subset=["age"])
df["age"] = df["age"].astype(int)

avg_age_by_job = df.groupby("occupation")["age"].mean()
print("\n=== Tuổi trung bình theo nghề ===")
print(avg_age_by_job)

male_ratio_by_job = (
    df.assign(is_male=(df["gender"] == "M").astype(int))
      .groupby("occupation")["is_male"]
      .mean()
      .sort_values(ascending=False)
)
print("\n=== Tỷ lệ nam theo nghề (giảm dần) ===")
print(male_ratio_by_job)

min_max_age_by_job = df.groupby("occupation")["age"].agg(["min", "max"])
print("\n=== Min/Max tuổi theo nghề ===")
print(min_max_age_by_job)

avg_age_job_gender = df.groupby(["occupation", "gender"])["age"].mean()
print("\n=== Tuổi TB theo nghề & giới ===")
print(avg_age_job_gender)

gender_count = df.groupby(["occupation", "gender"]).size().unstack(fill_value=0)
gender_percent = gender_count.div(gender_count.sum(axis=1), axis=0) * 100

print("\n=== % Nam – Nữ theo nghề ===")
print(gender_percent.round(2))
