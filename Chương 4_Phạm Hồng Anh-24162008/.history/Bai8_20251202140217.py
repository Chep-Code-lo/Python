def calc_star(n):
    if n < 2:
        return 5
    elif 2 <= n < 4:
        return 4
    elif 4 <= n < 6:
        return 3
    elif 6 <= n < 10:
        return 2
    else:
        return 1
def main():
    n = int(input())
    print(calc_star(n))
if __name__ == "__main__":
    main()