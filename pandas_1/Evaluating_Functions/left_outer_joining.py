"""
left outer joining
    it will return all the value from the left data frame and all the matching data from the right data frame.
    empty fields will have a null value.

"""

import pandas as pd
import numpy as np
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


df_3 = pd.merge(df_1, df_2, on='id', how='left')
print(df_3)