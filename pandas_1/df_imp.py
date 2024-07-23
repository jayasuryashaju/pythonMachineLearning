import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/customer1.txt", header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'profession', 'location']

x = df.iloc[:, :-1]
print(x)

print("*" * 100)

y = df.iloc[:, -1]
print(y)