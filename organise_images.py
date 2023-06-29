import os.path, time
from PIL import Image, ExifTags
from os import walk, rename
import pillow_heif

folder_path = 'other_images'
new_path = folder_path + '/' + 'all_photos_and_images'

if not os.path.exists(new_path):
    os.makedirs(new_path)

copy_file_extensions = ['.jpg', '.jpeg', '.png']

file_names = []

heic_files_count = 0

for (dirpath, dirnames, filenames) in walk(folder_path):
	# print(f'dirpath = {dirpath}')
	# print(f'dirnames = {dirnames}')
	# print(f'filenames = {filenames}\n\n')
	for single_file in filenames:
		complete_path = dirpath + '/' + single_file
		_, file_extension = os.path.splitext(complete_path)
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
		if file_extension.lower() in copy_file_extensions:
			file_names.append(complete_path)



for img_path in file_names:

	_, file_extension = os.path.splitext(img_path)
	img = Image.open(img_path)

	image_exif = img._getexif()

	if image_exif is not None:
		exif = { ExifTags.TAGS[k]: v for k, v in image_exif.items() if k in ExifTags.TAGS }
		original_time = exif['DateTimeOriginal']
		creation_time = original_time[0:4] + '_' + original_time[5:7] + '_' + original_time[8:10] + '_' + \
						original_time[11:13] + '_' + original_time[14:16] + '_' + original_time[17:19]

	else:
		# print('No Exif')
		original_time = time.gmtime(os.stat(img_path).st_birthtime)
		creation_time = str(original_time.tm_year) + '_' + str(original_time.tm_mon).zfill(2) + '_' + \
						str(original_time.tm_mday).zfill(2) + '_' + str(original_time.tm_hour).zfill(2) \
						+ '_' + str(original_time.tm_min).zfill(2) + '_' + \
						str(original_time.tm_sec).zfill(2)

	original_name = img_path
	new_name = new_path + '/' + creation_time + file_extension.lower()
	# print(f"{img_path} -> {new_path}/{creation_time}{file_extension.lower()}")
	rename(original_name, new_name)


