a, b, c = map(int, input().split())

so_lon_nhi = 0
if (a >= b and a <= c) or (a <= b and a >= c):
    so_lon_nhi = a
elif (b >= a and b <= c) or (b <= a and b >= c):
    so_lon_nhi = b
else:
    so_lon_nhi = c
print(so_lon_nhi)