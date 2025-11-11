n = int(input())

def kiem_tra_chinh_phuong(n):
    if n < 0:
        print(0)
    i = 0
    while True:
        chinh_phuong = i * i
        if chinh_phuong == n:
            print("YES")
        else:
            chinh_phuong_truoc = (i - 1) * (i - 1)
            chinh_phuong_sau = chinh_phuong
            khoang_cach_truoc = n - chinh_phuong_truoc
            khoang_cach_sau = chinh_phuong_sau - n
            if khoang_cach_truoc < khoang_cach_sau:
                print(chinh_phuong_truoc)
            else:
                print(chinh_phuong_sau)
            break
        i += 1
kiem_tra_chinh_phuong(n)