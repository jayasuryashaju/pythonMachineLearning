"""
data cleaning
    1. how to handle missing value
    2. how to handle wrong format data

steps:
    calculate the number of missing values in each column => .isna().sum()
"""

import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/jayas/OneDrive/Documents/missing_data.csv")

print(df)

print("*" * 100)

print(df.isna().sum())

print("*" * 100)

df.fillna(300, inplace=True)

print(df.isna().sum())

