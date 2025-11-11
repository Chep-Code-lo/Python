n = int(input())

so_chan = 0
so_le = 0
while n > 0:
    chu_so = n % 10
    if chu_so % 2 == 0:
        so_chan += 1
    else:
        so_le += 1
    n //= 10
print(so_chan, so_le)

