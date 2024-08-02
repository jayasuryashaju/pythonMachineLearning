import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/jayas/OneDrive/Documents/missing_data.csv")

print(df)

print("*" * 100)

print(df.isna().sum())

print("*" * 100)

df['Calories'].fillna(320, inplace=True)
df['Date'].fillna("2024/08/30", inplace=True)

print(df.isna().sum())