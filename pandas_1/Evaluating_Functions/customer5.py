"""
id, fname, lname, age, prof, location, salary

1. each prof count [desc]
2. each prof max salary [desc]
3. each location total salary [desc]
4. each prof min age [desc]
5. each prof avg age [desc]
"""


import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/OneDrive/Documents/customer5.txt", header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location', 'salary']

print("*" * 100)
print("each prof count [desc]")
print(df.groupby('prof')['prof'].count().sort_values(ascending=False))

print("*" * 100)
print("2. each prof max salary [desc]")
print(df.groupby('prof')['salary'].max().sort_values(ascending=False))

print("*" * 100)
print("3. each location max salary [desc]")
print(df.groupby('location')['salary'].sum().sort_values(ascending=False))

print("*" * 100)
print("4. each prof min age [desc]")
print(df.groupby('prof')['age'].min().sort_values(ascending=False))

print("*" * 100)
print("5. each prof avg age [desc]")
print(df.groupby('prof')['age'].mean().round(2).sort_values(ascending=False))
