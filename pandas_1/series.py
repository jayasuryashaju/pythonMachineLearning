"""

"""

import pandas as pd
import numpy as np

a = pd.Series([4, 5, 6, 7, 8, 9])
print(a)
print(a.shape)
print(a.size)
print(a.dtype)

elements = [1, 2, 4]
label = ["car", "bike", "train"]
b = pd.Series(data=elements, index=label)
print(b)
