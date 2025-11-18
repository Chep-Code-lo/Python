n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
c = []
l = []
for i in range(n):
    if arr[i] % 2 == 0:
        c.append(arr[i])   
    else:
        l.append(arr[i]) 
print('Danh sách phần tử chẵn là: ',c)
print('Danh sách phần tử lẻ là: ',l)
