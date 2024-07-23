"""
function = read_csv("location", sep=",", header=None(if no header))

default separation method = ","    =>  so no need to specify if it is a coma separated file

"""
import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/sample4.txt", sep=",", header=None)
print(df)
df.columns = ["id", "fname", "lname", "age", "phone number", "location"]
print(df)