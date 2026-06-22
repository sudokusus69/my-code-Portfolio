import pandas as pd

df = pd.read_csv('data.csv')
df2 = df.fillna({'Calories':200000}, inplace = True) #it is used to change the original df 

print(df)