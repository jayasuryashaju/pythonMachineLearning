"""
joining 1d matrices,
    to join two matrices we use concatenate()
syntax:
    new_matrix = np.concatenate((matrix_1, matrix_2))

"""

import numpy as np

a = np.array([4, 23, 2, 4, 6])
b = np.array([4, 87, 76, 55, 4])

c = np.concatenate((a, b))
print(c)
