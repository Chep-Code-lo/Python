while True:
    n = int(input())
    if n > 0 :
        break
    else:
        print("Nhap lai n > 0")
tong_chu_so = 0
while n > 0:
    chu_so = n % 10
    tong_chu_so += chu_so
    n //= 10
print(tong_chu_so)