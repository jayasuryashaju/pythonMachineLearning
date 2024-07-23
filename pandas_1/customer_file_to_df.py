import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/customer1.txt", header=None)
df.columns = ["id", "fname", "lname", "age", "prof", "location"]
# print(df)

print(df.head(20))

print("*" * 100)

# printing required columns only

df_1 = df[["fname", "lname", "age"]][:11]
print(df_1)