so_nam = int(input("Nhap so nam: "))
if so_nam % 400:
    print("la nam nhuan")
elif so_nam % 4 == 0 and so_nam % 100 != 0:
    print("la nam nhuan")
else:
    print("khong phai la nam nhuan")