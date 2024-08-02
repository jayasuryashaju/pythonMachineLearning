"""
dropping row with missing value
dropna()
"""
"""
wrong format data == outliers

impossible values
eg: height of a person == 300cm which is not possible
"""


import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/jayas/OneDrive/Documents/missing_data.csv")

print(df)

print("*" * 100)

"""
df.dropna(inplace=True, ignore_index=True)
print(df)
"""

"""
df.dropna(subset=['Date'], inplace=True)
print(df)
"""


df.dropna(subset=['Date', 'Calories'], inplace=True, ignore_index=True)
print(df)