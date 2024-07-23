"""
filter:
    the function loc() can be used to filter the data
    new_df = old_df.loc[df["column_name"] condition]
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/customer1.txt", header=None)
df.columns = ["id", "fname", "lname", "age", "prof", "location"]

# print(df.loc[lambda x: x.index % 2 == 0])
#
# print(df.loc[df["age"] > 70])
#
# print(df.loc[df['age'] < 30][['fname', 'lname', 'age', 'prof']])

print(df.loc[(df['location'] == 'india') & (df['age'] < 30)][['fname', 'lname', 'age', 'prof']])
