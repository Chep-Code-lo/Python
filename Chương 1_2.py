import math
a, b, c = map(int, input().split())
trung_binh = (a + b + c) / 3
print(math.floor(trung_binh * 10) / 10)
