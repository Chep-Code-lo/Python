a, b, c = map(float, input().split())
delattr = b**2 - 4*a*c
if delattr < 0:
    print("Phuong trinh vo nghiem")
elif delattr == 0:
    print(-b / (2*a))
else:
    print((-b + delattr**0.5) / (2*a), (-b - delattr**0.5) / (2*a))