while True:
    binary_string = input("Nhập chuỗi 8-bit nhị phân (để trống để thoát): ")

    if binary_string == " ":
        print("Đã thoát chương trình.")
        break

    if len(binary_string) != 8:
        print(f"Lỗi: Chuỗi '{binary_string}' không có 8 bit. Vui lòng nhập lại.")
        continue 

    is_binary = True
    for char in binary_string:
        if char != '0' and char != '1':
            is_binary = False
            break 

    if not is_binary:
        print(f"Lỗi: Chuỗi '{binary_string}' chứa ký tự không phải '0' hoặc '1'.")
        continue 

    one_count = binary_string.count('1')

    parity_bit = '0'
    if one_count % 2 != 0:
        parity_bit = '1'

    print(f"Bit Parity Chẵn cần thêm: {parity_bit}")