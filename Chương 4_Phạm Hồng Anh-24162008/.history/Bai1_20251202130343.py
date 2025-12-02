cost_co_so = 4.00
cost_meter = 0.25
def calc(n):
    return cost_co_so + n * cost_meter
n = int(input())
meter = n * 1000
so_luong = meter // 140
print(calc(so_luong))