import numpy as np
import pandas as pd


s1 = pd.Series(np.random.randint(1, 5, size=100))          
s2 = pd.Series(np.random.randint(1, 4, size=100))         
s3 = pd.Series(np.random.randint(10000, 30001, size=100)) 

df = pd.concat([s1, s2, s3], axis=1)

df.columns = ["bedrs", "bathrs", "price_sqr_meter"]

bigcolumn = pd.concat([s1, s2, s3], ignore_index=True)
df["bigcolumn"] = pd.Series(bigcolumn.values) 

df_300 = pd.DataFrame({"bigcolumn": bigcolumn})
df_300.index = range(300)

print("=== DataFrame 100 dòng (3 cột + bigcolumn lấy 100 phần tử đầu) ===")
print(df.head())
print(df.shape)

print("\n=== DataFrame 300 dòng với index 0..299 (bigcolumn đủ 300 giá trị) ===")
print(df_300.head())
print(df_300.shape)
