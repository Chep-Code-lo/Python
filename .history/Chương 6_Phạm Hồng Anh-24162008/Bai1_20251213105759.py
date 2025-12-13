import math

class hinh_tron:
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh

    def chu_vi(self):
        return 2 * math.pi * self.ban_kinh

    def dien_tich(self):
        return math.pi * (self.ban_kinh ** 2)
    def hien_thi_thong_tin(self):
        print(f"Hình tròn có bán kính: {self.ban_kinh}")
        print(f"Chu vi: {self.chu_vi()}")
        print(f"Diện tích: {self.dien_tich()}")