"""
1. age > 22 fname, lname, age, phno.

2. age == 23 fname, lname, age

3. chennai work => fname, lname, age, ph

4. chennai work and age above 23 => fname, lname, age, ph

"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/sample4.txt", header=None)
df.columns = ["id", "fname", "lname", "age", "ph", "loc"]

print(df)

print("*" * 100)
print(1)
print(df.loc[df["age"] > 22][["fname", "lname", "age", "ph"]])
print("*" * 100)
print(2)
print(df.loc[df["age"] == 23][["fname", "lname", "age"]])
print("*" * 100)
print(3)
print(df.loc[df["loc"] == "Chennai"][["fname", "lname", "age", "ph"]])
print("*" * 100)
print(4)
print(df.loc[(df["loc"] == "Chennai") & (df["age"] > 23)][["fname", "lname", "age", "ph"]])
