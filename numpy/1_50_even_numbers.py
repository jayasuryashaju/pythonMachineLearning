"""
1 to 50 even numbers 5 by 5
"""

import numpy as np

a = np.arange(1, 51)
print(a)

b = a % 2 == 0
c = a[b]

print(c)

d = np.reshape(c, (5, 5))

print(d)

print("*" * 100)

print(np.arange(2, 51, 2).reshape(5, 5))
