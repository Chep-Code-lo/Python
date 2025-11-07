don_gia = input("Nhap vao don gia: ")
so_luong = input("Nhap vao so luong: ")
tong_tien_truoc_thue = int(don_gia) * int(so_luong)
tien_thue = tong_tien_truoc_thue * 0.1
tong_tien_sau_thue = tong_tien_truoc_thue + tien_thue
print("Tong tien truoc thue: ", don_gia, "*", so_luong, "=", tong_tien_truoc_thue)
print("Tien thue la: ", int(tien_thue))
print("Tong tien sau thue la: ", int(tong_tien_sau_thue))
