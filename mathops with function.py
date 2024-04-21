import numpy as np # Importing numpy library
import pandas as pd # Importing pandas library

a1 = np.array([11, 12, 13, 14]) # Creating a1 array
a2 = np.array([1, 2, 3, 4]) # Creating a2 array

s1 = pd.Series(a1, index=['a', 'b', 'c', 'd']) # Creating a series with a1 array
s2 = pd.Series(a2, index=['a', 'b', 'c', 'd']) # Creating a series with a2 array

print(s1.add(s2)) # Adding two series
print(s1.sub(s2)) # Subtracting two series
print(s1.mul(s2)) # Multiplying two series
print(s1.div(s2)) # Dividing two series