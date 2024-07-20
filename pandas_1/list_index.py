"""
head()
    head() function is used to print the first five elements by default.
    if we pass a value to the head() it will print that many elements from the list

tail()
    tail function is used to print last 5 elements by default
    if we pass a value to tail it will print that many elements
"""

import pandas as pd
import numpy as np

a = pd.Series([4, 5, 6, 7, 8, 9, 23, 43, 12, 65, 43, 87, 32, 98, 74, 53, 38, 76, 18, 24, 29, 31])
print(a.head())

print("*" * 100)

print(a.head(7))

print("*" * 100)

print(a.tail())

print("*" * 100)

print(a.tail(3))
