n = int(input())
arr_1 = []
for i in range(n):
    x = int(input())
    arr_1.append(x)
arr_2 = []
for x in arr_1:
    if x < 0:
        arr_2.append(x)
arr_2.sort()
arr_2.reverse()
idx = 0
for i in range(len(arr_1)):
    if arr_1[i] < 0:
        arr_1[i] = arr_2[idx]
        idx += 1
print('List sau khi sắp xếp các phần tử âm giảm dần là:', arr_1)