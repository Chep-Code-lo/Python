n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
nguyen_to = [] 
for x in arr:
    if x >= 2:     
        dem = 0
        for j in range(1, x+1):
            if x % j == 0:
                dem = dem + 1
        if dem == 2:
            nguyen_to.append(x)
print("Danh sách các số nguyên tố là:", nguyen_to)
    