n = int(input())
arr=[]
for i in range(n):
    x = int(input())
    arr.append(x)
k = int(input())
dem = 0     
vitri = -1  
for i in range(n):
    if arr[i] < 0:
        dem += 1
        if dem == k:
            vitri = i    
            break
if vitri == -1:
    print('Không có phần tử âm thứ',k,' trong danh sách')
else:
    print('Vị trí phần tử âm thứ ',k,' là: ',vitri)