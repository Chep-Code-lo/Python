class giao_dich:
    def __init__(self, ma, ngay, gia, sl):
        self.ma, self.ngay, self.gia, self.sl = ma, ngay, gia, sl
class giao_dich_vang(giao_dich):
    def thanh_tien(self):
        return self.gia * self.sl
class giao_dich_tien_te(giao_dich):
    def __init__(self, ma, ngay, tygia, sl, loai):
        super().__init__(ma, ngay, tygia, sl)
        self.loai = loai
    def thanh_tien(self):
        if self.loai == "mua":
            return self.sl *self.gia
        return self.sl * self.gia * 1.05