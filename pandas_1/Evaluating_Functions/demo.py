"""
Evaluating Functions:
    count
    max
    min
    sum
    mean

count:
    to get column vise count
    eg:
        how many persons are working in india
    syntax:
        new_df = old_df.groupby('column_name')['column_name'].count()

"""

import pandas as pd
import numpy as np

employee_list = [[101, "vinu", "gopalan", 25, "data analyst", 23000],
                 [102, "gopi", "krishna", 27, "data engineer", 32000],
                 [103, "avani", "m", 23, "data scientist", 32000],
                 [104, "gopika", "p", 26, "software developer", 25000],
                 [105, "amal", "c", 21, "software tester", 22000],
                 [106, "yadhu", "v", 28, "data analyst", 26000],
                 [107, "akash", "c", 24, "data engineer", 30000],
                 [108,  "vimal", "sasi", 32, "flutter developer", 33000],
                 [102, "gopi", "krishna", 27, "data engineer", 32000],
                 [110, "amal", "c", 21, "software tester", 22000],
                 [103, "avani", "v", 24, "data analyst", 32000],
                 ]


df = pd.DataFrame(employee_list,columns=["id", "fname", "lname", "age", "prof", "salary"])
print(df)

df_1 = df.groupby("prof")['prof'].count()
print(df_1)

print(df_1.sort_values(ascending=False))

print("*" * 100)

print(df.groupby('age')['age'].count().sort_values(ascending=False))