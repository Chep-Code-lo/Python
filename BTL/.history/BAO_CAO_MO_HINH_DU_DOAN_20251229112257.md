# BÁO CÁO DỰ ÁN PHÂN TÍCH THỊ TRƯỜNG VIỆC LÀM AI
## Phần 5: Dự Đoán Lương (Machine Learning)

---

# 3.4 Xử lý dữ liệu trước thống kê (Machine Learning)

## 3.4.1 Mã hóa dữ liệu

### a) Phương pháp sử dụng: One-Hot Encoding

One-Hot Encoding là kỹ thuật chuyển đổi dữ liệu categorical (phân loại) thành dạng số mà máy học có thể xử lý được.

**Nguyên lý hoạt động:**
- Mỗi giá trị unique trong một cột categorical sẽ được tạo thành một cột mới
- Giá trị 1 nếu dòng đó thuộc category, 0 nếu không

**Ví dụ minh họa:**

| experience_level | → | Entry | Mid | Senior |
|------------------|---|-------|-----|--------|
| Entry            |   | 1     | 0   | 0      |
| Senior           |   | 0     | 0   | 1      |
| Mid              |   | 0     | 1   | 0      |

**Code thực hiện:**
```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X = encoder.fit_transform(df_ml[features])
```

**Tham số quan trọng:**
- `sparse_output=False`: Trả về dense array thay vì sparse matrix
- `handle_unknown='ignore'`: Bỏ qua các category không có trong training data

### b) Các features được mã hóa

| Feature | Số categories | Mô tả |
|---------|---------------|-------|
| `job_title` | 8 | Vị trí công việc (Data Scientist, ML Engineer, ...) |
| `experience_level` | 3 | Cấp độ kinh nghiệm (Entry, Mid, Senior) |
| `employment_type` | 4 | Loại hình việc làm (Full-time, Contract, Remote, Internship) |
| `industry` | 7 | Ngành nghề (Tech, Finance, Healthcare, ...) |
| `company_size` | 3 | Quy mô công ty (Startup, Mid, Large) |

**Tổng số features sau One-Hot Encoding: ~25 columns**

---

## 3.4.2 Chia tập dữ liệu

### a) Phương pháp Train/Test Split

Để đánh giá chính xác hiệu quả của mô hình, cần chia dữ liệu thành hai phần riêng biệt: một phần để huấn luyện (training) và một phần để kiểm tra (test). Điều này giúp đảm bảo mô hình không chỉ học thuộc dữ liệu mà còn có khả năng tổng quát hóa tốt trên dữ liệu mới.

Dữ liệu được chia thành 2 phần:
- **Training set (80%)**: Dùng để huấn luyện mô hình
- **Test set (20%)**: Dùng để đánh giá mô hình

