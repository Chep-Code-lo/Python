while True:
    n = int(input())
    if n > 0 and n < 8:
        break
    else:
        print("Nhap lai n(1-7)")
if n == 1:
    print("Sunday")
elif n == 2:
    print("Monday")
elif n == 3:
    print("Tuesday")
elif n == 4:
    print("Wednesday")
elif n == 5:
    print("Thursday")
elif n == 6:
    print("Friday")
else:
    print("Saturday")