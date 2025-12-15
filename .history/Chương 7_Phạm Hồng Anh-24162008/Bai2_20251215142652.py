import numpy as np
n = 10
arr = np.random.uniform(-10, 10, size=n)
for x in arr:
    if x > 0:
        print(x)