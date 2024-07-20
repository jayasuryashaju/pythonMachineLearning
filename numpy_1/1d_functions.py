"""
axis = 1 = row
axis = 0 = column
"""

import numpy as np

a = np.array([3, 8, 3, 12, 5, 6])

b = np.array([[4, 3, 5], [1, 3, 7], [2, 1, 7]])

print(np.max(a))

print(np.max(b))

print(np.max(b, axis=0))
print(np.max(b, axis=1))

print("*" * 50)

print(np.min(a))
print(np.min(b, axis=0))
print(np.min(b, axis=1))

print("desc sorting")

a = np.sort(a)
print(a[::-1])
b = np.sort(b, axis=0)
print(b)
print(b[:, ::-1])

print("*" * 50)
b = np.sort(b, axis=1)
print(b)
print(b[::-1, :])

