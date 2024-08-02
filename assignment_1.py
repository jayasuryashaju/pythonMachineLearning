"""
Questions:
file : Customer1
    fill missing values with "india"

1. Find Row count
2. Remove duplicate rows and find total row counts
3. Age maximum 10 fname,lname,prof,loc
4. Age minimum 5-employee fname,lname,prof,loc
5. Each location count [count desc order]
6. Full data
7. Each age group count [age desc order]
8. Each profession count [count desc order]
9. India work
    A. Row count
    B. Each profession count [count desc order]
    C. Age mxm 3 employees fname,lname,age,prof
    D. Age minimum 3 employees fname,lname,age,prof
    E. age above 40 full data
    F. age range 30 to 40 [profession count]
10. Us work
    A. Row count
    B. Each age group count
    C. Each profession counts [count desc]
    D. Civil engineer dept and age above 30
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/customer1.txt", header=None)
df.columns = ["id", "fname", "lname", "age", "prof", "location"]
df = df.fillna("india")

print("q1")
print(df.shape[0])

print("*" * 100)

print("q2")
print(df.drop_duplicates().shape[0])

print("*" * 100)

print("q3")
print(df.sort_values(by='age', ascending=False)[['fname', 'lname', 'prof', 'location']].head(10))

print("*" * 100)

print("q4")
print(df.sort_values(by='age')[['fname', 'lname', 'prof', 'location']].head(5))

print("*" * 100)

print("q5")
print(df.groupby('location')['location'].count().sort_values(ascending=False))

print("*" * 100)

print("q6")
print(df.loc[df['location'] == 'australia'])

print("*" * 100)

print("q7")
print(df.groupby('age')['age'].count().sort_values(ascending=False))

print("*" * 100)

print("q8")
print(df.groupby('prof')['prof'].count().sort_values(ascending=False))

print("*" * 100)

print("q9_a")
df_1 = df.loc[df['location'] == 'india']
print(df_1.shape[0])

print("*" * 100)

print("q9_b")
print(df_1.groupby('prof')['prof'].count().sort_values(ascending=False))

print("*" * 100)

print("q9_c")
print(df_1.sort_values(by='age', ascending=False)[['fname', 'lname', 'age', 'prof']].head(3))

print("*" * 100)

print("q9_d")
print(df_1.sort_values(by='age')[['fname', 'lname', 'age', 'prof']].head(3))

print("*" * 100)

print("q9_e")
print(df_1.loc[df['age'] > 40])

print("*" * 100)

print("q9_f")
print(df_1.loc[(df['age'] < 40) & (df['age'] > 30)].groupby('prof')['prof'].count())

print("*" * 100)

print("q10_a")
df_2 = df.loc[df['location'] == 'us']
print(df_2.shape[0])

print("*" * 100)

print("q10_b")
print(df_2.groupby('age')['age'].count())

print("*" * 100)

print("q10_c")
print(df_2.groupby('prof')['prof'].count().sort_values(ascending=False))

print("*" * 100)

print("q10_d")
print(df_2.loc[(df['prof'] == 'Civil engineer') & (df['age'] > 30)])