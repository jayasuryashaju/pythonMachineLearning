"""
name, roll no
roll, result
"""
import pandas as pd
import numpy as np
df_1 = pd.read_csv("C:/Users/jayas/OneDrive/Documents/student", header=None)
df_2 = pd.read_csv("C:/Users/jayas/OneDrive/Documents/results", header=None)

df_1.columns = ['name', 'roll_no']
df_2.columns = ['roll_no', 'result']
print(df_1)
print(df_2)

df_3 = pd.merge(df_2, df_1, on='roll_no', how='inner')

print(df_3.loc[df_3['result'] == 'pass'][['name', 'roll_no', 'result']])