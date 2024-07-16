import numpy as np

a = np.array([4, 23, 2, 4, 6, 78, 67, 87, 76, 55, 4, 43])

b = np.where(a == 4)
print(b)

print(np.where(a < 10))

print(np.where(a % 2 == 0))

