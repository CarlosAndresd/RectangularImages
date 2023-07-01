import pytest
from move_chronologically import *


def test_find_all_files_1():
	correct_answer = ['test_directory/0b0a9861-9f3d-4801-94dd-9c9db7056889.JPG',
					'test_directory/2014-12-27 14.21.16.jpg',
					'test_directory/directory_2/2014-08-10 10.46.40.png',
					'test_directory/directory_2/5QpPfOY-mathematics-wallpaper.jpg',
					'test_directory/directory_2/IMG_5050.HEIC',
					'test_directory/directory_2/IMG_0160.HEIC',
					'test_directory/directory_2/find_name/2014-12-26 10.16.44.png',
					'test_directory/directory_2/find_name/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/directory_2/find_name/IMG_4847.HEIC',
					'test_directory/directory_2/find_name/8fad5998-c87f-4155-98be-0ae52ae3e666.JPG',
					'test_directory/other_files/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/other_files/IMG_5041.PNG',
					'test_directory/other_files/IMG_4847.HEIC',
					'test_directory/other_files/IMG_0160.HEIC',
					'test_directory/directory_1/IMG_8777.PNG',
					'test_directory/directory_1/IMG_0240.HEIC',
					'test_directory/directory_1/IMG_5041.PNG',
					'test_directory/directory_1/IMG_9116.PNG',
					'test_directory/directory_1/IMG_0170.HEIC',
					'test_directory/directory_1/IMG_0160.HEIC',
					'test_directory/directory_1/folder_a/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/directory_1/folder_a/IMG_5050.HEIC',
					'test_directory/directory_1/folder_a/more_images/IMG_8549.PNG',
					'test_directory/directory_1/folder_a/more_images/IMG_6318.HEIC',
					'test_directory/directory_1/folder_a/more_images/IMG_4847.HEIC',
					'test_directory/directory_1/folder_1/IMG_5097.HEIC',
					'test_directory/directory_1/folder_1/IMG_5246.JPG',
					'test_directory/directory_1/folder_1/IMG_6100.HEIC',
					'test_directory/directory_1/folder_1/IMG_5096.HEIC',
					'test_directory/directory_1/folder_1/IMG_6095.HEIC',
					'test_directory/more_files/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/more_files/0b0a9861-9f3d-4801-94dd-9c9db7056889.JPG',
					'test_directory/more_files/IMG_5041.PNG',
					'test_directory/more_files/IMG_0170.HEIC',
					'test_directory/more_files/forest/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/more_files/forest/IMG_0240.HEIC',
					'test_directory/more_files/mountains/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/more_files/mountains/IMG_0251.JPG',
					'test_directory/more_files/mountains/lakes/IMG_4455.HEIC',
					'test_directory/more_files/mountains/lakes/f4492873-3889-40e7-99b7-b75e729881c8.JPG',
					'test_directory/more_files/mountains/lakes/IMG_5246.JPG',
					'test_directory/more_files/mountains/lakes/IMG_5041.PNG',
					'test_directory/more_files/mountains/lakes/IMG_3156.HEIC',
					'test_directory/more_files/mountains/lakes/IMG_3229.JPG']

	assert find_all_files('test_directory') == correct_answer


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


