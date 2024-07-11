"""
if we want to change the matrix to a one-dimension matrix, we use flatten
"""

import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [4, 5, 6, 7], [6, 7, 8, 9]])

print("1d")
print(a.reshape([16]))

print('3d')
print(a.reshape([2, 2, 4]))

print(a.flatten())