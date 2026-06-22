import pandas as pd

# read a json file with the name 'data.json'

df  = pd.read_json('data.json')
# print(df.to_string(index = True))

# print(df[-10:-1])

print(df.head(10))
print('.........................................')
print(df.tail(5))

# print(df.info())
# print(df.describe())
