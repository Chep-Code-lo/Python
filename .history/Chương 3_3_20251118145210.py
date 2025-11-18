n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
print('Vị trí phần tử âm đầu tiên: ')
for i in range(n):
    if arr[i]<0 : 
        print(i)
        break