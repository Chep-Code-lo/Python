nhietdo = []
for i in range(7):
    x = float(input())
    nhietdo.append(x)
tong = 0
for x in nhietdo:
    tong += x
tb = tong / 7
dem = 0
for x in nhietdo:
    if x > tb:
        dem += 1
print("Nhiệt độ trung bình của tuần là:", tb)
print("Số ngày có nhiệt độ lớn hơn trung bình là:", dem)