**Code thực hiện:**
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42
)
```

**Giải thích các tham số:**
- `X, y`: Features và target variable
- `test_size=0.2`: 20% dữ liệu dành cho test
- `random_state=42`: Seed để đảm bảo kết quả có thể tái tạo

### b) Thống kê sau khi chia

| Tập dữ liệu | Số lượng mẫu | Tỷ lệ |
|-------------|--------------|-------|
| Training set | 1,600 | 80% |
| Test set | 400 | 20% |
| **Tổng** | **2,000** | **100%** |

### c) Tại sao chọn tỷ lệ 80/20?

- **Đủ dữ liệu train**: 1,600 mẫu đủ để model học được pattern
- **Đủ dữ liệu test**: 400 mẫu đủ để đánh giá độ chính xác
- **Random state = 42**: Đảm bảo kết quả reproducible (có thể tái tạo)

---

# 3.5 Xây dựng mô hình và Chức năng dự đoán

## 3.5.1 Giới thiệu mô hình

### a) Mô hình được chọn: ElasticNet Regression

**ElasticNet** là mô hình hồi quy tuyến tính kết hợp hai kỹ thuật regularization:
- **L1 (Lasso)**: Giúp feature selection, đưa một số hệ số về 0
- **L2 (Ridge)**: Giúp giảm overfitting, thu nhỏ các hệ số

**Công thức toán học:**

$$\text{Loss} = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \alpha \cdot l_1\_ratio \cdot \sum_{j=1}^{p}|\beta_j| + \alpha \cdot (1 - l_1\_ratio) \cdot \sum_{j=1}^{p}\beta_j^2$$

Trong đó:
- $\alpha$ (alpha): Độ mạnh của regularization
- $l_1\_ratio$: Tỷ lệ giữa L1 và L2 (0.5 = cân bằng)

### b) Tại sao chọn ElasticNet?

| Tiêu chí | ElasticNet | Linear Regression | Random Forest |
|----------|------------|-------------------|---------------|
| Xử lý nhiều features | ✅ Tốt | ❌ Overfitting | ✅ Tốt |
| Interpretability | ✅ Cao | ✅ Cao | ❌ Thấp |
| Tốc độ train | ✅ Nhanh | ✅ Nhanh | ❌ Chậm |
| Feature selection | ✅ Có | ❌ Không | ❌ Không |

### c) Tham số mô hình

Việc lựa chọn tham số phù hợp ảnh hưởng trực tiếp đến hiệu quả của mô hình. Dưới đây là các tham số được sử dụng cho ElasticNet trong dự án này:

```python
model = ElasticNet(
    alpha=0.5,        # Độ mạnh regularization
    l1_ratio=0.5,     # Cân bằng L1 và L2
    max_iter=10000,   # Số iteration tối đa
    random_state=42   # Seed cho reproducibility
)
```

**Chi tiết các tham số:**
- **alpha = 0.5**: Mức độ regularization vừa phải, cân bằng giữa việc fit dữ liệu và tránh overfitting
- **l1_ratio = 0.5**: Kết hợp 50% L1 (Lasso) và 50% L2 (Ridge), tận dụng ưu điểm của cả hai
- **max_iter = 10000**: Đảm bảo thuật toán hội tụ đầy đủ
- **random_state = 42**: Giúp kết quả có thể tái tạo được

---

## 3.5.2 Huấn luyện và đánh giá

### a) Quá trình huấn luyện

Sau khi chuẩn bị dữ liệu và khởi tạo mô hình ElasticNet với các tham số đã chọn, tiến hành huấn luyện mô hình trên tập training set. Quá trình này giúp mô hình học được mối quan hệ giữa các features (vị trí, kinh nghiệm, ngành, ...) và biến mục tiêu (lương).

**Code thực hiện:**

```python
# Huấn luyện mô hình trên tập training
model.fit(X_train, y_train)

