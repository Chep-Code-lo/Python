while True:
    n = int(input())
    if n > 0 and n < 13:
        break
    else:
        print("Nhap lai n(1-12)")
if n > 2 and n < 6:
    print("Mua xuan")
elif n > 5 and n < 9:
    print("Mua ha")
elif n > 8 and n < 12:
    print("Mua thu")
else:
    print("Mua dong")