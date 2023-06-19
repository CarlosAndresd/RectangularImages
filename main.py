import matplotlib.pyplot as plt
import numpy as np
import random

def place_rectangle(initial_matrix, ini_row, ini_col, width, height):
	new_matrix = np.copy(initial_matrix)
	new_matrix[ini_row:ini_row+height, ini_col:ini_col+width] = 2*np.ones((height, width))
	return new_matrix

num_rows = 100
num_cols = 150

matrix = np.zeros((num_rows, num_cols))

for _ in range(20):

	rand_row = random.randint(0, num_rows-1)
	rand_col = random.randint(0, num_cols-1)

	rand_width = random.randint(1, 10)
	rand_height = random.randint(1, 10)

	matrix = place_rectangle(matrix, rand_row, rand_col, rand_width, rand_height)

plt.matshow(matrix)

plt.show()