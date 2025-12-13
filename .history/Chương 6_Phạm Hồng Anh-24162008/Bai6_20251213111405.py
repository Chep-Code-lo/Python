class hoc_vien:
    def __init__(self, id, ten, nam_sinh, mon):
        self.id, self.ten, self.nam_sinh, self.mon = id, ten, nam_sinh, mon
class quan_ly_hoc_vien:
    def __init__(self):
        self.ds = []
    def them(self, hv):
        self.ds.append(hv)
    def hien_thi(self):
        for hv in self.ds:
            print(hv.id, hv.ten, hv.nam_sinh, hv.mon)
    def hv_it_nhat_2_mon(self):
        return [hv for hv in self.ds if len(hv.mon) >= 2]