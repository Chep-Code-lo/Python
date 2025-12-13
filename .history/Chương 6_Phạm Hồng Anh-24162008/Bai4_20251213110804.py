import math
class diem:
    def __init__(self, x, y, mau):
        self.x, self.y, self.mau = x, y, mau
    def hien_thi(self):
        print(self.x, self.y, self.mau)
    def tinh_tien(self, dx, dy = 0):
        self.x += dx
        self.y += dy
    def tinh_khoang_cach(self, d = None):
        if d is None:
            return math.sqrt(self.x**2 + self.y**2)
        else:
            return math.sqrt((self.x - d.x)**2 + (self.y - d.y)**2)