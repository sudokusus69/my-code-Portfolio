import pandas as pd

# to find the correlations between colums using corr method
df = pd.read_csv('data.csv')
print(df.corr())

# The corr() method ignores "not numeric" columns.
# What is a good correlation? 
# it is safe to say at least 0.6 (or -0.6) to call it a good correlation.