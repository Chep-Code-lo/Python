n = int(input())
so_chu_so_7 = 0
while n > 0:
    chu_so = n % 10
    if chu_so == 7:
        so_chu_so_7 += 1
    n //= 10
print(so_chu_so_7)