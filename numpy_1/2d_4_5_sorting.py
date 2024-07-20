import numpy as np

a = np.array([[1, 2, 3, 5, 6], [4, 5, 6, 2, 1], [7, 8, 9, 5, 8], [1, 4, 7, 7, 5]])
print(a)

"""
slicing 2d matrix
syntax:
    s[row, column]

"""
print(a[1, 3])
print(a[2, 2])
print(a[1:, :2])  # row = 1, 2, 3 and column = 0, 1

print(a[1:3, 1:4])  # row = 1, 2 and column = 2, 3

print(a[:2, :3])  # row = 0, 1 and column = 0, 1, 2

print(a[1::2, 2::2])  # row = 1,3 and column = 2, 4

print(a[::2, 1::3])  # row = 0, 2 and column = 1, 4

print("*" * 50)

print(a[0])
print(a[:, 0])
