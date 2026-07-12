import numpy as np

def matrix_transpose(A):
    A = np.asarray(A)
    N, M = A.shape
    B = np.empty((M, N), dtype=A.dtype)

    for i in range(N):
        B[:, i] = A[i, :]

    return B