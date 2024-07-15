import numpy as np

a = np.array([4, 23, 2, 4, 6, 78, 67, 87, 76, 55, 4, 43])

print(a)

print("*" * 100)

print(np.max(a))

b = np.array([[11, 2, 13], [4, 15, 26], [27, 18, 39]])
print(np.max(b))
print(np.argmax(b))
print(np.argmax(b, axis=0))