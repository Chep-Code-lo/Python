class MonHoc:
    def __init__(self, ma, ten, so_tiet):
        self.ma, self.ten, self.so_tiet = ma, ten, int(so_tiet)

class HocVien:
    def __init__(self, dinh_danh, ho_ten, nam_sinh, ds_mon):
        self.dinh_danh, self.ho_ten, self.nam_sinh = dinh_danh, ho_ten, int(nam_sinh)
        self.ds_mon = ds_mon  # list[MonHoc]

class QuanLyHocVien:
    def __init__(self, path="dssv.txt"):
        self.path = path
        self.ds = []

    # a) nhập + lưu file
    def nhap_va_luu_file(self):
        n = int(input("Số học viên: "))
        self.ds = []
        for _ in range(n):
            id_ = input("CMND/CCCD/Khai sinh: ")
            ten = input("Họ tên: ")
            ns = int(input("Năm sinh: "))
            m = int(input("Số môn đăng ký: "))
            ds_mon = []
            for _ in range(m):
                ma = input("  Mã môn: ")
                tenm = input("  Tên môn: ")
                sot = int(input("  Số tiết: "))
                ds_mon.append(MonHoc(ma, tenm, sot))
            self.ds.append(HocVien(id_, ten, ns, ds_mon))
        self.ghi_file()

    def ghi_file(self):
        with open(self.path, "w", encoding="utf-8") as f:
            for hv in self.ds:
                mon_str = ";".join([f"{m.ma},{m.ten},{m.so_tiet}" for m in hv.ds_mon])
                f.write(f"{hv.dinh_danh}|{hv.ho_ten}|{hv.nam_sinh}|{mon_str}\n")

    def doc_file(self):
        self.ds = []
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line: continue
                    id_, ten, ns, mon_str = line.split("|")
                    ds_mon = []
                    if mon_str:
                        for item in mon_str.split(";"):
                            ma, tenm, sot = item.split(",")
                            ds_mon.append(MonHoc(ma, tenm, int(sot)))
                    self.ds.append(HocVien(id_, ten, int(ns), ds_mon))
        except FileNotFoundError:
            pass

    # b) hiển thị tất cả
    def hien_thi_tat_ca(self):
        for hv in self.ds:
            print(hv.dinh_danh, hv.ho_ten, hv.nam_sinh,
                  [(m.ma, m.ten, m.so_tiet) for m in hv.ds_mon])

    # c) hv ít nhất 2 môn
    def hv_it_nhat_2_mon(self):
        for hv in self.ds:
            if len(hv.ds_mon) >= 2:
                print(hv.dinh_danh, hv.ho_ten)

    # d) môn nhiều hv đăng ký nhất
    def mon_nhieu_dk_nhat(self):
        dem = {}
        ten_mon = {}
        for hv in self.ds:
            for m in hv.ds_mon:
                dem[m.ma] = dem.get(m.ma, 0) + 1
                ten_mon[m.ma] = m.ten
        if not dem:
            print("Không có dữ liệu.")
            return
        ma_max = max(dem, key=dem.get)
        print("Môn đăng ký nhiều nhất:", ma_max, ten_mon[ma_max], "=", dem[ma_max], "học viên")

    # e) thống kê số hv trên mỗi môn
    def thong_ke_moi_mon(self):
        dem = {}
        for hv in self.ds:
            for m in hv.ds_mon:
                dem[m.ma] = dem.get(m.ma, 0) + 1
        for ma, sl in dem.items():
            print(ma, ":", sl)
