import numpy as np

"""
The dot product in NumPy (using np.dot or the @ operator) is used to calculate the scalar product of two vectors.
It is a fundamental operation in linear algebra and has various applications such as:
- Calculating the projection of one vector onto another.
- Measuring the similarity between two vectors (e.g., in machine learning and data analysis).
- Computing work done in physics (force · displacement).
- Used in matrix multiplication and transformations in graphics and engineering.
Example:"""


a = np.array(['apple', 'banana', 'cherry'])
b = np.array(['strawberry', 'orange', 'grape'])

# vectorised array 
vectorise_arrays = np.vectorize(str.upper)
print(vectorise_arrays(a + b))