# Dự đoán lương trên tập test để đánh giá
y_pred = model.predict(X_test)
```

**Giải thích:**
- `model.fit()`: Mô hình học từ 1,600 mẫu trong tập training, tìm các hệ số tối ưu để minimize loss function
- `model.predict()`: Sử dụng mô hình đã huấn luyện để dự đoán lương cho 400 mẫu trong tập test

### b) Metrics đánh giá

**1. R² Score (Coefficient of Determination)**

$$R^2 = 1 - \frac{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2}$$

- Đo lường % variance của dữ liệu được giải thích bởi mô hình
- Giá trị từ 0 đến 1 (càng cao càng tốt)

**2. MAE (Mean Absolute Error)**

$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

- Sai số trung bình tuyệt đối
- Đơn vị: USD (dễ hiểu)

### c) Kết quả đánh giá

| Metric | Giá trị | Đánh giá |
|--------|---------|----------|
| **R² Score** | **0.6868** | Khá tốt (giải thích 69% variance) |
| **MAE** | **$20,261** | Sai số trung bình ~$20k |

**Biểu đồ So sánh Lương Thực tế vs Dự đoán:**

Để trực quan hóa hiệu quả của mô hình, biểu đồ scatter dưới đây so sánh giá trị lương thực tế (trục X) với giá trị lương dự đoán (trục Y) trên tập test 400 mẫu. Nếu mô hình dự đoán hoàn hảo, tất cả các điểm sẽ nằm trên đường chéo đỏ.

![So Sánh Lương Thực Tế vs Dự Đoán](./images/actual_vs_predicted.png)

*Hình 1: Biểu đồ scatter so sánh giữa lương thực tế và lương dự đoán. Đường đỏ nét đứt thể hiện dự đoán hoàn hảo (Actual = Predicted). Các điểm càng gần đường đỏ, mô hình càng chính xác.*

**Thang đánh giá R²:**

| R² Score | Đánh giá |
|----------|----------|
| > 0.9 | Xuất sắc |
| 0.7 - 0.9 | Tốt |
| **0.5 - 0.7** | **Khá ✅** |
| 0.3 - 0.5 | Trung bình |
| < 0.3 | Yếu |

### d) Phân tích kết quả

**Mô hình đạt R² = 0.6868 vì:**

✅ **Dữ liệu có pattern rõ ràng:**
- Senior > Mid > Entry (theo kinh nghiệm)
- Finance/Tech > Education/Retail (theo ngành)
- Large > Mid > Startup (theo quy mô công ty)

✅ **Features phù hợp:**
- 5 features categorical đều ảnh hưởng đến lương
- One-Hot Encoding giữ được thông tin categorical

**Biểu đồ Phân phối Sai số:**

Biểu đồ histogram dưới đây thể hiện phân phối sai số dự đoán (Actual - Predicted). Một mô hình tốt sẽ có sai số tập trung quanh giá trị 0, cho thấy không có xu hướng đoán cao hơn hoặc thấp hơn giá trị thực tế một cách có hệ thống.

![Phân Phối Sai Số Dự Đoán](./images/error_distribution.png)

*Hình 2: Phân phối sai số dự đoán (Actual - Predicted). Sai số tập trung quanh 0 cho thấy mô hình không có xu hướng đoán cao hoặc thấp hơn.*

**Biểu đồ Lương theo Kinh nghiệm:**

Biểu đồ cột ngang dưới đây minh họa mức lương trung bình theo từng cấp độ kinh nghiệm trong tập dữ liệu. Đây là một trong những pattern quan trọng mà mô hình đã học được để đưa ra dự đoán chính xác.

![Lương Theo Cấp Độ Kinh Nghiệm](./images/salary_by_experience.png)

*Hình 3: Lương trung bình theo cấp độ kinh nghiệm. Senior có mức lương cao nhất, tiếp theo là Mid và Entry.*

---

## 3.5.3 Chức năng dự đoán lương

### a) Hàm dự đoán

Sau khi huấn luyện thành công, mô hình có thể được sử dụng để dự đoán lương cho các trường hợp mới. Hàm `predict_salary()` được xây dựng để nhận vào các thông tin về vị trí công việc và trả về mức lương dự đoán.

**Code thực hiện:**

```python
def predict_salary(job, exp, emp_type, industry, size):
    """
    Dự đoán lương dựa trên các thông tin đầu vào
    
    Parameters:
    -----------
    job : str - Vị trí công việc
    exp : str - Cấp độ kinh nghiệm (Entry/Mid/Senior)
    emp_type : str - Loại hình việc làm
    industry : str - Ngành nghề
    size : str - Quy mô công ty
    
    Returns:
    --------
    float - Mức lương dự đoán (USD/năm)
    """
    input_data = pd.DataFrame({
        'job_title': [job],
        'experience_level': [exp],
        'employment_type': [emp_type],
        'industry': [industry],
        'company_size': [size]
    })
    
    x_encoded = encoder.transform(input_data)
    predicted_salary = model.predict(x_encoded)[0]
    
    return max(predicted_salary, 0)  # Đảm bảo không âm
