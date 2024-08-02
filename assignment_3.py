"""
1. Find row count
2. Remove duplicates and find row count
3. Sort data set by release year in des order
4. Find rating mxm 5 movies name,year,rating
5. Find rating minimum 3 movies name,year,rtaing
6. Find Each year release movie count [count desc order]
7. Each rating count [count desc order]
8. 2008 and rating above 3 [collect]
A. row count
9. Find duration mxm 1 movies name,year,rating,duration
10. Find rating mnm 1 movies name,year,rating,duration
11. Rating above 4 and relase year above 2005
A. Rating mxm movies full data
B. Rating mnm movies full data
12. 2008 movies count
13. 1975-2000 movies collect
A. Row count
14. 1975-2000 and rating above 3.5 total row count
"""

import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/jayas/Downloads/movies_cleaned_pandas.csv", header=None)
df.columns = ["id", "movie_name", "year", "rating", "duration"]
print(df)