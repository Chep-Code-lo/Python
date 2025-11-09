a, b = map(int, input().split())

a_chan = (a % 2 == 0)
b_chan = (b % 2 == 0)
if a_chan and b_chan:
    print("a va b la 2 so chan")
elif not a_chan and not b_chan:
    print("a, b la hai  so le")
else:
    print("chi co mot so chan")