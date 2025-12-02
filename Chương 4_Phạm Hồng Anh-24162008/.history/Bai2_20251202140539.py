def median_of_three(a, b, c):
    return sorted([a, b, c])[1]

def main():
    x = float(input())
    y = float(input())
    z = float(input())
    result = median_of_three(x, y, z)
    print(result)
if __name__ == "__main__":
    main()