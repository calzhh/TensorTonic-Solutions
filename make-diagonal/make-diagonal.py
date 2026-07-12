import numpy as np

def make_diagonal(v):
    A = np.zeros((len(v), len(v)))
    print(A)
    N, M = A.shape
    for i in range(N):
        A[i, i] = v[i]

    return A