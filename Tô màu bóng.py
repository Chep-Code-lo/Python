import math
n = int(input())
a = int(input())
b = int(input())   
do = n // a
xanh = n // b
do_xanh = n // (math.lcm(a, b))
print(n - (do + xanh - do_xanh))