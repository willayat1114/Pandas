import pandas as pd
import numpy as np

s1 = pd.Series([11,12,13,14], index=['a','b', 'c', 'd'])
s2 = pd.Series([1,2,3,4], index=['a', 'b', 'c','o'])

print(s1.add(s2, fill_value=0))
