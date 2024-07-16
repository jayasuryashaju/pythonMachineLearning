"""
1 to 50

div by 5

3d 2_5
"""

import numpy as np

a = np.arange(1, 51)
print(a)
print("*" * 100)

b = a % 5 == 0
b = a[b]
print(b)
print("*" * 100)


c = np.reshape(b, (1, 2, 5))
print(c)
