def to_decimal(value, base):
    try:
        return int(value, base)
    except:
        return None

def decimal_to_binary(decimal_value):
    return bin(decimal_value)[2:]

def decimal_to_hex(decimal_value):
    return hex(decimal_value)[2:].upper()

def main():
    from_base = int(input("Nhập vào hệ số"))
    to_base = int(input("Nhập hệ cơ số muốn chuyển sang"))
    value = input("Nhập giá trị cần chuyển đổi: ")

    if from_base not in (2, 10, 16) or to_base not in (2, 10, 16):
        print("Hệ số không hợp lệ")
        return

    decimal_value = to_decimal(value, from_base)
    if decimal_value is None:
        print("Giá trị không hợp lệ cho hệ", from_base)
        return

    if to_base == 10:
        print("Kết quả:", decimal_value)
    elif to_base == 2:
        print("Kết quả:", decimal_to_binary(decimal_value))
    elif to_base == 16:
        print("Kết quả:", decimal_to_hex(decimal_value))

if __name__ == "__main__":
    main()