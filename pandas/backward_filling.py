import pandas as pd 


'''BACKFARD FILLING IS USED TO FILL THE MISSING DATA VALUE 
BY RELACING IT WITH A NEW VALUE JUST BELOW IT '''


ds = pd.read_csv('data.csv')


print(ds.isnull().sum().sum())
bfillling = ds.bfill(inplace=True)
print(ds.to_string())

print(ds.isnull().sum().sum())