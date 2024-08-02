import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/sample4.txt", header=None)
df.columns = ["id", "fname", "lname", "age", "phone number", "location"]

print(df.groupby('location')['location'].count().sort_values(ascending=False))