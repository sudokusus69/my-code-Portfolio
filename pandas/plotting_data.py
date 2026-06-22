import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
# You can use 'line', 'bar', 'barh', 'hist', 'box', 'area', 'pie', etc.
# Example: Line plot
df.plot(kind='hist', x='Maxpulse', y='Duration', title='Plot Example')



plt.show()
