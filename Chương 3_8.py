n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
new_arr = []
for x in arr:
    if(arr.count(x)==1):
        new_arr.append(x)
print(new_arr)