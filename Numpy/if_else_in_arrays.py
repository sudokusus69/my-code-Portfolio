import numpy as np

arr = np.arange(12)
x = np.where(arr>5, "True", "False")
print(x)