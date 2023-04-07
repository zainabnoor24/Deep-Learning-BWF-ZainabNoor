
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [4, 2, 6], 'B': [1, 8, 9]})

# concatenate the DataFrames row-wise
result = pd.concat([df1, df2])
print(result)




df1 = pd.DataFrame({'name': ['zainab', 'noor', 'ali', 'Ahmed'], 'value': [1, 2, 3, 4]})
df2 = pd.DataFrame({'name': ['noor', 'zoha', 'ali', 'Muneeb'], 'value': [5, 6, 7, 8]})

# merge the DataFrames based on the 'name' column
result = pd.merge(df1, df2, on='name')
print(result)


df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['X', 'Y', 'Z'])
df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]}, index=['X', 'Y', 'Z'])

# join the DataFrames based on index
result = df1.join(df2)
print(result)


import numpy as np

arr1d = np.array([1, 2, 3, 4, 5, 6])

# reshape the array to a 2D array with 2 rows and 3 columns
arr2d = arr1d.reshape((2, 3))

print(arr2d)
