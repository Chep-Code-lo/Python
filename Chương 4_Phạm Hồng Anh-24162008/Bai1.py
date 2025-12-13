def calc(n):
    cost_co_so = 4.00
    cost_meter = 0.25
    return cost_co_so + n * cost_meter
def main():
    n = int(input())
    meter = n * 1000
    so_luong = meter / 140
    print(calc(so_luong))
if __name__ == "__main__":
    main()