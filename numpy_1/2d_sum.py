import numpy as np

a = np.array([[1, 2, 3, 6], [4, 5, 6, 3], [7, 8, 9, 2], [2, 4, 7, 9]])

result = np.sum(a)
print(result)

"""
to get the sum of each row or column

axis = 0 columns
axis = 1 row

"""

b = np.sum(a, axis=0)
print(b)

