n = int(input())

chinh_phuong = n ** 0.5
if chinh_phuong == int(chinh_phuong):
    print("YES")
else:
    chinh_phuong = int(chinh_phuong) + 1
    print(chinh_phuong * chinh_phuong)