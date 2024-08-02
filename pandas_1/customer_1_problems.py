"""
1. find total no. of missing value

2. fill the missing values with india

    1. age < 50 fname, lname, age, loacton

    2. 25<age<40 fname, lname, age, loc

    3. india work => fbame, lname, age, prof

    4. india work, age> 50 => fname, lname, age

    5. age msx 5 => fname, lname, age, age, prof

    6. age min 3 => fname, lname, age, prof

    7. india work, age mxm 3 employee fname,lname,age,prof

    8. india work and prof doctor => fname, lname, age

    9.Pilot prof , age minimum 2 employee fname,lname,age

    10.Pilot prof , age minimum 2 employee fname,lname,age

    11.Pilot prof age mxm 1 employee fname,lname,age

    12.Us work, age mxm 1 employee fname,lname,age

"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/customer1.txt", header=None)
df.columns = ["id", "fname", "lname", "age", "prof", "location"]

print(df.isna().sum())
print("*" * 100)
df = df.fillna("india")


print("1. age < 50 fname, lname, age, loacton")
print(df.loc[df["age"] < 50][['fname', 'lname', 'age', 'location']])

print("*" * 100)

print("2. 25<age<40 fname, lname, age, location")
print(df.loc[(df["age"] < 40) & (df["age"] > 25)][['fname', 'lname', 'age', 'location']])

print("*" * 100)

print('3. india work => fbame, lname, age, prof')
print(df.loc[df['location'] == 'india'][['fname', 'lname', 'age', 'prof']])

print("*" * 100)

print("4. india work, age> 50 => fname, lname, age")
print(df.loc[(df['location'] == 'india') & (df["age"] > 50)][['fname', 'lname', 'age']])

print("*" * 100)

print("5. age msx 5 => fname, lname, age, prof")
print(df.sort_values(by="age", ascending=False)[['fname', 'lname', 'age', 'prof']].head(5))

print("*" * 100)

print("6. age min 3 => fname, lname, age, prof")
print(df.sort_values(by="age")[['fname', 'lname', 'age', 'prof']].head(5))

print("*" * 100)

print("7. india work, age mxm 3 employee fname,lname,age,prof")
print(df.loc[df["location"] == 'india'].sort_values(by="age", ascending=False)[['fname', 'lname', 'age']].head(3))

print("*" * 100)

print("8. india work and prof doctor => fname, lname, age")
print(df.loc[(df["location"] == 'india') & (df["prof"] == "Doctor")][['fname', 'lname', 'age']])


print("*" * 100)

print("9. Pilot prof , age minimum 2 employee fname,lname,age")
print(df.loc[df["prof"] == "Pilot"].sort_values(by="age")[['fname', 'lname', 'age']].head(2))

print("*" * 100)

print("10. Pilot prof , age maximum 1 employee fname,lname,age")
print(df.loc[df["prof"] == "Pilot"].sort_values(by="age", ascending=False)[['fname', 'lname', 'age']].head(1))

print("*" * 100)

print("11. Us work, age mxm 1 employee fname,lname,age")
print(df.loc[df["location"] == "us"].sort_values(by="age", ascending=False)[['fname', 'lname', 'age']].head(1))