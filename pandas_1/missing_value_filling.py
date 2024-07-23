import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/OneDrive/Documents/missing_data.csv")
print(df)
print("*" * 100)
print(df.isna().sum())
print("*" * 100)

df_1 = df.fillna(2255)
print(df_1)