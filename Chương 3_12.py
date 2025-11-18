n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
chan = []     
le = []
vi_tri_chan = []
vi_tri_le = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        chan.append(arr[i])
        vi_tri_chan.append(i)
    else:
        le.append(arr[i])
        vi_tri_le.append(i)
chan.sort()
le.sort()
le.reverse()
for i in range(len(chan)):
    arr[vi_tri_chan[i]] = chan[i]
for i in range(len(le)):
    arr[vi_tri_le[i]] = le[i]
print("List sau khi sắp xếp là:", arr)