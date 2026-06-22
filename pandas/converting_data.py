import pandas as pd

df = pd.read_csv('data2.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())