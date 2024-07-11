"""
3 X 4
when changing the order of a matrix, the size or the number of elements should be the same.
"""

import numpy as np

a = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 5]])

print(a)
print("*" * 25)
print(a.reshape([4, 3]))
print("*" * 25)
print(a.reshape([3, 3]))  # this returns an error

print(a.shape)
