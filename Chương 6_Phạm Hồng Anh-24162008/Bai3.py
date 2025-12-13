class toan_hoc:
    def __init__(self, *n):
        self.n = n
    def tinh_tong(self):
        return sum(self.n)
    def tinh_trung_binh(self):
        return sum(self.n) / len(self.n)
    def tim_max(self):
        return max(self.n)
    def tim_min(self):
        return min(self.n)
    def hien_thi(self):
        print("Cac so da nhap:", self.n)