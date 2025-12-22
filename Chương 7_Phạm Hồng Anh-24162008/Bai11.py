import numpy as np

def product(mat_a, mat_b):
    a = np.array(mat_a)
    b = np.array(mat_b)

    if a.shape[1] == b.shape[0]:
        print("Tich ma tran:")
        print(a @ b)
    else:
        print("Khong co tich ma tran")

    if a.shape == b.shape:
        print("Tich Hadamard:")
        print(a * b)
    else:
        print("Khong co tich Hadamard")
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

product(A, B)
