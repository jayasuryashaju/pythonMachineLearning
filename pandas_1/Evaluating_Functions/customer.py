import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/customer1.txt", header=None)
df.columns = ["id", "fname", "lname", "age", "prof", "location"]

print(df.loc[df['location'] == 'india'].groupby('prof')['prof'].count().sort_values(ascending=False))