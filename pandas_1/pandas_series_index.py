import numpy as np
import pandas as pd

dic = {"id": 120, "fname": " Jayasurya", "lname": "Shaju", "age": 23, "prof": "Data Engineer", "salary": 23000}

a = pd.Series(dic, index=['fname', 'lname', 'salary', 'id', 'age', 'prof'])

print(a)
