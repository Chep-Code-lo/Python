a, b, c = map(int, input().split())

if a > 0:
    min_duong = a
if b > 0 and b < min_duong:
    min_duong = b
if c > 0 and c < min_duong:
    min_duong = c
if min_duong == float('inf'):
    print("KHONG co so duong")
else:
    print(min_duong)