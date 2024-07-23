"""
printing rows b/w a certain range

iloc() function can be used
eg:
    df_1 = df.iloc[3]  ==> which will give an output of the third index row.

"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/customer1.txt", header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'profession', 'location']
df_1 = df.iloc[3]
print(df_1)

print("*" * 100)

print(df.iloc[50:70:2])

print("*" * 100)

print(df.iloc[20:25, :3])

print("*" * 100)

# 5 to 20 rows, fname, lname, prof, loc

print(df.iloc[4:20, 1:])

# print(df.iloc[:, lambda x: x.index % 2 == 0])