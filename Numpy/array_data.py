import numpy as np


# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000], # Paradise Biryani
    [2, 120000, 140000, 160000, 190000], # Beijing Bites
    [3, 200000, 230000, 260000, 300000], # Pizza Hub
    [4, 180000, 210000, 240000, 270000], # Burger Point
    [5, 160000, 185000, 205000, 230000]  # Chai Point
])


print("\n ===> Sales Data <===")
size = sales_data.shape
print(f'shape of the data: {size}\n=')
print('maximum sales of every resaturent: ', np.max(sales_data[:, 1:], axis = 1))
print('maximuum sales of each resstaurent each year: ', np.max(sales_data[:, 1:], axis = 0))
avg = np.mean(sales_data[: , 1:], axis = 1)
print('average sales of each resaturent: ', avg)
cumsum = np.cumsum(sales_data[:, 1:], axis = 1)
print('cumulative sum of sales of each resaturent: ', cumsum)
# plotting this on a graph
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.dates as mdates
import datetime

# Convert the sales data to a pandas DataFrame
df = pd.DataFrame(sales_data, columns=['Restaurant ID', '2021', '2022', '2023', '2024'])
# Set the index to the restaurant ID
df.set_index('Restaurant ID', inplace=True)
# Transpose the DataFrame for better plotting
df = df.T
# Plotting the sales data
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, dashes=False)
plt.title('Sales Data of Restaurants (2021-2024)')
plt.xlabel('Year')
plt.ylabel('Sales (in $)')
plt.xticks(rotation=45)
plt.grid()
plt.legend(title='Restaurant ID', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
# Plotting the cumulative sum of sales data
