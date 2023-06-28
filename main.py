import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd


def enough_space(initial_matrix, ini_row, ini_col, width, height):
	total_height = np.shape(initial_matrix)[0]
	total_width = np.shape(initial_matrix)[1]

	if ini_row+height > total_height:
		# print('Not enough space')
		return False

	if ini_col+width > total_width:
		# print('Not enough space')
		return False

	return True


def is_empty(initial_matrix, ini_row, ini_col, width, height):
	if np.sum(initial_matrix[ini_row:ini_row + height, ini_col:ini_col + width]) == 0:
		return True
	else:
		# print('Not empty')
		# print(f"sum = {np.sum(initial_matrix[ini_row:ini_row + height, ini_col:ini_col + width])}")
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


def allocate_rectangles(num_rows, num_cols, different_types, rectangle_dimensions_by_type, number_of_rectangles_by_type, border_by_type, bleed):

	num_rectangles = sum(number_of_rectangles_by_type.values())

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

	for rectangle_type in different_types: # number_rectangles in enumerate(number_of_rectangles_by_type):

		# print(f"Rectangle type = {rectangle_type}")

		number_rectangles = number_of_rectangles_by_type[rectangle_type]

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
					if counter > 1000:
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

	df = pd.DataFrame(rectangle_allocation,
					  columns=['card_number', 'card_type', 'initial_row', 'initial_col', 'card_width', 'card_height'])
	df = df.sort_values(by='card_type')
	rectangle_allocation = df.to_numpy(dtype='int')

	return matrix[image_top_border:image_bottom_border, image_left_border:image_right_border], rectangle_allocation, matrix_borders


def show_matrix(matrix):
	plt.matshow(matrix)
	plt.show()

def compare_matrices(matrix_1, matrix_2):
	fig, axs = plt.subplots(ncols=2, nrows=1, figsize=(5.5, 3.5), layout="constrained")
	axs[0].matshow(matrix_1)
	axs[1].matshow(matrix_2)
	plt.show()


def create_latex_file(rectangle_allocation, matrix_borders, image_names_per_type):
	latex_file = open('resulting_images.tex', 'w')
	latex_file.write(chr(92) + 'documentclass[tikz,border=0pt]' + chr(123) + 'standalone}' + '\n')

	latex_file.write(chr(92) + 'begin' + chr(123) + 'document}' + '\n')
	latex_file.write(chr(92) + 'begin' + chr(123) + 'tikzpicture}' + '\n')

	image_left_border, image_right_border, image_top_border, image_bottom_border = matrix_borders

	latex_file.write(chr(92) + 'begin' + chr(123) + 'scope}' + '\n')

	latex_file.write(
		chr(92) + 'clip (' + str(image_left_border) + 'mm,' + str(image_top_border) + 'mm)  rectangle (' + str(
			image_right_border) + 'mm,' + str(image_bottom_border) + 'mm);' + '\n')
	latex_file.write(chr(92) + 'fill[black] (' + str(image_left_border) + 'mm,' + str(image_top_border) + 'mm)  rectangle (' + str(image_right_border) + 'mm,' + str(image_bottom_border) + 'mm);' + '\n')

	for rectangle_information in rectangle_allocation:
		place_rectangle_image(rectangle_information, latex_file, image_names_per_type)

	latex_file.write(chr(92) + 'end' + chr(123) + 'scope}' + '\n')

	latex_file.write(chr(92) + 'end' + chr(123) + 'tikzpicture}' + '\n')
	latex_file.write(chr(92) + 'end' + chr(123) + 'document}' + '\n')


def place_rectangle_image(rectangle_information, latex_file, image_names_per_type):
	card_number = rectangle_information[0]
	card_type = rectangle_information[1]
	rand_row = rectangle_information[2]
	rand_col = rectangle_information[3]
	rectangle_width = rectangle_information[4]
	rectangle_height = rectangle_information[5]

	y_pos = rand_row + 0.5*rectangle_height
	x_pos = rand_col + 0.5*rectangle_width

	image_name = image_names_per_type[int(card_type)][int(card_number)]

	image_name = image_name.replace(':', '')

	latex_file.write(chr(92) + 'node at (' + str(x_pos) + 'mm,' + str(y_pos) + 'mm) {' + chr(92) +
					 'includegraphics[height=' + str(0.99*rectangle_height) + 'mm]{images/' +
					 image_name + '.jpg}};' + '\n')


