n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
if n == 0:
    print("Danh sách rỗng, không có giá trị lớn nhất/nhỏ nhất.")
else:
    lonnhat = arr[0]
    nhonhat = arr[0]
    for i in range(1, n):
        if arr[i] > lonnhat:
            lonnhat = arr[i]
        if arr[i] < nhonhat:
            nhonhat = arr[i]

    print("Giá trị lớn nhất trong list là:", lonnhat)
    print("Giá trị nhỏ nhất trong list là:", nhonhat)   