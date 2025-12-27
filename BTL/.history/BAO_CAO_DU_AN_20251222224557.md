# 📊 BÁO CÁO PHÂN TÍCH THỊ TRƯỜNG VIỆC LÀM AI
## AI Job Market Analysis Report

---

## 📋 MỤC LỤC
1. [Giới thiệu dự án](#1-giới-thiệu-dự-án)
2. [Dữ liệu và tiền xử lý](#2-dữ-liệu-và-tiền-xử-lý)
3. [Phân tích tổng quan thị trường](#3-phân-tích-tổng-quan-thị-trường)
4. [Phân tích ngành và loại công việc](#4-phân-tích-ngành-và-loại-công-việc)
5. [Phân tích kỹ năng](#5-phân-tích-kỹ-năng)
6. [Phân tích lương (Heatmap)](#6-phân-tích-lương-heatmap)
7. [Mô hình Machine Learning dự đoán lương](#7-mô-hình-machine-learning-dự-đoán-lương)
8. [Kết luận và khuyến nghị](#8-kết-luận-và-khuyến-nghị)

---

## 1. GIỚI THIỆU DỰ ÁN

### 1.1 Mục tiêu
- Phân tích xu hướng thị trường việc làm trong lĩnh vực AI/Data Science
- Xác định các vị trí công việc phổ biến và mức lương tương ứng
- Tìm hiểu kỹ năng và công cụ được yêu cầu nhiều nhất
- Xây dựng mô hình dự đoán lương dựa trên các yếu tố đầu vào

### 1.2 Thư viện sử dụng

```python
import pandas as pd              # Xử lý dữ liệu dạng bảng
import numpy as np               # Tính toán số học
import matplotlib.pyplot as plt  # Vẽ biểu đồ
import seaborn as sns           # Vẽ biểu đồ nâng cao
from collections import Counter # Đếm tần suất
from sklearn.model_selection import train_test_split  # Chia dữ liệu train/test
from sklearn.preprocessing import LabelEncoder        # Mã hóa categorical
from sklearn.ensemble import RandomForestRegressor    # Mô hình ML
from sklearn.metrics import r2_score, mean_absolute_error  # Đánh giá mô hình
```

---

## 2. DỮ LIỆU VÀ TIỀN XỬ LÝ

### 2.1 Nguồn dữ liệu
- **File:** `ai_job_market.csv`
- **Số lượng:** 2000 bản ghi việc làm

### 2.2 Các cột dữ liệu
| Cột | Mô tả |
|-----|-------|
| `job_title` | Tên vị trí công việc |
| `experience_level` | Cấp độ kinh nghiệm (Entry, Mid, Senior) |
| `employment_type` | Loại hình làm việc (Full-time, Part-time, Contract, Remote, Internship) |
| `industry` | Ngành nghề |
| `company_size` | Quy mô công ty |
| `salary_range_usd` | Khoảng lương (dạng "min-max") |
| `skills_required` | Kỹ năng yêu cầu |
| `tools_preferred` | Công cụ ưa thích |
| `posted_date` | Ngày đăng tuyển |

### 2.3 Tiền xử lý dữ liệu

#### Công thức tính lương trung bình:

```python
# Tách cột salary_range_usd thành min và max
df[['min_sal', 'max_sal']] = df['salary_range_usd'].str.split('-', expand=True).astype(float)

# Tính lương trung bình
df['salary'] = (df['min_sal'] + df['max_sal']) / 2
```

**Công thức toán học:**
$$\text{Salary} = \frac{\text{min\_sal} + \text{max\_sal}}{2}$$

#### Chuyển đổi ngày tháng:
```python
df['posted_date'] = pd.to_datetime(df['posted_date'])
```

---

## 3. PHÂN TÍCH TỔNG QUAN THỊ TRƯỜNG

### 3.1 Top vị trí công việc

```python
df['job_title'].value_counts().head(8)
```

**Phương pháp:** Sử dụng `value_counts()` để đếm tần suất xuất hiện của mỗi vị trí công việc.

### 3.2 Lương trung bình theo vị trí

```python
df.groupby('job_title')['salary'].mean().sort_values()
```

**Phương pháp:** `groupby()` + `mean()` để tính trung bình lương theo nhóm.

**Công thức:**
$$\bar{x}_{job} = \frac{1}{n_{job}} \sum_{i=1}^{n_{job}} salary_i$$

Trong đó:
- $\bar{x}_{job}$ : Lương trung bình của vị trí job
- $n_{job}$ : Số lượng việc làm của vị trí đó

### 3.3 Phân bố kinh nghiệm

```python
df['experience_level'].value_counts()
```

**Biểu đồ:** Pie chart hiển thị tỷ lệ phần trăm:
- Entry: ~35%
- Mid: ~33%
- Senior: ~32%

---

## 4. PHÂN TÍCH NGÀNH VÀ LOẠI CÔNG VIỆC

### 4.1 Thống kê theo ngành

```python
ind_data = df.groupby('industry')['salary'].agg(['count', 'mean']).sort_values('count', ascending=False)
```

**Các hàm sử dụng:**
- `groupby('industry')`: Nhóm theo ngành
- `agg(['count', 'mean'])`: Tính đồng thời số lượng và trung bình
- `sort_values()`: Sắp xếp kết quả

### 4.2 Lương theo loại việc làm

```python
emp_data = df.groupby('employment_type')['salary'].agg(['count', 'mean']).sort_values('mean', ascending=False)
```

---

## 5. PHÂN TÍCH KỸ NĂNG

### 5.1 Trích xuất kỹ năng

```python
# Tách chuỗi kỹ năng thành list
all_skills = [s.strip() for skills in df['skills_required'].dropna() for s in skills.split(',')]

# Đếm tần suất
top_skills = pd.Series(Counter(all_skills)).sort_values(ascending=True).tail(12)
```

**Giải thích:**
1. `df['skills_required'].dropna()`: Loại bỏ giá trị null
2. `skills.split(',')`: Tách chuỗi theo dấu phẩy
3. `s.strip()`: Loại bỏ khoảng trắng thừa
4. `Counter()`: Đếm tần suất xuất hiện

### 5.2 Trích xuất công cụ

```python
all_tools = [t.strip() for tools in df['tools_preferred'].dropna() for t in tools.split(',')]
top_tools = pd.Series(Counter(all_tools)).sort_values(ascending=True).tail(10)
```

---

## 6. PHÂN TÍCH LƯƠNG (HEATMAP)

### 6.1 Tạo Pivot Table

```python
top_jobs = df['job_title'].value_counts().head(6).index

pivot = df[df['job_title'].isin(top_jobs)].pivot_table(
    values='salary',           # Giá trị cần tính
    index='job_title',         # Hàng
    columns='experience_level', # Cột
    aggfunc='mean'             # Hàm tổng hợp: trung bình
)
```

### 6.2 Vẽ Heatmap

```python
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='YlGnBu')
```

**Tham số:**
- `annot=True`: Hiển thị giá trị trên ô
- `fmt='.0f'`: Format số không có thập phân
- `cmap='YlGnBu'`: Bảng màu từ vàng → xanh lá → xanh dương

---

## 7. MÔ HÌNH MACHINE LEARNING DỰ ĐOÁN LƯƠNG

### 7.1 Chuẩn bị dữ liệu

#### Mã hóa Label Encoding:

```python
features = ['job_title', 'experience_level', 'employment_type', 'industry', 'company_size']
encoders = {}

for col in features:
    encoders[col] = LabelEncoder()
    df_ml[col + '_enc'] = encoders[col].fit_transform(df_ml[col])
```

**Label Encoding:** Chuyển đổi categorical → numerical
- Ví dụ: Entry → 0, Mid → 1, Senior → 2

### 7.2 Chia dữ liệu Train/Test

```python
X = df_ml[[f + '_enc' for f in features]]  # Features
y = df_ml['salary']                         # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

**Tỷ lệ:** 80% train, 20% test

### 7.3 Mô hình Random Forest Regressor

```python
model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

**Tham số:**
- `n_estimators=100`: Số lượng cây quyết định
- `random_state=42`: Seed để tái tạo kết quả
- `n_jobs=-1`: Sử dụng tất cả CPU cores

### 7.4 Đánh giá mô hình

#### R² Score (Coefficient of Determination):

$$R^2 = 1 - \frac{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2}$$

```python
r2 = r2_score(y_test, y_pred)
```

- $R^2 = 1$: Mô hình hoàn hảo
- $R^2 = 0$: Mô hình không tốt hơn dự đoán trung bình
- $R^2 < 0$: Mô hình tệ hơn dự đoán trung bình

#### Mean Absolute Error (MAE):

$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

```python
mae = mean_absolute_error(y_test, y_pred)
```

### 7.5 Feature Importance

```python
importance = pd.Series(model.feature_importances_, index=features).sort_values()
```

**Ý nghĩa:** Đo lường mức độ đóng góp của từng feature vào việc dự đoán.

### 7.6 Hàm dự đoán lương

```python
def predict_salary(job, exp, emp_type, industry, size):
    try:
        x = [[encoders['job_title'].transform([job])[0],
              encoders['experience_level'].transform([exp])[0],
              encoders['employment_type'].transform([emp_type])[0],
              encoders['industry'].transform([industry])[0],
              encoders['company_size'].transform([size])[0]]]
        return model.predict(x)[0]
    except: 
        return None
```

**Cách sử dụng:**
```python
salary = predict_salary('Data Scientist', 'Senior', 'Full-time', 'Tech', 'Large')
# Kết quả: $xxx,xxx
```

---

## 8. KẾT LUẬN VÀ KHUYẾN NGHỊ

### 8.1 Kết quả chính

| Chỉ số | Giá trị |
|--------|---------|
| Tổng số việc làm | 2,000 |
| Lương thấp nhất | ~$47,578 |
| Lương cao nhất | ~$197,776 |
| Lương trung bình | ~$122,000 |

### 8.2 Top vị trí công việc
1. Data Analyst
2. NLP Engineer
3. AI Product Manager
4. Quant Researcher
5. ML Engineer

### 8.3 Top kỹ năng cần học
1. TensorFlow
2. Excel
3. Pandas
4. FastAPI
5. NumPy

### 8.4 Top công cụ
1. MLflow
2. LangChain
3. FastAPI
4. KDB+
5. BigQuery

### 8.5 Khuyến nghị

1. **Kỹ năng:** Tập trung học Python, SQL, Machine Learning, TensorFlow
2. **Ngành nghề:** Nhắm đến ngành Tech/Finance (lương cao)
3. **Phát triển:** Entry → Senior có thể tăng lương ~30%
4. **Công cụ:** Làm quen với MLflow, LangChain, BigQuery

---

## 📚 TỔNG HỢP CÁC HÀM VÀ PHƯƠNG PHÁP

### Pandas
| Hàm | Mục đích |
|-----|----------|
| `pd.read_csv()` | Đọc file CSV |
| `df.groupby()` | Nhóm dữ liệu |
| `df.value_counts()` | Đếm tần suất |
| `df.pivot_table()` | Tạo bảng tổng hợp |
| `df.agg()` | Áp dụng nhiều hàm tổng hợp |
| `str.split()` | Tách chuỗi |

### Matplotlib/Seaborn
| Hàm | Mục đích |
|-----|----------|
| `plt.subplots()` | Tạo nhiều biểu đồ |
| `plot(kind='barh')` | Biểu đồ cột ngang |
| `plot(kind='pie')` | Biểu đồ tròn |
| `sns.heatmap()` | Biểu đồ nhiệt |

### Scikit-learn
| Hàm | Mục đích |
|-----|----------|
| `train_test_split()` | Chia dữ liệu |
| `LabelEncoder()` | Mã hóa categorical |
| `RandomForestRegressor()` | Mô hình hồi quy |
| `r2_score()` | Đánh giá R² |
| `mean_absolute_error()` | Đánh giá MAE |

---

**Ngày thực hiện:** December 2024  
**Công cụ:** Python, Jupyter Notebook, VS Code
