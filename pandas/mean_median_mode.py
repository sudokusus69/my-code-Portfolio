import pandas as pd

df = pd.read_csv('data.csv')

df2 = df["Calories"].mode()[0]

df.fillna({"Calories":df2}, inplace = True)  # it is used to change the original df

print(df.to_string())