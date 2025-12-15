import numpy as np
sales = np.random.randint(0, 51, size=(2,7))

maxx = -1
day_max = -1
for day in range(7):
    total = sales[0][day] + sales[1][day]
    if total > maxx:
        maxx = total
        day_max = day

session_max = -1
day_max_b = -1
total_max = -1
for x in range(2):
    for y in range(7):
        if sales[x][y] > total_max:
            total_max = sales[x][y]
            session_max = x
            day_max_b = y
if session_max == 0:
    session = "Sáng"
else:
    session = "Chiều"
print("Thời điểm bán được nhiều nhất vào buổi " , session, "ngày", day_max_b)

morning_better = 0
afternoon_better = 0
for day in range(7):
    if sales[0][day] > sales[1][day]:
        morning_better += 1
    elif sales[0][day] < sales[1][day]:
        afternoon_better += 1
if morning_better > afternoon_better:
    print("Buổi sáng bán nhiều hơn")
elif afternoon_better > morning_better:
    print("Buổi chiều bán nhiều hơn")
else:
    print("Hai buổi bán tương đương nhau")
