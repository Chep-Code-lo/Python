def check_energy(energy):
    if energy < 10:
        return "Tiết kiệm"
    else:
        return "Tiêu hao nhiều"
def main():
    energy = float(input())
    print(check_energy(energy))

if __name__ == "__main__":
    main()