so_lon_nhat = -999999999
n = int(input())
while n != 0:
    if n > so_lon_nhat:
        so_lon_nhat = n
    n = int(input())
print(so_lon_nhat)