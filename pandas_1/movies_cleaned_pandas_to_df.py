import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/jayas/Downloads/movies_cleaned_pandas.csv", header=None)
df.columns = ["id", "movie_name", "year", "rating", "duration"]
print(df)

