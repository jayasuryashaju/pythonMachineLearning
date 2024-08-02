"""
dtatatype check
missing value check
fill with mean, meadian , mode

"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/OneDrive/Documents/winequality-red.csv")
print(df)

print("*" * 100)

print(df.isna().sum())

print("*" * 100)

x = df['volatile acidity'].mean()

df['volatile acidity'].fillna(x, inplace=True)

y = df['residual sugar'].mean()

df['residual sugar'].fillna(y, inplace=True)

z = df['free sulfur dioxide'].mean()

df['free sulfur dioxide'].fillna(z, inplace=True)

a = df['density'].mean()

df['density'].fillna(a, inplace=True)

print(df.isna().sum())


