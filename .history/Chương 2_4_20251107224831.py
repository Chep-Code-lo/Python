a, b, c = map(float, input().split())
phuong_trinh_bac_hai = b**2 - 4*a*c
if phuong_trinh_bac_hai < 0:
    print("Phuong trinh vo nghiem")
elif phuong_trinh_bac_hai == 0:
    print(-b / (2*a))
else:
    print((-b + phuong_trinh_bac_hai**0.5) / (2*a), (-b - phuong_trinh_bac_hai**0.5) / (2*a))