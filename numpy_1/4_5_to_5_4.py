"""
4 x 4
1. 5 x 4
2. 1D
3. 3D (2, 10)

"""
import numpy as np

a = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [6, 5, 3, 2, 6], [8, 4, 9, 2, 1]], dtype=int)
print(a)
print("*" * 30)
print("5 x 4")
print(a.reshape([5, 4]))
print("*" * 30)
print("1 D")
print(a.reshape([20]))
print("*" * 30)
print("3 D")
print(a.reshape([1, 2, 10]))
