import math
class tam_giac:
    def __init__(self, a, b, c, mau):
        self.a, self.b, self.c, self.mau = a, b, c, mau
    def chu_vi(self):
        return self.a + self.b +self.c
    def dien_tich(self):
        p = self.chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
    def loai(self):
        a, b, c = sorted ([self.a, self.b, self.c])
        if a == b == c: return "Đều"
        if a*a + b*b == c*c: return "Vuông"
        if a*a + b*b == c*c and a == b or b == c: return "Vuông cân"
        if a == b or b == c or a == c: return "Cân"
        return "Thường"
    def hien_thi(self):
        print(f'Tam giác có các cạnh a={self.a}, b={self.b}, c={self.c}, màu {self.mau}')
        print(f'Chu vi: {self.chu_vi()}')
        print(f'Diện tích: {self.dien_tich()}')
        print(f'Loại tam giác: {self.loai()}')