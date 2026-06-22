import pandas as pd

s = {'day1':'hindi', 'day2':'english', 'day3':'maths'}
a = pd.Series(s)

print(a)
print(a['day1'])