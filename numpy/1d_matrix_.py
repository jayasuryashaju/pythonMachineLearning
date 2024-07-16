"""
splitting array into

"""


import numpy as np

a = np.array([5, 1, 3, 0, 3, 8, 9, 4, 7, 2, 6])
print(a)
print(np.array_split(a, 3))
print(np.array_split(a, 3)[0])

