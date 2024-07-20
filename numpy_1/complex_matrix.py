"""
complex matrix:
    a + ib
    x + iy
    real part and imaginary part (a,x are real parts and ib, iy are imaginary parts)

"""

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=complex)
print(a)

b = np.array([[1 + 2j, 2 + 4j], [3 + 5j, 2 + 9j], [5 + 9j, 2 + 3j], [9 + 1j, 2 + 8j]])
print(b)

print([[i, j, k] for i in range(1, 3) for j in range(1, 3) for k in range(1, 3)])
