import pandas as pd

def get_image_information():

	# images_information = pd.read_excel('images_information.xlsx')
	images_information = pd.read_excel('images_information_v2.xlsx')

	# Get the unique values of type
	type_values = images_information.Type.unique()

	image_names_per_type = dict()
	number_images_per_type = dict()

	for image_type in type_values:
		image_names_per_type[image_type] = []
		number_images_per_type[image_type] = 0

	for row in images_information.index:
		card_name = images_information['Name'][row]
		card_type = images_information['Type'][row]

		card_name.replace(':', '')

		image_names_per_type[card_type].append(card_name)
		number_images_per_type[card_type] = number_images_per_type[card_type] + 1

	return type_values, number_images_per_type, image_names_per_type


type_values, number_images_per_type, image_names_per_type = get_image_information()

print(type_values)
print(number_images_per_type)
print(image_names_per_type)