def get_image_information():

	images_information = pd.read_excel('images_information_v2.xlsx')
	# images_information = pd.read_excel('images_information_v3.xlsx')
	# images_information = pd.read_excel('images_information.xlsx')

	# Get the unique values of type
	type_values = images_information.Type.unique()

	image_names_per_type = dict()
	number_images_per_type = dict()

	for image_type in type_values:
		image_names_per_type[image_type] = []
		number_images_per_type[image_type] = 0

	for row in images_information.index:
		card_name = str(images_information['Name'][row])
		card_type = images_information['Type'][row]

		card_name = card_name.replace(':', '')

		image_names_per_type[card_type].append(card_name)
		number_images_per_type[card_type] = number_images_per_type[card_type] + 1

	return type_values, number_images_per_type, image_names_per_type


def remove_rectangle(matrix, single_rectangle, matrix_borders):
	image_left_border, image_right_border, image_top_border, image_bottom_border = matrix_borders

	rectangle_row = single_rectangle[2] - image_top_border
	rectangle_col = single_rectangle[3] - image_left_border
	rectangle_width = single_rectangle[4]
	rectangle_height = single_rectangle[5]

	# print(f"row = {rectangle_row}, col = {rectangle_col}, width = {rectangle_width}, height = {rectangle_height} \n")

	matrix[rectangle_row:rectangle_row + rectangle_height, rectangle_col:rectangle_col + rectangle_width] = np.zeros(
		(rectangle_height, rectangle_width))


def move_single_rectangle(matrix, single_rectangle, matrix_borders, horizontal_movement, vertical_movement):
	total_height = np.shape(matrix)[0]
	total_width = np.shape(matrix)[1]

	image_left_border, image_right_border, image_top_border, image_bottom_border = matrix_borders

	rectangle_type = single_rectangle[1]
	rectangle_row = single_rectangle[2] - image_top_border
	rectangle_col = single_rectangle[3] - image_left_border
	rectangle_width = single_rectangle[4]
	rectangle_height = single_rectangle[5]

	new_col = rectangle_col + horizontal_movement
	new_row = rectangle_row + vertical_movement

	if new_col < 0:
		new_col = 0

	if new_col >= total_width:
		new_col = total_width

	if new_row < 0:
		new_row = 0

	if new_row >= total_height:
		new_row = total_height

	if horizontal_movement != 0:
		remove_rectangle(matrix, single_rectangle, matrix_borders)
		matrix, status = place_rectangle(matrix, rectangle_row, new_col, rectangle_width, rectangle_height, rectangle_type)
		if status == 1:
			single_rectangle[3] = new_col + image_left_border

		if status == -1:
			matrix, _ = place_rectangle(matrix, rectangle_row, rectangle_col, rectangle_width, rectangle_height,
										rectangle_type)

	if vertical_movement != 0:
		remove_rectangle(matrix, single_rectangle, matrix_borders)
		matrix, status = place_rectangle(matrix, new_row, rectangle_col, rectangle_width, rectangle_height, rectangle_type)

		if status == 1:
			single_rectangle[2] = new_row + image_top_border

		if status == -1:
			matrix, _ = place_rectangle(matrix, rectangle_row, rectangle_col, rectangle_width, rectangle_height,
											 rectangle_type)

	return matrix, status


def move_rectangle_horizontally(matrix, single_rectangle, matrix_borders, horizontal_movement):
	total_height = np.shape(matrix)[0]
	total_width = np.shape(matrix)[1]

	image_left_border, image_right_border, image_top_border, image_bottom_border = matrix_borders

	rectangle_type = single_rectangle[1]
	rectangle_row = single_rectangle[2] - image_top_border
	rectangle_col = single_rectangle[3] - image_left_border
	rectangle_width = single_rectangle[4]
	rectangle_height = single_rectangle[5]

	# First, remove the rectangle
	remove_rectangle(matrix, single_rectangle, matrix_borders)

	# show_matrix(matrix)

	new_col = rectangle_col + horizontal_movement

	if new_col < 0:
		new_col = 0

	if new_col >= total_width:
		new_col = total_width

	# print(f"Old column = {rectangle_col}, new column = {new_col}")

	status = 1

	matrix, status = place_rectangle(matrix, rectangle_row, new_col, rectangle_width, rectangle_height, rectangle_type)

	if status == 1:
		single_rectangle[3] = new_col + image_left_border

	# print(status)

	if status == -1:
		matrix, _ = place_rectangle(matrix, rectangle_row, rectangle_col, rectangle_width, rectangle_height,
										 rectangle_type)

	return matrix, status


def move_rectangle_vertically(matrix, single_rectangle, matrix_borders, vertical_movement):
	total_height = np.shape(matrix)[0]
	total_width = np.shape(matrix)[1]

	image_left_border, image_right_border, image_top_border, image_bottom_border = matrix_borders

	rectangle_type = single_rectangle[1]
	rectangle_row = single_rectangle[2] - image_top_border
	rectangle_col = single_rectangle[3] - image_left_border
	rectangle_width = single_rectangle[4]
	rectangle_height = single_rectangle[5]

	# First, remove the rectangle
	remove_rectangle(matrix, single_rectangle, matrix_borders)

	new_row = rectangle_row + vertical_movement

	if new_row < 0:
		new_row = 0

	if new_row >= total_height:
		new_row = total_height

	matrix, status = place_rectangle(matrix, new_row, rectangle_col, rectangle_width, rectangle_height, rectangle_type)

	if status == 1:
		single_rectangle[2] = new_row + image_top_border

	if status == -1:
		matrix, _ = place_rectangle(matrix, rectangle_row, rectangle_col, rectangle_width, rectangle_height,
									rectangle_type)

	return matrix, status


