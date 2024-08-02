"""
joining different data sets.
types of joining:
    1. inner joining
    2.  left outer joining
    3. right outer joining
    4. full outer joining


inner joining:
    joining two tables with a common field => i it matches in two tables the data
    will be collected


"""
import numpy as np

import pandas as pd

dic_1 = {
    "id": [1, 2, 3, 4, 5],
    "fname": ["venu", "gopi", "sandra", "arunima", "sijin"],
    "lname": ["p", "s", "c", "gopi", "k"],
    "age": [21, 27, 19, 24, 25],
}

dic_2 = {
    "prof": ["data engineer", "software developer", "data engineer", "data analyst", "data scientist"],
    "id": [3, 4, 5, 6, 7],
    "salary": [23000, 32000, 33000, 17000, 39000],
    "company_name": ['tcs', 'sutherland', 'luminar technolab', 'fedserv', "deolite"]
}

df_1 = pd.DataFrame(dic_1)
df_2 = pd.DataFrame(dic_2)

print(df_1)
print("*" * 100)
print(df_2)

print("*" * 100)

df_3 = pd.merge(df_1, df_2, on='id', how="inner")
print(df_3)
print("*" * 100)
print(df_3[['fname', 'age', 'prof', 'salary', 'company_name']])

print("*" * 100)

print(df_3.sort_values(by='age', ascending=False).head(1)[['fname','lname', 'age', 'prof', 'salary']])
