
import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/OneDrive/Documents/Temperature", header=None, sep=" ")
df.columns = ['year', 'temp']


df_1 = df.groupby('year')['temp'].max().sort_values(ascending=False)
print(df_1)

print("*" * 100)
print("min temperature each year")

print(df.groupby('year')['temp'].min().sort_values(ascending=False))

print("*" * 100)
print("total temperature each year")
print(df.groupby('year')['temp'].sum().sort_values(ascending=False))

print("*" * 100)
print("average temperature each year")
print(df.groupby('year')['temp'].mean().round(2).sort_values(ascending=False))