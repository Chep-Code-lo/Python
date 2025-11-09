import math

n = int(input())

term1 = math.floor((n - 1) / 4)
term2 = math.floor((n - 1) / 100)
term3 = math.floor((n - 1) / 400)
day_of_the_week = (n + term1 - term2 + term3) % 7

if day_of_the_week == 0:
    thu = "Chủ nhật"
elif day_of_the_week == 1:
    thu = "Thứ Hai"
elif day_of_the_week == 2:
    thu = "Thứ Ba"
elif day_of_the_week == 3:
    thu = "Thứ Tư"
elif day_of_the_week == 4:
    thu = "Thứ Năm"
elif day_of_the_week == 5:
    thu = "Thứ Sáu"
else: 
    thu = "Thứ Bảy"
print(f"Ngày 1 tháng 1 năm {n} là ngày: {thu}")