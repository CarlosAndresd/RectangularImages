import pandas as pd

images_information = pd.read_excel('images_information.xlsx')
num_rows = images_information.shape[0]

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

	image_names_per_type[card_type].append(card_name)

	number_images_per_type[card_type] = number_images_per_type[card_type] + 1


print(images_information)

