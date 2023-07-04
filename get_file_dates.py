from PIL import Image, ExifTags
import os.path, time
from os import walk


def find_all_files(source_directory_path, copy_file_extensions=''):
	file_names = []

	for (directory_path, _, filenames) in walk(source_directory_path):
		for single_file in filenames:
			if single_file != '.DS_Store':
				# print(single_file)
				complete_path = directory_path + '/' + single_file
				_, file_extension = os.path.splitext(complete_path)

				if copy_file_extensions == '':
					file_names.append(complete_path)
				else:
					if file_extension.lower() in copy_file_extensions:
						file_names.append(complete_path)

	return file_names


def get_file_date(file_path, which_date='created'):
	if which_date == 'created':

		try:
			img = Image.open(file_path)
			image_exif = img._getexif()
			original_time = None

			if image_exif is not None:
				exif = {ExifTags.TAGS[k]: v for k, v in image_exif.items() if k in ExifTags.TAGS}

				if 'DateTimeOriginal' in exif.keys():
					original_time = exif['DateTimeOriginal']
					file_year = original_time[0:4]
					file_month = original_time[5:7]
					file_day = original_time[8:10]
					file_hour = original_time[11:13]
					file_min = original_time[14:16]
					file_sec = original_time[17:19]

		except:
			original_time = None

		if original_time is None:
			original_time = time.gmtime(os.stat(file_path).st_birthtime)

			file_year = str(original_time.tm_year)
			file_month = str(original_time.tm_mon).zfill(2)
			file_day = str(original_time.tm_mday).zfill(2)
			file_hour = str(original_time.tm_hour).zfill(2)
			file_min = str(original_time.tm_min).zfill(2)
			file_sec = str(original_time.tm_sec).zfill(2)

		return file_year, file_month, file_day, file_hour, file_min, file_sec

	elif which_date == 'modified':

		original_time = time.gmtime(os.path.getmtime(file_path))

		file_year = str(original_time.tm_year)
		file_month = str(original_time.tm_mon).zfill(2)
		file_day = str(original_time.tm_mday).zfill(2)
		file_hour = str(original_time.tm_hour).zfill(2)
		file_min = str(original_time.tm_min).zfill(2)
		file_sec = str(original_time.tm_sec).zfill(2)

		return file_year, file_month, file_day, file_hour, file_min, file_sec


def create_file_name_from_date(file_date):
	return '_'.join(file_date)


directory_path = 'reference_test_files'
all_file_names = find_all_files(directory_path, copy_file_extensions='')

for file_path in all_file_names:
	created_date = create_file_name_from_date(get_file_date(file_path, which_date='created'))
	modified_date = create_file_name_from_date(get_file_date(file_path, which_date='modified'))
	print(f'{file_path}     \t{created_date}\t\t{modified_date}')


