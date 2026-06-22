import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as lr

ds = pd.read_csv('car_dataset.csv')
x = ds[['present_price']]
y = ds['selling_price']

plt.scatter(x,y, s=3)
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

lr = lr()
lr.fit(x_train, y_train)  # it is used to adjust the values for m and c in the formula -- y = mx + c

print(lr.predict([[8]]))
print(lr.score(x_train,y_train)*100)


print(lr.coef_) #0.91 which means the theta angle formed is <90 deg or it is a pos slope
print(lr.intercept_) # -0.50 which means that the line is below the origin of the graph


'''DISPLAYING THE SLOPE LINE GRAPHICALLY'''

plt.scatter(x,y, s=2, c= 'r', label= 'org data')
plt.plot(x,lr.predict(x), color='b', label= 'slop line' )
plt.legend()
plt.show()






