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
class QuanLyGiaoDich:
    def __init__(self):
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
    def tinh_tong_so_luong(self):
        tong_sl_vang = sum(gd.so_luong for gd in self.ds_vang)
        tong_sl_tien = sum(gd.so_luong for gd in self.ds_tien)
        
        print(f"Tổng số lượng Vàng: {tong_sl_vang}")
        print(f"Tổng số lượng Tiền tệ: {tong_sl_tien}")

    def tinh_tong_thanh_tien(self):
        tong_tien_vang = sum(gd.thanh_tien for gd in self.ds_vang)
        tong_tien_tien = sum(gd.thanh_tien for gd in self.ds_tien)
        
        print(f"Tổng thành tiền Vàng: {tong_tien_vang:,.0f} VNĐ")
        print(f"Tổng thành tiền Tiền tệ: {tong_tien_tien:,.2f} VNĐ")