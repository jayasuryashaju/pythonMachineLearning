"""
[1 2 3 ]  DOT [5 6 7 ]      [1*5 + 2*1 + 3*4]
[4 5 6 ]      [1 3 6]   =   [4*6 + 5*3 + 6*1]
[7 8 9]       [4 1 6]       [7*7 + 8*6 + 9*6]

"""

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
d = np.array([[13, 2, 33], [42, 5, 64], [47, 28, 95]])

result = np.add(a, b)
print(result)

# dot product

result = np.dot(a, b)
print(result)

result = np.dot(c, d)
print(result)
