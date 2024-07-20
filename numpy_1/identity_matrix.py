"""
identity matrix:
    all the diagonal elements are ones, and all the other elements are zeros, and it must be a square matrix too.
    [[1, 0, 0]
    [0, 1, 0]
    [0, 0, 1]]
"""
import numpy as np

a = np.identity(5, dtype=int)
print(a)

b = np.identity(3, dtype=int)
print(b)

c = np.eye(3, dtype=int)
print(c)

