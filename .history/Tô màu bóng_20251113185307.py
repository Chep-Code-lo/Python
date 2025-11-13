import math
n, a, b = map(int, input().split())
do = n // a
xanh = n // b
do_xanh = n // (math.lcm(a, b))
print(n - (do + xanh - do_xanh))