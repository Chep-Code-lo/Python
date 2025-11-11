dem_so_am = 0
while True:
    n = int(input())
    if n == 0:
        break
    if n < 0:
        dem_so_am += 1
print("Co", dem_so_am, "so am")