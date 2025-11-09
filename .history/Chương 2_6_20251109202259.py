a, b, c, d, e = map(float, input().split())

max_val = a

if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
if d > max_val:
    max_val = d
if e > max_val:
    max_val = e

min_val = a

if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
if d < min_val:
    min_val = d
if e < min_val:
    min_val = e
print(max_val, min_val)