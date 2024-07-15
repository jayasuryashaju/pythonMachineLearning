import numpy as np

a = np.array([4, 23, 2, 4, 6, 78, 67, 87, 76, 55, 4, 43])

print(a)

print("*" * 100)

print(np.min(a))

b = np.array([[11, 2, 13], [4, 15, 26], [27, 18, 39]])
print(np.min(b))
print(np.argmin(b))
print(np.argmin(b, axis=0))
print(np.argmin(b, axis=1))