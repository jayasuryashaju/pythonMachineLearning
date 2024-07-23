import pandas as pd
import numpy as np

# employee_dic = {
#     {"id": 101, "fname": "venu", "lname": "p", "age": 23, "prof": "data engineer"},
#     {"id": 102, "fname": "gopi", "lname": "p", "age": 27, "prof": "data engineer"},
#     {"id": 103, "fname": "sandra", "lname": "p", "age": 21, "prof": "software developer"},
#     {"id": 104, "fname": "arunima", "lname": "s", "age": 15, "prof": "data analyst"}
# }


employee_dic = {
    "id": [101, 102, 103, 104],
    "fname": ["venu", "gopi", "sandra", "arunima"],
    "lname": ["p", "s", "c", "gopi"],
    "age": [21, 27, 19, 24],
    "prof": ["data engineer", "software developer", "data engineer", "data analyst"],
    "location": ["adimali", "wadakkachery", "adoor", "palakkad"]
}

df = pd.DataFrame(employee_dic)
print(df)
print("*" * 100)

df["salary"] = [23000, 43000, 36000, 26000]
print(df)