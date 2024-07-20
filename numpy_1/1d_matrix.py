import numpy as np

a = np.array([4, 23, 2, 4, 6, 78, 67, 87, 76, 55, 4, 43])

print(a)
for i in a:
    print(i)

b = np.array([[11, 2, 13], [4, 15, 26], [27, 18, 39]])

print("*" * 100)

for i in b:
    for j in i:
        print(j)