"""
 prof, id, fname, lname, age, salary
"""

import numpy as np
import pandas as pd

t = ("hello", "world", "happy", "face")
a = pd.Series(data=t)
print(a)

print("*" * 100)

dic = {"id": 120, "fname": " Jayasurya", "lname": "Shaju", "age": 23, "prof": "Data Engineer", "salary": 23000}
print(dic)

print("*" * 100)

b = pd.Series(data=dic.values(), index=dic.keys(), name=dic["fname"])
print(b)

print("*" * 100)

c = pd.Series(dic)
print(c)
