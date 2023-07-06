"""

=====================================================================
move_chronologically, (:mod:`RectangularImages.move_chronologically`)
=====================================================================

Description
-----------

    This module contains has one single function: organise all the files in a selected directory by date, either created
    date or modified date. It is primarily aimed at photos, since it looks for the exif information, but it should work
    with any file.

    Important! If the file contains exif information and the selected date is the creation date, the program will take
    the creation date from the exif metadata. Keep in mind that this creation date does not account for different time
    zones, it always uses UTC.

Functions
---------

    - create_year_directory
    - find_all_files
    - get_file_date
    - create_file_name_from_date
    - move_files


Related files/directories
-------------------------

    This module has three related files/directories:

    - tests_move_chronologically.py: script that contains all the tests.
    - reference_test_directory: this is the directory that contains all the files that are used for the testing.
    - Test_Photo_Information.xlsx: this is the Excel file that can be used to write the tests.


Examples
--------

    Imagine you want to organise the files contained in the directory 'dir_A' and move them to a new directory called
    'dir_B'. But not all the files, just the '.jpg' and '.heic' files. And you want to organise them by created date.
    Then you should type

    python move_chronologically.py -s dir_A -d dir_B -e .jpg .heic

    You probably saw a lot of output, depending on the number of files. If you prefer to mute the program you could type

    python move_chronologically.py -s dir_A -d dir_B -e .jpg .heic -m true

    Now, then the files where moved they kept their original name, but maybe you would also like the file name to
    reflect the creation/modification date, in that case you should type

    python move_chronologically.py -s dir_A -d dir_B -e .jpg .heic -m true -r true

    Finally, if you want to order the files by modified date instead of created date, you can type

    python move_chronologically.py -s dir_A -d dir_B -e .jpg .heic -m true -r true -t modified


"""

import os.path
import time
from PIL import Image, ExifTags
from os import walk, rename
import argparse
import shutil
import textwrap


def create_year_directory(year, source_path):
	"""

	This function creates a new directory for the given year and inside that directory it creates 12 directories for
	each month

	Parameters
	----------
	year: the name of the main directory
	source_path: the path where the directory will be created

	Returns
	-------
	None

	"""
	year_path = source_path + '/' + year
	os.makedirs(year_path)

	for month_number in range(12):
		month_path = year_path + '/' + year + '_' + str(month_number + 1).zfill(2)
		os.makedirs(month_path)


def find_all_files(source_directory_path, copy_file_extensions=''):
	"""

	This function finds all the files inside the given directory that have the provided extensions. It ignores
	'.DS_Store' files

	Parameters
	----------
	source_directory_path: path of the directory where to look
	copy_file_extensions: a tuple containing the extensions to look for. If any extension is allowed, then it is an
	empty string

	Returns
	-------
	A list containing all the found files with relative path

	"""
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
	"""

	This function gets the desired date from a file. Either the created or the modified date.

	Important! If the file contains exif information and the selected date is the creation date, the program will take
    the creation date from the exif metadata. Keep in mind that this creation date does not account for different time
    zones, it always uses UTC.

	Parameters
	----------
	file_path: the path of the file.
	which_date: either 'created' or 'modified'. By default, it is 'created'. If it is none of these strings, then it
	becomes 'created'

	Returns
	-------
	A tuple containing the information of the file creation/modification date

	"""

	which_date = which_date.lower()

	if which_date != 'created' and which_date != 'modified':
		which_date = 'created'

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
	"""

	This function takes the file date and transforms it into a string

	Parameters
	----------
	file_date: the tuple with file date information

	Returns
	-------
	The string with the file date

	"""
	return '_'.join(file_date)


def create_new_complete_file_path(assigned_names, assigned_years, file_date, new_file_path, destination_path,
								  file_extension, new_file_name):
	"""

	This function creates the new complete path for the given file. It checks whether there are other files with that
	name and if so it adds a number

	Parameters
	----------
	assigned_names: list of all the names that have been assigned
	assigned_years: list of all the years that have been assigned
	file_date: the date of the file (tuple)
	new_file_path: the path where the images are moved to
	destination_path: path of the destination (I am not sure what is the difference with 'new_file_path')
	file_extension: the extension of the file
	new_file_name: the new file name, it could be the old file name or a new one depending on the date

	Returns
	-------
	A string with the new file path

	"""
	file_year, file_month, file_day, file_hour, file_min, file_sec = file_date
	new_complete_file_path = new_file_path + '/' + new_file_name + file_extension.lower()

	if new_complete_file_path in assigned_names:
		repeated_counter = 0
		repeated_name = True
		while repeated_name:
			repeated_counter += 1
			new_complete_file_path = new_file_path + '/' + new_file_name + '_' + str(
				repeated_counter) + file_extension.lower()
			if not (new_complete_file_path in assigned_names):
				repeated_name = False

	if not (file_year in assigned_years):
		create_year_directory(str(file_year), destination_path)
		assigned_years.append(file_year)

	return new_complete_file_path


