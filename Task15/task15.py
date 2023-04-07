import numpy as np
import pandas as pd

data = {'Name': ['zainab','Ali','huda'],
     'Age':[21,66,np.nan],
     'Address': ['sialkot',np.nan,'Islamabad'] }

df = pd.DataFrame(data)

print(df)

print(df.isnull())

print(df.notnull())


# Dropping Missing Values

df.dropna()

data = pd.DataFrame([[np.nan, 7.5, np.nan], [1., np.nan, np.nan],
                      [np.nan, np.nan, 66], [9, 6.5, 3.]])


print('Data after Cleaning....')
data.dropna(axis=0)
print(data)
data.dropna(axis=0 , how='all')
print(data)

print(df.fillna(0)) #Filling out missing Data with 0
print(df.fillna(method='ffill'))



#Detecting and Removing Outliers
print("---Detecting and Removing Outliers----")
df = pd.DataFrame(np.random.randn(1000, 4))
print(df.head())

# Checking for values exceeding 2 or -2

print(df[(np.abs(df)>2).any(1)])


# Dealing with outliers exceeding 3 or -3

df[np.abs(df)>3] = np.sign(df)*3

print(df[(np.abs(df)>3).any(1)] )