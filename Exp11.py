# Write a Python program to create a Pandas Series with ten random numbers.
import pandas as pd
import numpy as np
s = pd.Series(np.random.rand(10))
print("Pandas Series:")
print(s)