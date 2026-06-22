from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(random.binomial(n=100, p=0.5, size=1000), kind='kde')
plt.show()