"""
we use mean(), median(), mode() functions to fill values properly.

if missing values are integers, we can use mean() or median()
else if missing values are objects either we can drop the column,
fill value manually or we can use mode().

"""

import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/jayas/OneDrive/Documents/missing_data.csv")

print(df)

# print("*" * 100)
#
# x = df['Calories'].mean()
#
# df['Calories'].fillna(x, inplace=True)
# print(df)

print("*" * 100)

z = df['Calories'].mode()[0]
df['Calories'].fillna(z, inplace=True)
print(df)

x = df['Date'].mode()[0]
df['Date'].fillna(x, inplace=True)