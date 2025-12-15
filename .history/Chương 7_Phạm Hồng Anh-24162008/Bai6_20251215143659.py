import numpy as np
a = float(input())
b = float(input())
arr = a + (b - a)*np.random.rand(10)
print(arr)