```

### b) Ví dụ sử dụng

Để minh họa cách sử dụng hàm dự đoán, ta thử với một trường hợp cụ thể: một Data Scientist cấp Senior, làm việc Full-time trong ngành Tech tại công ty lớn.

**Input:**
```python
predict_salary(
    job='Data Scientist',
    exp='Senior', 
    emp_type='Full-time',
    industry='Tech',
    size='Large'
)
```

**Output:** `$198,543`

Kết quả cho thấy mức lương dự đoán khoảng ~$200,000/năm - phù hợp với thực tế thị trường cho vị trí Senior Data Scientist tại các công ty công nghệ lớn.

### c) Kết quả dự đoán mẫu

Dưới đây là kết quả dự đoán cho một số trường hợp điển hình, thể hiện sự khác biệt về lương giữa các cấp độ kinh nghiệm và vị trí công việc:

| Vị trí | Kinh nghiệm | Ngành | Quy mô | Lương dự đoán |
|--------|-------------|-------|--------|---------------|
| Data Scientist | Senior | Tech | Large | ~$200,000 |
| ML Engineer | Mid | Tech | Large | ~$140,000 |
| Data Analyst | Entry | Tech | Mid | ~$60,000 |

**Nhận xét:** Kết quả dự đoán phản ánh đúng xu hướng thực tế - lương tăng theo cấp độ kinh nghiệm, với mức chênh lệch đáng kể giữa Entry và Senior level.

### d) Biểu đồ trực quan hóa

Biểu đồ cột dưới đây minh họa kết quả dự đoán lương cho 3 trường hợp điển hình, giúp người dùng dễ dàng so sánh mức lương giữa các vị trí và cấp độ kinh nghiệm khác nhau.

![Dự Đoán Lương](./images/salary_prediction.png)

*Hình 4: Kết quả dự đoán lương cho các vị trí khác nhau. Biểu đồ thể hiện mức lương dự đoán theo vị trí công việc và cấp độ kinh nghiệm.*

**Giải thích biểu đồ:**
- Trục X: Vị trí công việc và cấp độ kinh nghiệm
- Trục Y: Mức lương dự đoán (USD/năm)
- Màu sắc: Phân biệt các vị trí khác nhau

---

# 4. Kết luận

## 4.1 Tóm tắt kết quả

| Tiêu chí | Kết quả |
|----------|---------|
| Mô hình | ElasticNet Regression |
| R² Score | 0.6868 (Khá tốt) |
| MAE | $20,261 |
| Số features | 5 (sau encoding: ~25) |
| Tập dữ liệu | 2,000 mẫu |

## 4.2 Ưu điểm của mô hình

✅ **Độ chính xác khá**: R² = 0.6868 cho thấy mô hình học được pattern từ dữ liệu

✅ **Dễ hiểu**: Mô hình tuyến tính, có thể giải thích được kết quả

✅ **Nhanh**: Huấn luyện và dự đoán nhanh chóng

✅ **Ổn định**: Regularization giúp tránh overfitting

## 4.3 Hạn chế

❌ **Dữ liệu giới hạn**: Chỉ có 5 features cơ bản

❌ **Không xét đến skills**: Kỹ năng cụ thể có thể ảnh hưởng nhiều đến lương

❌ **Không xét location**: Vị trí địa lý ảnh hưởng lớn đến mức lương

## 4.4 Hướng phát triển

1. **Thêm features**: skills, location, years of experience
2. **Thử mô hình phức tạp hơn**: XGBoost, Neural Network
3. **Hyperparameter tuning**: GridSearchCV để tìm tham số tối ưu
4. **Cross-validation**: Đánh giá ổn định hơn với K-Fold

---

*Báo cáo được tạo: 29/12/2025*
*Mô hình: ElasticNet Regression với One-Hot Encoding*
*R² Score: 0.6868 | MAE: $20,261*
