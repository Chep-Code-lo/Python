import numpy as np
n = 10
arr = np.random.uniform(-10, 10, size=n)
arr_0 = arr[arr > 0]
print(arr_0)