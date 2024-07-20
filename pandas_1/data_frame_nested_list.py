import pandas as pd
import numpy as np

employee_list = [[101, "vinu", "gopalan", 25, "data analyst", 23000],
                 [102, "gopi", "krishna", 27, "data engineer", 32000],
                 [103, "avani", "m", 23, "data scientist", 32000],
                 [104, "gopika", "p", 26, "software developer", 25000],
                 [105, "amal", "c", 21, "software tester", 22000],
                 [106, "yadhu", "v", 28, "data analyst", 26000],
                 [107, "akash", "c", 24, "data engineer", 30000]]

df = pd.DataFrame(employee_list)

print(df)

print("*" * 100)

print(pd.DataFrame(employee_list, columns=["id", "fname", "lname", "age", "prof", "salary"]))

print(df.shape)
print(df.dtypes)
print("*" * 100)

print(df.head(3))