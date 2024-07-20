"""
normal sort works in row wisely.
argsort also normally works in row.




"""

import numpy as np

a = np.array([[11, 2, 13], [4, 15, 26], [27, 18, 39]])
print(a)

print("*" * 100)

print(np.sort(a))

print("*" * 100)

print(np.argsort(a))

print("*" * 100)

print(np.argsort(a, axis=0))

print("*" * 100)

print(np.max(a))