def move_rectangle(matrix, single_rectangle, matrix_borders, vertical_movement, horizontal_movement, num_movements):
	total_movements = 0
	status_vertical = 1
	status_horizontal = 1

	while (total_movements < num_movements) and ((status_vertical == 1) or (status_horizontal == 1)):
		total_movements += 1
		# matrix, status_vertical = move_rectangle_vertically(matrix, single_rectangle, matrix_borders, vertical_movement)
		# matrix, status_horizontal = move_rectangle_horizontally(matrix, single_rectangle, matrix_borders, horizontal_movement)
		matrix, status_vertical = move_single_rectangle(matrix, single_rectangle, matrix_borders,
																0, vertical_movement)
		matrix, status_horizontal = move_single_rectangle(matrix, single_rectangle, matrix_borders,
														  horizontal_movement, 0)


	return matrix


def move_many_rectangles(original_matrix, rectangle_allocation, matrix_borders):
	image_left_border, image_right_border, image_top_border, image_bottom_border = matrix_borders

	matrix = np.copy(original_matrix)

	total_height = np.shape(matrix)[0]
	total_width = np.shape(matrix)[1]

	num_movements = 100

	for iteration in range(10):

		print(f"iteration = {iteration}")

		for single_rectangles in rectangle_allocation:
			# single_rectangles = rectangle_allocation[0]
			rectangle_row = single_rectangles[2] - image_top_border
			rectangle_col = single_rectangles[3] - image_left_border
			rectangle_width = single_rectangles[4]
			rectangle_height = single_rectangles[5]

			if (rectangle_row + 0.5*rectangle_height) < 0.5*total_height:
				vertical_movement = 1
			else:
				vertical_movement = -1

			if (rectangle_col + 0.5*rectangle_width) < 0.5*total_width:
				horizontal_movement = 1
			else:
				horizontal_movement = -1

			matrix = move_rectangle(matrix, single_rectangles, matrix_borders, vertical_movement, horizontal_movement,
						   num_movements)

	return matrix


num_r = int(round(1484*1))
num_c = int(round(1000*1))

# rectangle_dimensions = np.array([[30, 40], [20, 27], [15, 20], [10, 15]])
# number_of_rectangles = [5, 10, 20, 30]
# border = [150, 130, 140, 150]

different_types, number_of_rectangles_dict, image_names_per_type = get_image_information()

# different_types = [10, 9, 8, 7, 6]

# number_of_rectangles_dict = {10: 5, 9: 5, 8: 6, 7: 5, 6: 10}

aspect_ratio = 1484/1000  # 100/60

rectangle_dimensions_dict = {10: [100, int(round(aspect_ratio*100))],  # 60
							 9: [35, int(round(aspect_ratio*35))],
							 8: [30, int(round(aspect_ratio*30))],
							 7: [25, int(round(aspect_ratio*25))],
							 6: [20, int(round(aspect_ratio*20))]}
border_dict = {10: 200, 9: 200, 8: 200, 7: 200, 6: 200}

bleed = 10

matrix, rectangle_allocation, matrix_borders = allocate_rectangles(num_r, num_c, different_types, rectangle_dimensions_dict, number_of_rectangles_dict, border_dict, bleed)

# print(rectangle_allocation)

# show_matrix(matrix)

matrix_1 = matrix

matrix_2 = move_many_rectangles(matrix, rectangle_allocation, matrix_borders)

new_matrix_borders = find_borders(matrix_2, bleed)

old_image_left_border, old_image_right_border, old_image_top_border, old_image_bottom_border = matrix_borders
new_image_left_border, new_image_right_border, new_image_top_border, new_image_bottom_border = new_matrix_borders

new_matrix_borders_2 = old_image_left_border + new_image_left_border, old_image_right_border + new_image_right_border, \
					old_image_top_border + new_image_top_border, old_image_bottom_border + new_image_bottom_border

create_latex_file(rectangle_allocation, matrix_borders, image_names_per_type)

# for single_rectangles in rectangle_allocation:
# 	print(single_rectangles)
# 	remove_rectangle(matrix, single_rectangles, matrix_borders)


# show_matrix(matrix)

compare_matrices(matrix_1, matrix_2)

# show_matrix(matrix_1)

print('Ready')