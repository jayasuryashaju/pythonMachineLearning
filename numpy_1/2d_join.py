"""
when joining 2d matrices, it will join like column wise default.
to join row wise, we pass axis = 1.
matrix order must be the same.

"""

import numpy as np

a = np.array([[11, 2, 13], [4, 15, 9], [6, 11, 3]])
b = np.array([[1, 2, 4], [4, 15, 7], [12, 5, 3]])

c = np.concatenate((a, b))

print(c)
print(c.shape)