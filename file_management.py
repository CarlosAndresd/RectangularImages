from os import walk
import os.path


root_sorted_path = 'sorted_images'
name_source_path = 'images_GUI'


def find_all_files(source_directory_path=name_source_path, copy_file_extensions=('.jpg', '.png', '.jpeg'), filter_results=True):
	file_names = []

	for (directory_path, directory_name, filenames) in walk(source_directory_path):
		if (not (root_sorted_path in directory_path)) or not filter_results:
			for single_file in filenames:
				if single_file != '.DS_Store':
					# print(single_file)
					complete_path = directory_path + '/' + single_file
					_, file_extension = os.path.splitext(complete_path)

					if file_extension.lower() in copy_file_extensions:
						file_names.append(complete_path)

	return file_names


all_file_names = find_all_files(filter_results=False)

for file_name in all_file_names:
	print("\t'" + file_name + "',")

