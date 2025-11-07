n = int(input())
d = abs(n)
tram = d // 100 % 10
chuc = d // 10 % 10
donvi = d % 10
print((tram + chuc + donvi) / 3)