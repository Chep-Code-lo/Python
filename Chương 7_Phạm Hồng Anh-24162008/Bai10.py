import numpy as np

def transpose(mat):
    return mat.T
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(transpose(A))
