"""
searching through 2d matrix:

a = np.array([[1, 2, 3, 4], [5, 4, 7, 8], [4, 5, 6, 4], [6, 7, 8, 9]])
print(np.where(a == 4))


output:
    (array([0, 1, 2, 2]), array([3, 1, 0, 3])) ==> indexes => (0,3), (1, 1), (2, 0), (2, 3)

here the first array represents rows, the second array represents columns

"""


import numpy as np

a = np.array([[1, 2, 3, 4], [5, 4, 7, 8], [4, 5, 6, 4], [6, 7, 8, 9]])

print(np.where(a == 4))

print(np.where(a > 5))
b = np.where(a > 5)


