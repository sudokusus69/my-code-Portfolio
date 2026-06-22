import numpy as np
import matplotlib.pyplot as plt 

x = np.random.normal(200, 10, 1000) #mean 200, std deviation 10, 1000 samples  
plt.hist(x, bins=20)
plt.show()