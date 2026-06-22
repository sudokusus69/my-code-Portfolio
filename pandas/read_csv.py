import pandas as pd 

r = pd.read_csv('data.csv')
print(r.to_string(index=False))

pd.options.display.max_rows = 10
print(r)


