"""
filter is used to get elements that satisfy a condition in an array


"""

import numpy as np

a = np.array([5, 1, 3, 0, 3, 8, 9, 4, 7, 2, 6])
print(a)

b = a > 3

print(b)

c = a[b]

print(c)