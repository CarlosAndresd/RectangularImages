import matplotlib.pyplot as plt
import numpy as np
import random


num_rows = 100
num_cols = 150

matrix = np.zeros((num_rows, num_cols))

rand_row = random.randint(0, num_rows-1)
rand_col = random.randint(0, num_cols-1)

matrix[rand_row, rand_col] = 1

plt.matshow(matrix)

plt.show()