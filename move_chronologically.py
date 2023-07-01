import os.path, time
from PIL import Image, ExifTags
from os import walk, rename
import argparse
import shutil
import textwrap


def create_year_directory(year, source_path):
	year_path = source_path + '/' + year
	os.makedirs(year_path)

	for month_number in range(12):
		month_path = year_path + '/' + year + '_' + str(month_number + 1).zfill(2)
		os.makedirs(month_path)


def find_all_files(source_directory_path, copy_file_extensions=''):
	file_names = []

	for (directory_path, _, filenames) in walk(source_directory_path):
		for single_file in filenames:
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


def create_new_complete_file_path(assigned_names, assigned_years, file_date, new_file_path, destination_path, file_extension):

	file_year, file_month, file_day, file_hour, file_min, file_sec = file_date
	new_file_name = create_file_name_from_date(file_date)
	new_complete_file_path = new_file_path + '/' + new_file_name + file_extension.lower()

	if new_complete_file_path in assigned_names:
		repeated_counter = 0
		repeated_name = True
		while repeated_name:
			repeated_counter += 1
			new_complete_file_path = new_file_path + '/' + new_file_name + '_' + str(repeated_counter) + file_extension.lower()
			if not (new_complete_file_path in assigned_names):
				repeated_name = False

	if not (file_year in assigned_years):
		create_year_directory(str(file_year), destination_path)
		assigned_years.append(file_year)

	return new_complete_file_path


def move_files(source_path='other_images', resulting_path='resulting_images', copy_file_extensions=('.jpg', '.jpeg', '.png'), new_name=True):
	if not os.path.exists(resulting_path):
		os.makedirs(resulting_path)

	file_names = find_all_files(source_path, copy_file_extensions)

	assigned_names = []
	assigned_years = []

	for original_complete_file_path in file_names:

		original_file_path, _ = os.path.splitext(original_complete_file_path)
		original_file_name, file_extension = os.path.splitext(os.path.basename(original_complete_file_path))

		file_date = get_file_date(original_complete_file_path)
		file_year, file_month, file_day, file_hour, file_min, file_sec = file_date

		new_file_path = resulting_path + '/' + file_year + '/' + file_year + '_' + file_month

		if new_name:
			new_complete_file_path = create_new_complete_file_path(assigned_names, assigned_years, file_date, new_file_path, resulting_path, file_extension)
		else:
			new_complete_file_path = new_file_path + '/' + original_file_name + file_extension.lower()

		if mute == 'false':
			print(f"{original_complete_file_path} -> {new_complete_file_path}")

		if copy == 'false':
			rename(original_complete_file_path, new_complete_file_path)
		else:
			shutil.copy2(original_complete_file_path, new_complete_file_path)

		assigned_names.append(new_complete_file_path)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
									 description=textwrap.dedent('''
									
									
									
									Organise files by date in a separate directory. The name of the files may change to be the date of creation
									
									
									
									'''),
									 epilog=textwrap.dedent('''
			Some examples:
			--------------
			
			Example 1:
			python move_chronologically.py -s other_images -d results -e .jpg .heic -m true
			
			Example 2:
			python move_chronologically.py -s other_images -d results -e .jpg .heic .png
			
			.
	         '''))

	parser.add_argument('-s', '--source', default='other_images',
						help="this is the path to the source directory, by default it is 'other_images'")
	parser.add_argument('-d', '--destination', default='resulting_images',
						help="this is the path to the destination directory, by default it is 'resulting_images'")
	parser.add_argument('-e', '--extension', nargs='+', default=('.jpg', '.jpeg', '.png'),
						help="these are the extensions that will be moved or copied, by default they are '.jpg', '.jpeg', '.png'")
	parser.add_argument('-m', '--mute', default='false',
						help="boolean variable that decides whether the copying/moving process is shown or not. By default, it shows the progress")
	parser.add_argument('-c', '--copy', default='false',
						help="boolean variable that decides whether the files are copied or not. By default it moves the files")
	parser.add_argument('-r', '--rename', default='false',
						help="boolean variable that decides whether the file name changes or not")

	args = parser.parse_args()

	folder_path = args.source
	resulting_folder = args.destination
	extension = args.extension
	mute = args.mute
	copy = args.copy
	file_rename = args.rename

	move_files(source_path=folder_path, resulting_path=resulting_folder, copy_file_extensions=extension)
