s = input("Nhập chuỗi số nhị phân: ")

decimal_value = 0
power = 0 

for digit in reversed(s):
    if digit == '1':
        decimal_value += 2**power
    power += 1

print(f"Chuỗi nhị phân {s} tương ứng với số thập phân là: {decimal_value}")