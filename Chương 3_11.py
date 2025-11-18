n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
am = []     
duong = []
for x in arr:
    if x < 0:
        am.append(x)
    elif x > 0:
        duong.append(x)
am.sort()
duong.sort()
duong.reverse()
dem_duong = 0
dem_am = 0
for i in range(n):
    if arr[i ] > 0:
        arr[i] = duong[dem_duong]
        dem_duong += 1
    elif arr[i] < 0:
        arr[i] = am[dem_am]
        dem_am += 1
print("List sau khi sắp xếp là:", arr)

