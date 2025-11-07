import math
a, b, c = map(int, input().split())
average = (a + b + c) / 3
print(math.floor(average * 10) / 10)
