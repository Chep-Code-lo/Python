from abc import ABC, abstractmethod
import math

class HinhHoc(ABC):
    @abstractmethod
    def tinh_dien_tich(self):
        pass
    @abstractmethod
    def tinh_chu_vi(self):
        pass
class Hinh_tron(HinhHoc):
    def __init__(self, r):
        self.r = r
    def chu_vi(self):
        return 2 * math.pi * self.r
    def dien_tich(self):
        return math.pi * self.r ** 2
class Hinh_chu_nhat(HinhHoc):
    def __init__(self, d, r):
        self.d = d
        self.r = r
    def chu_vi(self):
        return 2 * (self.d + self.r)
    def dien_tich(self):
        return self.d * self.r
