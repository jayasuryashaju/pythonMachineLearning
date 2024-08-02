"""
1. joining two data frame
2. id equal => name, age, location, date, amount
3. age above 25 => fname , age, loc, date, amount
4. highest amount purchase => name, age, loc, date, amount
5. latest date, name, age, loc, date, amount
"""
import pandas as pd
import numpy as np
df_1 = pd.read_csv("C:/Users/jayas/OneDrive/Documents/custom.txt", header=None)
df_2 = pd.read_csv("C:/Users/jayas/OneDrive/Documents/order.txt", header=None)
df_1.columns = ['id', 'name', 'age', 'loc', 'salary']
df_2.columns = ['item', 'date', 'id', 'amnt']


print(df_1)
print(df_2)

print("*" * 100)

df_3 = pd.merge(df_1, df_2, on='id', how='inner')

print(df_3)

print("*" * 100)

print(df_3[['name', 'age', 'loc', 'date', 'amnt']])

print("*" * 100)

print(df_3.loc[df_3['age'] > 25][['name', 'age', 'loc', 'date', 'amnt']])

print("*" * 100)

print(df_3.sort_values(by='amnt', ascending=False).head(1)[['name', 'age', 'loc', 'salary', 'date', 'amnt']])

print("*" * 100)

print(df_3.sort_values(by='date', ascending=False).head(1)[['name', 'age', 'loc', 'salary', 'date', 'amnt']])