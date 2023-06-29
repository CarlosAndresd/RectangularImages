import os.path, time
from PIL import Image, ExifTags
from os import walk, rename
import pillow_heif

folder_path = 'other_images'
resulting_folder = 'resulting_images'
new_path = resulting_folder + '/' + 'all_photos_and_images'
heic_path = resulting_folder + '/' + 'heic_photos_and_images'

if not os.path.exists(new_path):
    os.makedirs(new_path)

if not os.path.exists(heic_path):
    os.makedirs(heic_path)

copy_file_extensions = ['.jpg', '.jpeg', '.png']

file_names = []

heic_files_count = 0
assigned_heic_names = []

for (dirpath, dirnames, filenames) in walk(folder_path):
	# print(f'dirpath = {dirpath}')
	# print(f'dirnames = {dirnames}')
	# print(f'filenames = {filenames}\n\n')
	for single_file in filenames:
		complete_path = dirpath + '/' + single_file
		file_name, file_extension = os.path.splitext(complete_path)
		if file_extension.lower() == '.heic':
			# print('heic file!')
			heic_files_count += 1
			# This is too slow and creates very big files. For now it is better to do this manually
			# heif_file = pillow_heif.read_heif(complete_path)
			# image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw", )
			# file_name, _ = os.path.splitext(complete_path)
			# file_extension = '.png'
			# complete_path = file_name + file_extension
			# image.save(complete_path, format(file_extension))

			file_name = os.path.basename(file_name)
			new_name = heic_path + '/' + file_name + file_extension

			if new_name in assigned_heic_names:
				repeated_counter = 0
				repeated_name = True
				while repeated_name:
					repeated_counter += 1
					new_name = heic_path + '/' + file_name + '_' + str(repeated_counter) + file_extension
					if not (new_name in assigned_heic_names):
						repeated_name = False

			print(f"{complete_path} -> {new_name}")
			rename(complete_path, new_name)
			assigned_heic_names.append(new_name)

		if file_extension.lower() in copy_file_extensions:
			file_names.append(complete_path)

assigned_names = []

for img_path in file_names:

	_, file_extension = os.path.splitext(img_path)
	img = Image.open(img_path)

	image_exif = img._getexif()

	original_time = None

	if image_exif is not None:
		exif = { ExifTags.TAGS[k]: v for k, v in image_exif.items() if k in ExifTags.TAGS }

		if 'DateTimeOriginal' in exif.keys():

			original_time = exif['DateTimeOriginal']
			creation_time = original_time[0:4] + '_' + original_time[5:7] + '_' + original_time[8:10] + '_' + \
							original_time[11:13] + '_' + original_time[14:16] + '_' + original_time[17:19]

	if original_time is None:
		# print('No Exif')
		original_time = time.gmtime(os.stat(img_path).st_birthtime)
		creation_time = str(original_time.tm_year) + '_' + str(original_time.tm_mon).zfill(2) + '_' + \
						str(original_time.tm_mday).zfill(2) + '_' + str(original_time.tm_hour).zfill(2) \
						+ '_' + str(original_time.tm_min).zfill(2) + '_' + \
						str(original_time.tm_sec).zfill(2)

	original_name = img_path
	new_name = new_path + '/' + creation_time + file_extension.lower()
	# print(f"{img_path} -> {new_path}/{creation_time}{file_extension.lower()}")
	if new_name in assigned_names:
		repeated_counter = 0
		repeated_name = True
		while repeated_name:
			repeated_counter += 1
			new_name = new_path + '/' + creation_time + '_' + str(repeated_counter) + file_extension.lower()
			if not(new_name in assigned_names):
				repeated_name = False

	rename(original_name, new_name)
	print(f"{original_name} -> {new_name}")
	assigned_names.append(new_name)


