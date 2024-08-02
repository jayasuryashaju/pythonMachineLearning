"""
to calculate the maximum with respect to a column.
    eg: the max salary of any each profession.
syntax:
    new_df = old_df.groupby("col_name")["col_name"].max()
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/customer1.txt", header=None)
df.columns = ["id", "fname", "lname", "age", "prof", "location"]

df_1 = df.groupby("prof")["age"].max().sort_values(ascending=False)
print(df_1)