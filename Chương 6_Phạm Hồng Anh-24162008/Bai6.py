class hoc_vien:
    def __init__(self, dinh_danh, ho_ten, nam_sinh, ds_mon):
        self.dinh_danh, self.ten, self.nam_sinh, self.ds_mon = dinh_danh, ho_ten, int(nam_sinh), ds_mon
class mon_hoc:
    def __init__(self, ma, ten_mon, so_tiet):
        self.ma, self.ten_mon, self.so_tiet = ma, ten_mon, int(so_tiet)
class quan_ly:
    def __init__(self, path = "dssv.txt"):
        self.path = path
        self.ds = []
    def nhap_va_luu(self):
        self.ds = []
        n = int(input("Số học viên: "))
        for _ in range(n):
            id_ = input("CMND/CCCD/khai sinh: ")
            ten = input("Họ tên: ") 
            ns = input("Năm sinh: ")
            m = int(input("Số môn đăng kí: "))
            ds_mon = []
            for _ in range(m):
                ma = input("Mã môn: ")
                tenm = input("Tên môn: ")
                tiet = int(input("Số tiết: "))
                ds_mon.append(mon_hoc(ma, tenm, tiet))
            self.ds.append(hoc_vien(id_, ten, ns, ds_mon))
        self.ghi_file()
    def ghi_file(self):
        with open(self.path, "w", encoding = "utf-8") as f:
            for hv in self.ds:
                mon_str = ";".join([f"{m.ma}, {m.ten_mon}, {m.so_tiet}" for m in hv.ds_mon])
                f.write(f"{hv.dinh_danh}| {hv.ho_ten}| {hv.nam_sinh}| {mon_str}\n")
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
                            ma, tenm, tiet = item.split(",")
                            ds_mon.append(mon_hoc(ma, tenm, int(tiet)))
                    self.ds.append(hoc_vien(id_, ten, int(ns), ds_mon))
        except FileNotFoundError:
            pass
    def hien_thi(self):
        for hv in self.ds:
            print(hv.dinh_danh, hv.ho_ten, hv.nam_sinh, [(m.ma, m.ten, m.tiet) for m in hv.ds_mon])
    def hv_min_2(self):
        for hv in self.ds:
            if len(hv.ds_mon) >= 2:
                print(hv.dinh_danh, hv.ho_ten)
    def mon_max(self):
        dem = {}
        ten_mon = {}
        for hv in self.ds:
            for m in hv.ds_mon:
                dem[m.ma] = dem.get(m.ma, 0) + 1
                ten_mon[m.ma] = m.ten
        if not dem:
            print("Không có dữ liệu")
            return
        mmax = max(dem, key=dem.get)
        print("Môn đăng ký nhiều : ", mmax, ten_mon[mmax], "=", dem[mmax], "học viên")
    def thong_ke(self):
        dem = {}
        for hv in self.ds:
            for m in hv.ds_mon:
                dem[m.ma] = dem.get(m.ma, 0) + 1
        for ma, sl in dem.items():
            print(ma, ":", sl)