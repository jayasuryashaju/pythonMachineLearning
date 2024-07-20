"""
if all the elements is matrix is zeroes, it is called a zero matrix
"""

import numpy as np

# a = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
a = np.zeros([5, 6], dtype=int)
print(a)
print(type(a))
print(a.ndim)
print(a.shape)
