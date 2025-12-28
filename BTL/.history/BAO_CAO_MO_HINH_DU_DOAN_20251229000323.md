# BÁO CÁO MÔ HÌNH DỰ ĐOÁN LƯƠNG
## Phân Tích Thị Trường Việc Làm AI

---

## 1. TỔNG QUAN MÔ HÌNH

### 1.1. Mô hình sử dụng: **ElasticNet Regression**

ElasticNet là sự kết hợp giữa **Ridge Regression (L2)** và **Lasso Regression (L1)**:
- Kết hợp ưu điểm của cả hai phương pháp regularization
- Phù hợp với dữ liệu có nhiều features (sau One-Hot Encoding)
- Tham số: `alpha=0.5`, `l1_ratio=0.5`

### 1.2. Features (Tiêu chí dự đoán)

| Feature | Mô tả | Số categories |
|---------|-------|---------------|
| `job_title` | Vị trí công việc | ~15+ loại |
| `experience_level` | Cấp độ kinh nghiệm | 3 (Entry, Mid, Senior) |
| `employment_type` | Loại hình làm việc | 4 (Full-time, Contract, Remote, Internship) |
| `industry` | Ngành nghề | ~8 loại |
| `company_size` | Quy mô công ty | 3 (Startup, Mid, Large) |

### 1.3. Phương pháp mã hóa: **One-Hot Encoding**
- Chuyển categorical features thành binary columns (0/1)
- Tổng số features sau encoding: ~35-40 columns

---

## 2. KẾT QUẢ ĐÁNH GIÁ

| Metric | Giá trị | Ý nghĩa |
|--------|---------|---------|
| **R² Score** | **~-0.08** (âm) | Mô hình kém hơn baseline |
| **MAE** | ~$29,000 | Sai số trung bình ~$29k |

---

## 3. TẠI SAO R² SCORE BỊ ÂM? 🔴

### 3.1. R² Score là gì?

```
R² = 1 - (SS_res / SS_tot)

Trong đó:
- SS_res = Σ(y_actual - y_predicted)²  → Sai số của mô hình
- SS_tot = Σ(y_actual - y_mean)²       → Sai số của baseline (dùng mean)
```

**Giải thích:**
- **R² = 1**: Mô hình hoàn hảo
- **R² = 0**: Mô hình tương đương với việc chỉ dùng giá trị trung bình
- **R² < 0**: Mô hình **TỆ HƠN** việc chỉ dùng giá trị trung bình!

### 3.2. Nguyên nhân chính: **DỮ LIỆU SYNTHETIC (GIẢ LẬP)**

Sau khi phân tích file `ai_job_market.csv`, phát hiện dữ liệu có đặc điểm **BẤT THƯỜNG**:

#### ❌ Vấn đề 1: Salary không theo logic thực tế

| Experience | Ví dụ Salary trong dữ liệu | Thực tế |
|------------|---------------------------|---------|
| Entry | $124,496 - $217,204 | Thấp nhất |
| Internship | $138,184 - $192,857 | Rất thấp |
| Senior | $100,845 - $159,745 | Cao nhất |

**→ Entry/Intern có lương CAO HƠN Senior? Phi logic!**

#### ❌ Vấn đề 2: Không có correlation giữa features và salary

```
Correlation thực tế kỳ vọng:
- Senior > Mid > Entry (theo kinh nghiệm)
- Tech > Healthcare > Retail (theo ngành)
- Large > Mid > Startup (theo quy mô)

Dữ liệu synthetic:
- Salary được random, KHÔNG tuân theo pattern nào
```

#### ❌ Vấn đề 3: High variance, no signal

```
Salary trong cùng 1 nhóm (VD: Data Scientist + Senior + Tech):
- Row 1: $80,000
- Row 2: $180,000
- Row 3: $120,000
→ Variance quá cao, không có pattern để học
```

### 3.3. Minh họa trực quan

```
Dữ liệu thực tế (có pattern):          Dữ liệu synthetic (random):
                                       
Salary                                 Salary
  ^                                      ^
  |        * * *                         |    *     *
  |      * * *                           |  *   *     *
  |    * * *                             |      *   *
  |  * *                                 |  *     *   *
  +-----------> Experience               +-----------> Experience
  Entry  Mid  Senior                     Entry  Mid  Senior
  
  → Có xu hướng tăng                     → Random, không xu hướng
```

---

## 4. TẠI SAO MÔ HÌNH VẪN DỰ ĐOÁN ĐƯỢC?

Mặc dù R² âm, mô hình vẫn cho ra con số dự đoán vì:

1. **ElasticNet tính toán weighted average**: Dựa trên các coefficients học được
2. **One-Hot Encoding**: Tạo ra các features binary, model học "trung bình" của mỗi category
3. **Dự đoán ~mean của dataset**: Vì không có pattern, model quay về dự đoán gần giá trị trung bình

**→ Đây là lý do các dự đoán gần bằng nhau (~$127,000-$128,000)**

---

## 5. CÁC MÔ HÌNH ĐÃ THỬ NGHIỆM

| Mô hình | R² Score | Kết luận |
|---------|----------|----------|
| Linear Regression | < 0 | Âm |
| Ridge Regression | < 0 | Âm |
| Lasso Regression | < 0 | Âm |
| **ElasticNet** | **~-0.08** | **Tốt nhất (ít âm nhất)** |
| Random Forest | < 0 | Âm |
| Gradient Boosting | < 0 | Âm |
| SVR | < 0 | Âm |
| KNN | < 0 | Âm |

**→ TẤT CẢ đều âm vì dữ liệu không có pattern!**

---

## 6. KẾT LUẬN

### 6.1. Về mô hình ElasticNet
✅ **Đúng phương pháp**: ElasticNet + One-Hot Encoding là approach chuẩn cho categorical data
✅ **Code đúng**: Không có lỗi trong implementation
✅ **Best choice**: Trong các model đã thử, ElasticNet cho R² ít âm nhất

### 6.2. Về dữ liệu
❌ **Dữ liệu synthetic**: Được generate random, không phản ánh thực tế
❌ **Không có signal**: Salary không correlate với bất kỳ feature nào
❌ **High noise**: Variance quá cao trong cùng một nhóm

### 6.3. Khuyến nghị

| Nếu muốn | Giải pháp |
|----------|-----------|
| R² dương | Sử dụng dữ liệu thực từ Glassdoor, LinkedIn, Indeed |
| Demo học tập | Chấp nhận R² âm, giải thích nguyên nhân như báo cáo này |
| Cải thiện model | Không thể - vấn đề nằm ở DATA, không phải MODEL |

---

## 7. THAM KHẢO

- Scikit-learn ElasticNet: https://scikit-learn.org/stable/modules/linear_model.html#elastic-net
- One-Hot Encoding: https://scikit-learn.org/stable/modules/preprocessing.html#encoding-categorical-features
- R² Score interpretation: https://scikit-learn.org/stable/modules/model_evaluation.html#r2-score

---

*Báo cáo được tạo: 29/12/2025*
*Mô hình: ElasticNet Regression với One-Hot Encoding*
