n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
k = int(input())
newarr = []
for x in arr:
    if x != k:
        newarr.append(x)
print(newarr)