n = int(input())
tong = 0
chuc_nghin = n // 10000 % 10
nghin = n // 1000 % 10
tram = n // 100 % 10
chuc = n // 10 % 10
donvi = n % 10
tong = chuc_nghin + nghin + tram + chuc + donvi
so_nut = tong % 10
print(so_nut)