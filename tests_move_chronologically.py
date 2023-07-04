import pytest
from move_chronologically import *


def test_find_all_files_1():
	correct_answer = {
		'test_directory/dir_1/dir_4/dir_8/dir_9/file_6.HEIC',
		'test_directory/dir_1/dir_4/dir_8/dir_9/file_14.HEIC',
		'test_directory/dir_1/dir_4/dir_8/dir_9/file_16.HEIC',
		'test_directory/dir_1/dir_4/dir_8/file_5.HEIC',
		'test_directory/dir_1/dir_4/file_1.HEIC',
		'test_directory/dir_1/dir_5/dir_10/file_24.HEIC',
		'test_directory/dir_1/dir_5/file_12.HEIC',
		'test_directory/dir_1/dir_5/file_26.HEIC',
		'test_directory/dir_1/file_1.HEIC',
		'test_directory/dir_2/dir_6/file_21.HEIC',
		'test_directory/dir_2/dir_6/file_24.HEIC',
		'test_directory/dir_2/file_6.HEIC',
		'test_directory/dir_2/file_8.HEIC',
		'test_directory/dir_2/file_16.HEIC',
		'test_directory/dir_3/file_1.HEIC',
		'test_directory/dir_3/file_5.HEIC',
		'test_directory/dir_3/file_10.HEIC',
		'test_directory/dir_3/file_12.HEIC',
		'test_directory/dir_3/file_25.HEIC',
		'test_directory/file_1.HEIC',
		'test_directory/file_12.HEIC',
		'test_directory/file_24.HEIC',
		'test_directory/dir_1/dir_4/dir_8/dir_9/file_7.JPG',
		'test_directory/dir_1/dir_4/dir_8/dir_9/file_22.JPG',
		'test_directory/dir_1/dir_4/dir_8/file_17.jpg',
		'test_directory/dir_1/dir_5/dir_10/file_7.JPG',
		'test_directory/dir_1/file_3.JPG',
		'test_directory/dir_1/file_15.JPG',
		'test_directory/dir_2/dir_6/file_3.JPG',
		'test_directory/dir_2/file_3.JPG',
		'test_directory/dir_3/file_15.JPG',
		'test_directory/dir_3/file_19.JPG',
		'test_directory/dir_3/file_22.JPG',
		'test_directory/file_15.JPG',
		'test_directory/dir_1/dir_4/file_4.png',
		'test_directory/dir_1/dir_4/file_13.PNG',
		'test_directory/dir_1/dir_4/file_18.PNG',
		'test_directory/dir_1/dir_5/file_2.png',
		'test_directory/dir_1/file_2.png',
		'test_directory/dir_1/file_4.png',
		'test_directory/dir_2/dir_6/file_9.png',
		'test_directory/dir_2/dir_7/file_20.png',
		'test_directory/dir_2/file_2.png',
		'test_directory/dir_3/file_4.png',
		'test_directory/file_20.png',
		'test_directory/dir_1/file_11.jpeg',
		'test_directory/dir_2/dir_7/file_11.jpeg',
		'test_directory/dir_2/file_23.jpeg',
	}

	assert set(find_all_files('test_directory')) == correct_answer


def test_find_all_files_2():
	correct_answer = ['test_directory/0b0a9861-9f3d-4801-94dd-9c9db7056889.JPG',
					'test_directory/2014-12-27 14.21.16.jpg',
					'test_directory/directory_2/5QpPfOY-mathematics-wallpaper.jpg',
					'test_directory/directory_2/find_name/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/directory_2/find_name/8fad5998-c87f-4155-98be-0ae52ae3e666.JPG',
					'test_directory/other_files/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/directory_1/folder_a/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/directory_1/folder_1/IMG_5246.JPG',
					'test_directory/more_files/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/more_files/0b0a9861-9f3d-4801-94dd-9c9db7056889.JPG',
					'test_directory/more_files/forest/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/more_files/mountains/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/more_files/mountains/IMG_0251.JPG',
					'test_directory/more_files/mountains/lakes/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/more_files/mountains/lakes/IMG_5246.JPG',
					'test_directory/more_files/mountains/lakes/IMG_3229.JPG']

	assert set(find_all_files('test_directory', copy_file_extensions='.jpg')) == set(correct_answer)


def test_find_all_files_3():
	correct_answer = ['test_directory/directory_2/2014-08-10 10.46.40.png',
					'test_directory/directory_2/IMG_5050.HEIC',
					'test_directory/directory_2/IMG_0160.HEIC',
					'test_directory/directory_2/find_name/2014-12-26 10.16.44.png',
					'test_directory/directory_2/find_name/IMG_4847.HEIC',
					'test_directory/other_files/IMG_5041.PNG',
					'test_directory/other_files/IMG_4847.HEIC',
					'test_directory/other_files/IMG_0160.HEIC',
					'test_directory/directory_1/IMG_8777.PNG',
					'test_directory/directory_1/IMG_0240.HEIC',
					'test_directory/directory_1/IMG_5041.PNG',
					'test_directory/directory_1/IMG_9116.PNG',
					'test_directory/directory_1/IMG_0170.HEIC',
					'test_directory/directory_1/IMG_0160.HEIC',
					'test_directory/directory_1/folder_a/IMG_5050.HEIC',
					'test_directory/directory_1/folder_a/more_images/IMG_8549.PNG',
					'test_directory/directory_1/folder_a/more_images/IMG_6318.HEIC',
					'test_directory/directory_1/folder_a/more_images/IMG_4847.HEIC',
					'test_directory/directory_1/folder_1/IMG_5097.HEIC',
					'test_directory/directory_1/folder_1/IMG_6100.HEIC',
					'test_directory/directory_1/folder_1/IMG_5096.HEIC',
					'test_directory/directory_1/folder_1/IMG_6095.HEIC',
					'test_directory/more_files/IMG_5041.PNG',
					'test_directory/more_files/IMG_0170.HEIC',
					'test_directory/more_files/forest/IMG_0240.HEIC',
					'test_directory/more_files/mountains/lakes/IMG_4455.HEIC',
					'test_directory/more_files/mountains/lakes/IMG_5041.PNG',
					'test_directory/more_files/mountains/lakes/IMG_3156.HEIC']

	assert set(find_all_files('test_directory', copy_file_extensions=('.heic', '.png'))) == set(correct_answer)


def test_get_file_date_1():
	created_date = get_file_date('test_directory/directory_1/IMG_8777.PNG')
	correct_answer = ('2021', '07', '27', '15', '31', '18')

	assert created_date == correct_answer


def test_get_file_date_2():
	created_date = get_file_date('test_directory/directory_1/folder_1/IMG_6100.HEIC', which_date='created')
	correct_answer = ('2023', '03', '11', '10', '08', '29')

	assert created_date == correct_answer


