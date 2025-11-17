while True:
    while True:
        n = int(input())
        if n > 0:
            break
        else :
            print("Vui lòng nhập số nguyên dương")

    max_le = None

    print("Nhập n số nguyên dương")

    for i in range(n):
        while True:
            try:
                num = int(input(f"Nhập số thứ {i + 1}: "))
                break
            except ValueError:
                print(f"Lỗi: '{num}' không phải là số nguyên. Vui lòng nhập lại.")
        
        if num % 2 != 0:
            if max_le is None or num > max_le:
                max_le = num

    if max_le is None:
        print("Không tìm thấy số lẻ nào trong các số bạn đã nhập.")
    else:
        print(f"Số lẻ lớn nhất trong những số được nhập là: {max_le}")

    print("-" * 30)
    choice = input("Bạn có muốn tiếp tục không? (nhấn 'c' để tiếp tục, phím khác để thoát): ")
    
    if choice.lower().strip() != 'c':
        print("Đã thoát chương trình. Tạm biệt!")
        break