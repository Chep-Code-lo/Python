n = int(input())

sum_a = 0.0
for i in range(1, n + 1):
    temp = 1 / (i * (i + 1))
    sum_a += temp

print(f"Tổng S(n) = 1/(1*2) + ... + 1/(n*(n+1)) là: {sum_a}")

sum_b = 0.0
for i in range(n + 1):
    tu = 2 * i + 1
    mau = 2 * i + 2
    term = tu / mau
    sum_b += term
    
print(f"Tổng S(n) = 1/2 + 3/4 + ... + (2n+1)/(2n+2) là: {sum_b}")