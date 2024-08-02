"""
1. age max 2 employees => fname,lname,age,ph

2. age min 1 employee fname, lname, age, ph

3. chennai work, age max 1 emp fname, lname, age, ph
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/sample4.txt", header=None)
df.columns = ["id", "fname", "lname", "age", "ph", "loc"]
# print(df)

print(df.sort_values(by="age", ascending=False)[['fname', 'lname', 'age', 'ph']].head(2))

print("*" * 100)

print(df.sort_values(by="age")[['fname', 'lname', 'age', 'ph']].head(1))

print("*" * 100)

print(df.loc[df['loc'] == "Chennai"].sort_values(by="age", ascending=False) \
          [['fname', 'lname', 'age', 'ph']].head(1))
