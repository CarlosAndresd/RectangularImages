import matplotlib.pyplot as plt
import numpy as np
import random


def enough_space(initial_matrix, ini_row, ini_col, width, height):
	total_height = np.shape(initial_matrix)[0]
	total_width = np.shape(initial_matrix)[1]

	if ini_row+height > total_height:
		return False

	if ini_col+width > total_width:
		return False

	return True


def is_empty(initial_matrix, ini_row, ini_col, width, height):
	if np.sum(initial_matrix[ini_row:ini_row + height, ini_col:ini_col + width]) == 0:
		return True
	else:
		return False


def can_be_placed(initial_matrix, ini_row, ini_col, width, height):
	if is_empty(initial_matrix, ini_row, ini_col, width, height):
		return enough_space(initial_matrix, ini_row, ini_col, width, height)
	else:
		return False


def place_rectangle(initial_matrix, ini_row, ini_col, width, height, coefficient):

	if can_be_placed(initial_matrix, ini_row, ini_col, width, height):
		new_matrix = np.copy(initial_matrix)
		new_matrix[ini_row:ini_row+height, ini_col:ini_col+width] = coefficient*np.ones((height, width))
		return new_matrix
	else:
		print("The rectangle cannot be placed")
		return initial_matrix


num_rows = 100
num_cols = 150

matrix = np.zeros((num_rows, num_cols))

for _ in range(20):

	rand_row = random.randint(0, num_rows-1)
	rand_col = random.randint(0, num_cols-1)

	rand_width = random.randint(1, 10)
	rand_height = random.randint(1, 10)

	matrix = place_rectangle(matrix, rand_row, rand_col, rand_width, rand_height, 1)

plt.matshow(matrix)

plt.show()