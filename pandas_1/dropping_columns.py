"""
dropping non-needed columns form a data set

function => drop()

syntax:
    df.drop(['column_name'], axis=1)
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/sample4.txt", header=None)
df.columns = ["id", "fname", "lname", "age", "ph", "loc"]


print(df)

print("*" * 100)

print(df.drop(["ph"], axis=1))

