import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split


ds = pd.read_csv('car_dataset.csv')

print(ds.bfill(inplace=True))

input_data = ds.iloc[::-1]
output_data = ds['selling_price']

x_train, x_test, y_train, y_test = train_test_split(input_data, output_data, test_size=0.25)

print(x_train.shape)