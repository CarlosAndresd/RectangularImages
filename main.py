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

	num_rectangles = np.sum(number_of_rectangles_by_type)

	rectangle_allocation = np.zeros((num_rectangles, 6))
	# Information by columns:
	# Column 1 -> card number
	# Column 2 -> rectangle type
	# Column 3 -> initial row
	# Column 4 -> initial column
	# Column 5 -> rectangle width
	# Column 6 -> rectangle height

	current_rectangle = 0

	matrix = np.zeros((num_rows, num_cols))

	for rectangle_type, number_rectangles in enumerate(number_of_rectangles_by_type):

		# print(f"Rectangle type = {rectangle_type}")

		rectangle_width = rectangle_dimensions_by_type[rectangle_type][0]
		rectangle_height = rectangle_dimensions_by_type[rectangle_type][1]

		card_number = 0

		for id_rectangle in range(number_rectangles):

			# print(f"\tRectangle {id_rectangle} of {number_rectangles}")

			rectangle_placed = False
			counter = 0
			initial_border = border_by_type[rectangle_type]

			while not rectangle_placed:

				if initial_border > 0:
					initial_border -= 1

				rand_row = random.randint(0 + initial_border, num_rows - 1 - initial_border)
				rand_col = random.randint(0 + initial_border, num_cols - 1 - initial_border)

				rand_row = rand_row - int(np.round(rectangle_height/2))
				rand_col = rand_col - int(np.round(rectangle_width/2))

				counter += 1
				matrix, status = place_rectangle(matrix, rand_row, rand_col, rectangle_width, rectangle_height, rectangle_type+1)
				# print(f"Counter = {counter}")
				# print(f"status = {status}")

				if status == 1:
					# print("Rectangle placed")
					rectangle_placed = True
					rectangle_allocation[current_rectangle, :] = np.array([card_number, rectangle_type, rand_row, rand_col, rectangle_width, rectangle_height])
					current_rectangle += 1
					card_number += 1

				if counter > 10000:
					print("Limit reached")
					rectangle_placed = True

	matrix_borders = find_borders(matrix, bleed)
	image_left_border, image_right_border, image_top_border, image_bottom_border = matrix_borders
	return matrix[image_top_border:image_bottom_border, image_left_border:image_right_border], rectangle_allocation, matrix_borders


def show_matrix(matrix):
	plt.matshow(matrix)
	plt.show()


def create_latex_file(rectangle_allocation, matrix_borders):
	latex_file = open('resulting_images.tex', 'w')
	latex_file.write(chr(92) + 'documentclass[tikz,border=0pt]' + chr(123) + 'standalone}' + '\n')

	latex_file.write(chr(92) + 'begin' + chr(123) + 'document}' + '\n')
	latex_file.write(chr(92) + 'begin' + chr(123) + 'tikzpicture}' + '\n')

	image_left_border, image_right_border, image_top_border, image_bottom_border = matrix_borders

	latex_file.write(chr(92) + 'fill[black] (' + str(image_left_border) + 'mm,' + str(image_top_border) + 'mm)  rectangle (' + str(image_right_border) + 'mm,' + str(image_bottom_border) + 'mm);' + '\n')

	for rectangle_information in rectangle_allocation:
		place_rectangle_image(rectangle_information, latex_file)

	latex_file.write(chr(92) + 'end' + chr(123) + 'tikzpicture}' + '\n')
	latex_file.write(chr(92) + 'end' + chr(123) + 'document}' + '\n')


def place_rectangle_image(rectangle_information, latex_file):
	card_number = rectangle_information[0]+1
	card_type = rectangle_information[1]+1
	rand_row = rectangle_information[2]
	rand_col = rectangle_information[3]
	rectangle_width = rectangle_information[4]
	rectangle_height = rectangle_information[5]

	y_pos = rand_row + 0.5*rectangle_height
	x_pos = rand_col + 0.5*rectangle_width

	latex_file.write(chr(92) + 'node at (' + str(x_pos) + 'mm,' + str(y_pos) + 'mm) {' + chr(92) +
					 'includegraphics[height=' + str(0.9*rectangle_height) + 'mm]{images/card_' +
					 str(int(card_number)) + '-color_' + str(int(card_type)) + '.pdf}};' + '\n')


num_r = 300*2
num_c = 200*2

rectangle_dimensions = np.array([[30, 40], [20, 27], [15, 20], [10, 15]])
number_of_rectangles = [5, 10, 20, 30]
border = [150, 130, 140, 150]

rectangle_dimensions_dict = {10: [30, 40], 9: [20, 27], 8: [15, 20], 7: [10, 15], 6:[10, 15]}


bleed = 10

matrix, rectangle_allocation, matrix_borders = allocate_rectangles(num_r, num_c, rectangle_dimensions, number_of_rectangles, border, bleed)
print(rectangle_allocation)
create_latex_file(rectangle_allocation, matrix_borders)
show_matrix(matrix)