my_list = [1.5, 10.2, 3.0, 50.7, 8.8, 4.0]

a = float(input("Nhập số s: "))
new_list = []
for num in my_list:
    if num <= a:
        new_list.append(num)
        
print(f"List ban đầu: {my_list}")
print(f"List sau khi lọc: {new_list}")

