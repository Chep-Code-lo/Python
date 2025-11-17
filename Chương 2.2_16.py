q = int(input())

result = ""
if q == 0:
    result = "0"
else:
    while q > 0:
        r = q % 2
        result = str(r) + result
        q = q // 2

print(result)