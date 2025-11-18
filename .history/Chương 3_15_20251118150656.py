n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
k = int(input())
if k == 0:
    print("k = 0 nên không kiểm tra ước / bội được")
else:
    uoc = []   
    boi = []   
    for x in arr:
        if x != 0 and k % x == 0:
            uoc.append(x)
        if x % k == 0:
            boi.append(x)
    print("Các ước số của", k, "trong list là:", uoc)
    print("Các bội số của", k, "trong list là:", boi)