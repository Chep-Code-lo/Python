n = int(input())
m = int(input())
s = []
for i in range(m):
    x = int(input())
    s.append(x)
f = [0] * (n + 1)
f[0] = 1
for coin in s:
    for v in range(coin, n + 1):
        f[v] = f[v] + f[v - coin]
print("số cách đổi", n , "xu là:", f[n])
