import numpy as np

def replace_col(mat, col_ind):
    mat = np.array(mat)     
    mat[:, col_ind] = 1      
    return mat
A = np.array([
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10]
])
print(replace_col(A, 1))
