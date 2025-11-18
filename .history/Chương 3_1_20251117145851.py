n = int(input())
list = []
sum = 0
for i in range(n):
    x = int(input())
    list.append(x)
for i in range(1, n):
    if list[i] % 3 == 0:
        sum += list[i]
print(sum)