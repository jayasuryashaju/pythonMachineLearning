"""
round | floor | ceil

[[1.1 3.3 7.7 2.3]
 [9.4 1.2 6.5 3.9]
 [1.3 5.6 7.3 8.9]
 [2.7 4.4 3.2 8.4]]

floor:
    discard decimal points
    np.floor(array)
    datatype can't be changed

ceil
    it will convert all the decimal points to the highest integer point.
    3.1 => 4
    5.7 => 6

round
    it will convert all the decimal points up to 5 to the lowest integer, and all the decimal points above 5 will be
     converted to the highest integer point.
     if .5 is the decimal point and the number is even, it will be converted the lowest integer
     else .5 is the decimal, and the number is odd, it will convert to the highest integer

     3.1 => 3
     4.5 => 4
     5.5 => 6
     2.7 => 3

"""

import numpy as np

a = np.array([[1.1, 3.3, 7.7, 2.3], [9.4, 1.2, 6.5, 3.9], [1.3, 5.6, 7.3, 8.9], [2.7, 4.4, 3.2, 8.4]])
print(a)
print("*" * 100)


b = np.floor(a)
print(b)

print("*" * 100)

c = np.ceil(a)
print(c)

print("*" * 100)


d = np.round(a)
print(d)

print("*" * 100)
