import os

file_path = "Báo_cáo_python.md"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the start and end markers for the section to replace
start_marker = "**BỘ GIÁO DỤC VÀ ĐÀO TẠO**"
end_marker = "|24110190|Trần Phước Đại|"

start_index = content.find(start_marker)
end_index = content.find(end_marker)

if start_index != -1 and end_index != -1:
    # Calculate the full range to replace
    end_index += len(end_marker)
    
    # The new content formatted as a single-cell table to simulate a frame
    new_cover = """| <br>**BỘ GIÁO DỤC VÀ ĐÀO TẠO**<br>**TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT TP.HCM**<br>**KHOA CÔNG NGHỆ THÔNG TIN**<br><br><br><br><br>**BÀI TẬP LỚN**<br>**MÔN HỌC : LẬP TRÌNH PYTHON**<br>**TÊN ĐỀ TÀI : PHÂN TÍCH THỊ TRƯỜNG VIỆC LÀM AI**<br>**Mã lớp học phần :  IPPA233277_04**<br>**Học kỳ 2 – Năm học 2025-2026**<br>**Giảng viên hướng dẫn : Ts. Phan Thị Thể**<br><br>**Danh sách sinh viên thực hiện:**<br>24162008 - Phạm Hồng Anh<br>24162064 - Tăng Anh Kiệt<br>24162081 - Phạm Hữu Ngọc<br>24110190 - Trần Phước Đại<br><br>_Thành phố Hồ Chí Minh, tháng 12 năm 2025_<br> |
| :---: |"""
    
    # Construct the new content
    new_content = content[:start_index] + new_cover + content[end_index:]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Cover page restored with a frame.")
else:
    print("Could not find the cover page section to replace.")
