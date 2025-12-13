from datetime import datetime

# --- GIỮ NGUYÊN CÁC LỚP CƠ BẢN ---
class GiaoDich:
    def __init__(self, ma_gd, ngay_gd, don_gia, so_luong):
        self.ma_gd, self.ngay_gd, self.don_gia, self.so_luong = ma_gd, ngay_gd, don_gia, so_luong
        self.thanh_tien = 0

    def nhap(self):
        self.ma_gd = input("Nhập mã giao dịch: ")
        self.ngay_gd = input("Nhập ngày giao dịch (dd/mm/yyyy): ")
        self.don_gia = float(input("Nhập đơn giá: "))
        self.so_luong = int(input("Nhập số lượng: "))

    def xuat(self):
        print(f"Mã: {self.ma_gd} | Ngày: {self.ngay_gd} | Đơn giá: {self.don_gia} | SL: {self.so_luong}", end=' | ')

class GiaoDichVang(GiaoDich):
    def __init__(self):
        super().__init__("", "", 0, 0)
        self.loai_vang = ""

    def nhap(self):
        print("--- Nhập Giao Dịch Vàng ---")
        super().nhap()
        self.loai_vang = input("Nhập loại vàng (18k/24k/9999): ")
        self.thanh_tien = self.so_luong * self.don_gia

    def xuat(self):
        super().xuat()
        print(f"Loại: {self.loai_vang} | Thành tiền: {self.thanh_tien:,.0f}")

class GiaoDichTienTe(GiaoDich):
    def __init__(self):
        super().__init__("", "", 0, 0)
        self.ty_gia = 0
        self.loai_tien = ""
        self.loai_gd = 0

    def nhap(self):
        print("--- Nhập Giao Dịch Tiền Tệ ---")
        super().nhap()
        self.loai_tien = input("Nhập loại tiền (USD/EUR/AUD): ")
        self.loai_gd = int(input("Nhập loại giao dịch (1: Mua, 2: Bán): "))
        if self.loai_gd == 1:
            self.thanh_tien = self.so_luong * self.don_gia
        else:
            self.thanh_tien = (self.so_luong * self.don_gia) * 1.05

    def xuat(self):
        trang_thai = "Mua" if self.loai_gd == 1 else "Bán"
        super().xuat()
        print(f"Tiền: {self.loai_tien} | Loại: {trang_thai} | Thành tiền: {self.thanh_tien:,.2f}")

# --- PHẦN MỚI: CLASS QUẢN LÝ (Xử lý câu d và e) ---
class QuanLyGiaoDich:
    def __init__(self):
        # Khởi tạo 2 danh sách riêng biệt để quản lý
        self.ds_vang = []
        self.ds_tien = []

    def them_gd_vang(self, gd_vang):
        self.ds_vang.append(gd_vang)

    def them_gd_tien(self, gd_tien):
        self.ds_tien.append(gd_tien)

    def xuat_danh_sach(self):
        print("\n--- DANH SÁCH GIAO DỊCH VÀNG ---")
        for gd in self.ds_vang:
            gd.xuat()
        
        print("\n--- DANH SÁCH GIAO DỊCH TIỀN TỆ ---")
        for gd in self.ds_tien:
            gd.xuat()

    # Xử lý câu d: Tính tổng số lượng
    def tinh_tong_so_luong(self):
        tong_sl_vang = sum(gd.so_luong for gd in self.ds_vang)
        tong_sl_tien = sum(gd.so_luong for gd in self.ds_tien)
        
        print(f"-> Tổng số lượng Vàng: {tong_sl_vang}")
        print(f"-> Tổng số lượng Tiền tệ: {tong_sl_tien}")

    # Xử lý câu e: Tính tổng thành tiền
    def tinh_tong_thanh_tien(self):
        tong_tien_vang = sum(gd.thanh_tien for gd in self.ds_vang)
        tong_tien_tien = sum(gd.thanh_tien for gd in self.ds_tien)
        
        print(f"-> Tổng thành tiền Vàng: {tong_tien_vang:,.0f} VNĐ")
        print(f"-> Tổng thành tiền Tiền tệ: {tong_tien_tien:,.2f} VNĐ")
        
    # Tính trung bình thành tiền của giao dịch tiền tệ (Mở rộng thêm)
    def tinh_trung_binh_tien_te(self):
        if len(self.ds_tien) == 0:
            print("Chưa có giao dịch tiền tệ nào.")
            return
        tong = sum(gd.thanh_tien for gd in self.ds_tien)
        trung_binh = tong / len(self.ds_tien)
        print(f"-> Trung bình thành tiền GD Tiền tệ: {trung_binh:,.2f} VNĐ")

# --- CHƯƠNG TRÌNH CHÍNH ---
def main():
    ql = QuanLyGiaoDich() # Khởi tạo đối tượng quản lý

    while True:
        print("\n--- MENU QUẢN LÝ ---")
        print("1. Nhập giao dịch Vàng")
        print("2. Nhập giao dịch Tiền tệ")
        print("3. Xuất danh sách")
        print("4. Tổng số lượng (Câu d)")
        print("5. Tổng thành tiền (Câu e)")
        print("6. Tính trung bình tiền tệ")
        print("0. Thoát")
        
        chon = int(input("Chọn chức năng: "))

        if chon == 1:
            gd = GiaoDichVang()
            gd.nhap()
            ql.them_gd_vang(gd) # Thêm vào class quản lý
        elif chon == 2:
            gd = GiaoDichTienTe()
            gd.nhap()
            ql.them_gd_tien(gd) # Thêm vào class quản lý
        elif chon == 3:
            ql.xuat_danh_sach()
        elif chon == 4:
            ql.tinh_tong_so_luong() # Gọi hàm xử lý câu d
        elif chon == 5:
            ql.tinh_tong_thanh_tien() # Gọi hàm xử lý câu e
        elif chon == 6:
            ql.tinh_trung_binh_tien_te()
        elif chon == 0:
            break
        else:
            print("Lựa chọn sai, vui lòng nhập lại!")

if __name__ == "__main__":
    main()