def next_prime(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1
def main():
    n = int(input())
    print(next_prime(n))
if __name__ == "__main__":
    main()