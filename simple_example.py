import matplotlib.pyplot as plt
import numpy as np

matrix = np.zeros((2, 3))
matrix[0, 0] = 1

plt.matshow(matrix)

plt.show()


matrix = np.zeros((20, 30))
matrix[0:10, 0:10] = np.ones((10, 10))

plt.matshow(matrix)

plt.show()