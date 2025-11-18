n = int(input())
list = []
sum = 0
count = 0
for i in range(n):
    x = int(input())
    list.append(x)
for i in list:
    if i > 0:
        sum += i
        count += 1
print(float(sum / count))