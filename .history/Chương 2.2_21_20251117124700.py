list = [12, 45, 8, 20, 55, 91, 105, 3]

max_div_5 = None

for num in list:
    if num % 5 == 0:
        if max_div_5 is None or num > max_div_5:
            max_div_5 = num

if max_div_5 is not None:
    print(f"Số lớn nhất chia hết cho 5 là: {max_div_5}")
else:
    print(f"List {list} không có số nào chia hết cho 5.")