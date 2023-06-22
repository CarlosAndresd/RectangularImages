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
		return new_matrix, 1
	else:
		# print("The rectangle cannot be placed")
		return initial_matrix, -1


num_rows = 200
num_cols = 300

matrix = np.zeros((num_rows, num_cols))

rectangle_dimensions_by_type = np.array([[30, 40],
										[15, 20],
										[7, 10]])


number_of_rectangles_by_type = [3, 10, 30]

for rectangle_type, number_rectangles in enumerate(number_of_rectangles_by_type):

	print(f"Rectangle type = {rectangle_type}")

	rectangle_width = rectangle_dimensions_by_type[rectangle_type][0]
	rectangle_height = rectangle_dimensions_by_type[rectangle_type][1]

	for id_rectangle in range(number_rectangles):

		print(f"\tRectangle {id_rectangle} of {number_rectangles}")

		rand_row = random.randint(0, num_rows-1)
		rand_col = random.randint(0, num_cols-1)

		rectangle_placed = False
		counter = 0

		while not rectangle_placed:

			counter += 1
			matrix, status = place_rectangle(matrix, rand_row, rand_col, rectangle_width, rectangle_height, rectangle_type+1)
			# print(f"Counter = {counter}")
			# print(f"status = {status}")

			if status == 1:
				# print("Rectangle placed")
				rectangle_placed = True

			if counter > 10000:
				print("Limit reached")
				rectangle_placed = True

plt.matshow(matrix)

plt.show()