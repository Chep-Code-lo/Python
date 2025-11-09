a, b, c = map(int, input().split())

if a % 2 == 0:
    max_chan = a
if b % 2 == 0 and b > max_chan:
    max_chan = b
if c % 2 == 0 and c > max_chan:
    max_chan = c
if max_chan == float('-inf'):
    print("KHONG co so chan")
else:
    print(max_chan)