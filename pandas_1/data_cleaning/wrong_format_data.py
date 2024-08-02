import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/OneDrive/Documents/missing_data.csv")

# print(df)

# df.loc[7, 'Duration'] = 45
#
# print(df)
print("*" * 100)

x = df['Calories'].mean()

for i in df.index:
    if df.loc[i, 'Calories'] > 400:
        df.loc[i, 'Calories'] = x
    
print(df)
