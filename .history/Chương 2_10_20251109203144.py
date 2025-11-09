a, b, c, d, e = map(float, input().split())

so_duong = 0
so_am = 0
so_khong = 0

if a > 0:
    so_duong = so_duong + 1
elif a < 0:
    so_am = so_am + 1
else:
    so_khong = so_khong + 1

if b > 0:
    so_duong = so_duong + 1
elif b < 0:
    so_am = so_am + 1
else:
    so_khong = so_khong + 1

if c > 0:
    so_duong = so_duong + 1
elif c < 0:
    so_am = so_am + 1
else:
    so_khong = so_khong + 1

if d > 0:
    so_duong = so_duong + 1
elif d < 0:
    so_am = so_am + 1
else:
    so_khong = so_khong + 1

if e > 0:
    so_duong = so_duong + 1
elif e < 0:
    so_am = so_am + 1
else:
    so_khong = so_khong + 1

print(f"- {so_duong} số dương")
print(f"- {so_am} số âm")
print(f"- {so_khong} số bằng 0")