"""
all the elements in the matrix are ones

[1 1 1]
[1 1 1]
[1 1 1]
"""
import numpy as np

a = np.ones([3, 3], dtype=int)
print(a)
print(a.ndim)
print(a.shape)

b = np.ones([6], dtype=int)
print(b)

c = np.ones([1, 3, 3], dtype=int)
print(c)
print(c.ndim)
print(c.shape)