def move_files(source_path='other_images', resulting_path='resulting_images',
			   copy_file_extensions=('.jpg', '.jpeg', '.png'), sorting_date='created', new_name=True, mute=False,
			   copy=False):
	"""

	This is the function that actually moves the files depending on the information provided by the user.

	Parameters
	----------
	source_path: this is the path to the source directory, by default it is 'other_images'
	resulting_path: this is the path to the destination directory, by default it is 'resulting_images'
	copy_file_extensions: these are the extensions that will be moved or copied, by default they are '.jpg', '.jpeg', '.png'
	sorting_date: variable deciding whether the sorting date is the created or modified date, by default is created
	new_name: variable that decides whether the file name changes or not
	mute: variable that decides whether the copying/moving process is shown or not. By default, it shows the progress
	copy: variable that decides whether the files are copied or not. By default it moves the files

	Returns
	-------
	None

	"""
	if not os.path.exists(resulting_path):
		os.makedirs(resulting_path)

	file_names = find_all_files(source_path, copy_file_extensions)

	assigned_names = []
	assigned_years = []

	for original_complete_file_path in file_names:

		original_file_path, _ = os.path.splitext(original_complete_file_path)
		original_file_name, file_extension = os.path.splitext(os.path.basename(original_complete_file_path))

		file_date = get_file_date(original_complete_file_path, which_date=sorting_date)
		file_year, file_month, file_day, file_hour, file_min, file_sec = file_date

		new_file_path = resulting_path + '/' + file_year + '/' + file_year + '_' + file_month

		if new_name:
			new_complete_file_path = create_new_complete_file_path(assigned_names, assigned_years, file_date,
																   new_file_path, resulting_path, file_extension,
																   create_file_name_from_date(file_date))
		else:
			new_complete_file_path = create_new_complete_file_path(assigned_names, assigned_years, file_date,
																   new_file_path, resulting_path, file_extension,
																   original_file_name)

		if not mute:
			print(f"{original_complete_file_path} -> {new_complete_file_path}")

		if copy:
			shutil.copy2(original_complete_file_path, new_complete_file_path)
		else:
			rename(original_complete_file_path, new_complete_file_path)

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

	parser.add_argument('-s', '--source', default='source_images',
						help="this is the path to the source directory, by default it is 'other_images'")
	parser.add_argument('-d', '--destination', default='resulting_images',
						help="this is the path to the destination directory, by default it is 'resulting_images'")
	parser.add_argument('-e', '--extension', nargs='+', default=('.jpg', '.jpeg', '.png'),
						help="these are the extensions that will be moved or copied, by default they are '.jpg', '.jpeg', '.png'")
	parser.add_argument('-m', '--mute', default='false',
						help="variable that decides whether the copying/moving process is shown or not. By default, it shows the progress")
	parser.add_argument('-c', '--copy', default='false',
						help="variable that decides whether the files are copied or not. By default it moves the files")
	parser.add_argument('-r', '--rename', default='false',
						help="variable that decides whether the file name changes or not")
	parser.add_argument('-t', '--sorting', default='created',
						help="variable deciding whether the sorting date is the created or modified date, by default is created")

	args = parser.parse_args()

	folder_path = args.source
	resulting_folder = args.destination
	extension = args.extension

	if args.mute == 'false':
		mute = False
	else:
		mute = True

	if args.copy == 'false':
		copy = False
	else:
		copy = True

	if args.rename == 'false':
		file_rename = False
	else:
		file_rename = True

	move_files(source_path=folder_path, resulting_path=resulting_folder, copy_file_extensions=extension,
			   sorting_date=args.sorting, new_name=file_rename, mute=mute, copy=copy)
