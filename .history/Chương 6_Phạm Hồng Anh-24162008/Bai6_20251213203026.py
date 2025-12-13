class hoc_vien:
    def __init__(self, dinh_danh, ten, nam_sinh, ds_mon):
        self.dinh_danh, self.ten, self.nam_sinh, self.ds_mon = dinh_danh, ten, int(nam_sinh), ds_mon
class mon_hoc:
    def __init__(self, ma, ten_mon, so_tiet):
        self.ma, self.ten_mon, self.so_tiet = ma, ten_mon, int(so_tiet)
class quan_ly:
    def __init__(self, path = "dssv.txt"):
        self.path = path
        self.ds = []
    def nhap_va_luu(self):
         

