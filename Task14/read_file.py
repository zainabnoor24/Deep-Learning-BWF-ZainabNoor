######csv file
import pandas as pd

df=pd.read_csv("F:/bytewise-fellowship/Task14/example1.csv")
print(df.head())


#####json file
import json
f = open("F:/bytewise-fellowship/Task14/data.json")
data = json.load(f)
for i in data['emp_details']:
    print(i)

f.close()


#####excel file
import pandas as pd

df = pd.read_excel('F:/bytewise-fellowship/Task14/sample.xlsx')

print(df)