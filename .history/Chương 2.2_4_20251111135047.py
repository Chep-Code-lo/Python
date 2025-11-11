while True:
    ly_thuyet = float(input())
    if(ly_thuyet >= 0 and ly_thuyet <= 10):
        break
    else:
        print("Nhap lai diem ly thuyet (0-10)")
while True:
    thuc_hanh = float(input())
    if(thuc_hanh >= 0 and thuc_hanh <= 10):
        break
    else:
        print("Nhap lai diem thuc hanh (0-10)") 
trung_binh = (ly_thuyet + thuc_hanh) / 2
print(trung_binh)