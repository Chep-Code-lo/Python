my_list = [2, 5, 8, 12, 19, 25]

b = int(input("Nhập số b cần chèn: "))

index_to_insert = len(my_list) 
for i in range(len(my_list)):
    if my_list[i] >= b:
        index_to_insert = i
        break 
my_list.insert(index_to_insert, b)
print(f"List sau khi chèn: {my_list}")