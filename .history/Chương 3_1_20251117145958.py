n = int(input())
list = []
sum = 0
for i in range(n):
    x = int(input())
    list.append(x)
for x in list:
    if x % 3 == 0:
        sum += x
print(sum)