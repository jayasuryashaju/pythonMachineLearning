"""
argsort()

agsort returns an array of indexes of the sorted array

"""

import numpy as np

a = np.array([1, 3, 1, 5, 4, 7, 4, 8, 5, 3, 9])

b = np.argsort(a)
print(b)
print(np.sort(a))

