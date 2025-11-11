while True:
    n = int(input())
    if n == 0:
        break
so_lon_nhat = -999999999
while n != 0:
    if n > so_lon_nhat:
        so_lon_nhat = n
print(so_lon_nhat)