import numpy as np

a = np.array([[11, 2, 63, 4], [84, 5, 36, 97], [7, 68, 9, 95], [24, 95, 86, 57]])
b = np.array([[71, 32, 3, 14], [14, 95, 26, 57], [7, 28, 9, 55], [32, 56, 10, 1]])

print(a)

print("*" * 50)

# sorting the matrix using sort function

a = np.sort(a)  # sorting will happen row wise
print(a)

print("*" * 50)
a = np.sort(a, axis=0) # sorting based on columns
print(a)

