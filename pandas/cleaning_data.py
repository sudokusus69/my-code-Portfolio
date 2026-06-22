import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')


df.dropna(inplace=True)
print(df)

print(df.isnull().sum().sum())

sns.heatmap(df.isnull())
plt.show()


