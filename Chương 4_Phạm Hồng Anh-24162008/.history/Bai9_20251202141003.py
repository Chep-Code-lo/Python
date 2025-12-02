from Bai8 import calc_star
def check_energy(energy):
    star = calc_star(energy)
    if star < 3:
        return "Không tiết kiệm"
    else:
        return "Tiết kiệm"
def main():
    energy = float(input())
    print(check_energy(energy))
if __name__ == "__main__":
    main()