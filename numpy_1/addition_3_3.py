"""
the order of the matrices should be the same.
"""

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[8, 2, 9], [4, 4, 2], [9, 8, 3]])

# addition

result = np.add(a, b)
print(result)

# subtraction

result = np.subtract(a, b)
print(result)

# multiplication

result = np.multiply(a, b)
print(result)

# division

result = np.divide(a, b)
print(result)

# square of all elements

result = np.square(a)
print(result)

# square root

result = np.sqrt(a)
print(result.round(2))