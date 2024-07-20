
import pandas as pd
import numpy as np

a = pd.Series([87, 32, 98, 74, 53, 38, 76, 18, 24, 29, 31])
b = pd.Series([4, 5, 6, 7, 8, 9, 23, 43, 12, 65, 43])

c = a.add(b)
print(c)

print("*" * 100)

print(a.subtract(b))

print("*" * 100)

print(a.multiply(b))

print("*" * 100)

print(a.divide(b))