"""
finding the total number of missing value:
    isna().sum() function can be used

eg:
    df.isna().sum()


filling missing value using fillna() function

eg:
    df.fillna("value")

"""


import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/customer1.txt", header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'profession', 'location']

print(df.isna().sum())

# print(df.fillna("india").isna().sum())

df_1 = df.fillna("india")

print(df_1.isna().sum())
