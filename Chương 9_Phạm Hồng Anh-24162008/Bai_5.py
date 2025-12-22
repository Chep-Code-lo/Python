import pandas as pd
import numpy as np

file_path = "wind.data"
df = pd.read_csv(file_path, sep=r"\s+")   

print("Shape:", df.shape)
print(df.head())
print(df.columns)

df["Year"] = np.where(df["Yr"] < 100, 1900 + df["Yr"], df["Yr"])

df["Yr_Mo_Dy"] = pd.to_datetime(
    dict(year=df["Year"], month=df["Mo"], day=df["Dy"]),
    errors="coerce"
)

df["Yr_Mo_Dy"] = df["Yr_Mo_Dy"].dt.strftime("%Y-%m-%d")

df = df.set_index("Yr_Mo_Dy")

df = df.drop(columns=["Year"])

print("\nAfter set index:")
print(df.head())

wind_cols = df.loc[:, "RPT":"MAL"]

present_count = wind_cols.notna().sum()
missing_count = wind_cols.isna().sum()

d_stats = pd.DataFrame({"present": present_count, "missing": missing_count})
print("\n=== Present/Missing count (RPT -> MAL) ===")
print(d_stats)

overall_mean = wind_cols.stack().mean()
print("\n=== Overall mean wind speed (all locations & times) ===")
print(overall_mean)

loc_stats = wind_cols.agg(["min", "max", "mean", "std"]).T
loc_stats = loc_stats.rename(columns={"std": "std_dev"})
print("\n=== loc_stats ===")
print(loc_stats)

dt_index = pd.to_datetime(df.index, format="%Y-%m-%d", errors="coerce")
jan_mean_by_loc = wind_cols.loc[dt_index.month == 1].mean()

print("\n=== Mean wind speed in January (each location) ===")
print(jan_mean_by_loc)

df_dt = df.copy()
df_dt.index = dt_index

yearly = df_dt.loc[:, "RPT":"MAL"].resample("Y").mean()
monthly_year = df_dt.loc[:, "RPT":"MAL"].resample("M").mean()
weekly = df_dt.loc[:, "RPT":"MAL"].resample("W").mean()

print("\n=== Yearly mean (head) ===")
print(yearly.head())

print("\n=== Monthly-Year mean (head) ===")
print(monthly_year.head())

print("\n=== Weekly mean (head) ===")
print(weekly.head())
