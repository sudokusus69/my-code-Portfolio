import pandas as pd

# creating a dataframe and finding
dataframe= {  
    'name': ['alice', 'bob', 'charlie', 'david'],
    'age': [25, 30, 35, 40],
    'city': ['new york', 'los angeles', 'chicago', 'houston'],
    'salary': [70000, 80000, 60000, 90000]
}
df = pd.DataFrame(dataframe, index = ['a', 'b', 'c', 'd'])

print(df)



















