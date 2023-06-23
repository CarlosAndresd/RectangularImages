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


def find_borders(matrix, bleed=0):
	total_height = np.shape(matrix)[0]
	total_width = np.shape(matrix)[1]

	left_border_found = False
	right_border_found = False
	top_border_found = False
	bottom_border_found = False

	left_border = -1
	while not left_border_found:
		left_border += 1
		column = matrix[:, left_border]
		if np.sum(column) > 0:
			left_border_found = True

	left_border = np.amax([0, left_border-bleed])

	right_border = total_width
	while not right_border_found:
		right_border -= 1
		column = matrix[:, right_border]
		if np.sum(column) > 0:
			right_border_found = True

	right_border = np.amin([total_width, right_border + bleed])

	top_border = -1
	while not top_border_found:
		top_border += 1
		row = matrix[top_border, :]
		if np.sum(row) > 0:
			top_border_found = True

	top_border = np.amax([0, top_border - bleed])

	bottom_border = total_height
	while not bottom_border_found:
		bottom_border -= 1
		row = matrix[bottom_border, :]
		if np.sum(row) > 0:
			bottom_border_found = True

	bottom_border = np.amin([total_height, bottom_border + bleed])

	return left_border, right_border, top_border, bottom_border




def allocate_rectangles(num_rows, num_cols, rectangle_dimensions_by_type, number_of_rectangles_by_type, border_by_type, bleed):

	matrix = np.zeros((num_rows, num_cols))

	for rectangle_type, number_rectangles in enumerate(number_of_rectangles_by_type):

		print(f"Rectangle type = {rectangle_type}")

		rectangle_width = rectangle_dimensions_by_type[rectangle_type][0]
		rectangle_height = rectangle_dimensions_by_type[rectangle_type][1]

		for id_rectangle in range(number_rectangles):

			print(f"\tRectangle {id_rectangle} of {number_rectangles}")

			rectangle_placed = False
			counter = 0
			border = border_by_type[rectangle_type]

			while not rectangle_placed:

				if border > 0:
					border -= 1

				rand_row = random.randint(0 + border, num_rows - 1 - border)
				rand_col = random.randint(0 + border, num_cols - 1 - border)

				rand_row = rand_row - int(np.round(rectangle_height/2))
				rand_col = rand_col - int(np.round(rectangle_width/2))

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

	image_left_border, image_right_border, image_top_border, image_bottom_border = find_borders(matrix, bleed)
	return matrix[image_top_border:image_bottom_border, image_left_border:image_right_border]


def show_matrix(matrix):
	plt.matshow(matrix)
	plt.show()


num_r = 300*2
num_c = 200*2

rectangle_dimensions = np.array([[30, 40], [15, 20], [10, 15], [7, 10]])
number_of_rectangles = [5, 10, 20, 50]
border = [120, 130, 140, 150]
bleed = 10

show_matrix(allocate_rectangles(num_r, num_c, rectangle_dimensions, number_of_rectangles, border, bleed))