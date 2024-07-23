"""
sorting a df:
we use sort_values() function.

eg:
    df.sort(by="column_name')
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/customer1.txt", header=None)
df.columns = ["id", "fname", "lname", "age", "ph", "loc"]


df_1 = df.sort_values(by="age", ascending=False)
print(df_1)