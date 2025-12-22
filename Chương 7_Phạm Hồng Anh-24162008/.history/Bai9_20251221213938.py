import numpy as np

def broadcast(vec, n):
    vec = np.array(vec).reshape(-1, 1)   
    return np.repeat(vec, n, axis=1)   
print(broadcast([6, 7], 3))
# [[6 6 6]
#  [7 7 7]]

