import pytest
from move_chronologically import *
import subprocess


def test_find_all_files_1():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	answer = set(find_all_files(name_source_path))

	shutil.rmtree('test_results')

	correct_answer = {
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_6.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_14.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_16.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/file_5.HEIC',
		'test_results/test_directory/dir_1/dir_4/file_1.HEIC',
		'test_results/test_directory/dir_1/dir_5/dir_10/file_24.HEIC',
		'test_results/test_directory/dir_1/dir_5/file_12.HEIC',
		'test_results/test_directory/dir_1/dir_5/file_26.HEIC',
		'test_results/test_directory/dir_1/file_1.HEIC',
		'test_results/test_directory/dir_2/dir_6/file_21.HEIC',
		'test_results/test_directory/dir_2/dir_6/file_24.HEIC',
		'test_results/test_directory/dir_2/file_6.HEIC',
		'test_results/test_directory/dir_2/file_8.HEIC',
		'test_results/test_directory/dir_2/file_16.HEIC',
		'test_results/test_directory/dir_3/file_1.HEIC',
		'test_results/test_directory/dir_3/file_5.HEIC',
		'test_results/test_directory/dir_3/file_10.HEIC',
		'test_results/test_directory/dir_3/file_12.HEIC',
		'test_results/test_directory/dir_3/file_25.HEIC',
		'test_results/test_directory/file_1.HEIC',
		'test_results/test_directory/file_12.HEIC',
		'test_results/test_directory/file_24.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_7.JPG',
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_22.JPG',
		'test_results/test_directory/dir_1/dir_4/dir_8/file_17.jpg',
		'test_results/test_directory/dir_1/dir_5/dir_10/file_7.JPG',
		'test_results/test_directory/dir_1/file_3.JPG',
		'test_results/test_directory/dir_1/file_15.JPG',
		'test_results/test_directory/dir_2/dir_6/file_3.JPG',
		'test_results/test_directory/dir_2/file_3.JPG',
		'test_results/test_directory/dir_3/file_15.JPG',
		'test_results/test_directory/dir_3/file_19.JPG',
		'test_results/test_directory/dir_3/file_22.JPG',
		'test_results/test_directory/file_15.JPG',
		'test_results/test_directory/dir_1/dir_4/file_4.png',
		'test_results/test_directory/dir_1/dir_4/file_13.PNG',
		'test_results/test_directory/dir_1/dir_4/file_18.PNG',
		'test_results/test_directory/dir_1/dir_5/file_2.png',
		'test_results/test_directory/dir_1/file_2.png',
		'test_results/test_directory/dir_1/file_4.png',
		'test_results/test_directory/dir_2/dir_6/file_9.png',
		'test_results/test_directory/dir_2/dir_7/file_20.png',
		'test_results/test_directory/dir_2/file_2.png',
		'test_results/test_directory/dir_3/file_4.png',
		'test_results/test_directory/file_20.png',
		'test_results/test_directory/dir_1/file_11.jpeg',
		'test_results/test_directory/dir_2/dir_7/file_11.jpeg',
		'test_results/test_directory/dir_2/file_23.jpeg',
	}

	assert answer == correct_answer


def test_find_all_files_2():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	answer = set(find_all_files(name_source_path, copy_file_extensions='.jpg'))

	shutil.rmtree('test_results')

	correct_answer = {
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_7.JPG',
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_22.JPG',
		'test_results/test_directory/dir_1/dir_4/dir_8/file_17.jpg',
		'test_results/test_directory/dir_1/dir_5/dir_10/file_7.JPG',
		'test_results/test_directory/dir_1/file_3.JPG',
		'test_results/test_directory/dir_1/file_15.JPG',
		'test_results/test_directory/dir_2/dir_6/file_3.JPG',
		'test_results/test_directory/dir_2/file_3.JPG',
		'test_results/test_directory/dir_3/file_15.JPG',
		'test_results/test_directory/dir_3/file_19.JPG',
		'test_results/test_directory/dir_3/file_22.JPG',
		'test_results/test_directory/file_15.JPG',
	}

	assert answer == correct_answer


def test_find_all_files_3():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	answer = set(find_all_files(name_source_path, copy_file_extensions=('.heic', '.png')))

	shutil.rmtree('test_results')

	correct_answer = {
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_6.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_14.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_16.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/file_5.HEIC',
		'test_results/test_directory/dir_1/dir_4/file_1.HEIC',
		'test_results/test_directory/dir_1/dir_5/dir_10/file_24.HEIC',
		'test_results/test_directory/dir_1/dir_5/file_12.HEIC',
		'test_results/test_directory/dir_1/dir_5/file_26.HEIC',
		'test_results/test_directory/dir_1/file_1.HEIC',
		'test_results/test_directory/dir_2/dir_6/file_21.HEIC',
		'test_results/test_directory/dir_2/dir_6/file_24.HEIC',
		'test_results/test_directory/dir_2/file_6.HEIC',
		'test_results/test_directory/dir_2/file_8.HEIC',
		'test_results/test_directory/dir_2/file_16.HEIC',
		'test_results/test_directory/dir_3/file_1.HEIC',
		'test_results/test_directory/dir_3/file_5.HEIC',
		'test_results/test_directory/dir_3/file_10.HEIC',
		'test_results/test_directory/dir_3/file_12.HEIC',
		'test_results/test_directory/dir_3/file_25.HEIC',
		'test_results/test_directory/file_1.HEIC',
		'test_results/test_directory/file_12.HEIC',
		'test_results/test_directory/file_24.HEIC',
		'test_results/test_directory/dir_1/dir_4/file_4.png',
		'test_results/test_directory/dir_1/dir_4/file_13.PNG',
		'test_results/test_directory/dir_1/dir_4/file_18.PNG',
		'test_results/test_directory/dir_1/dir_5/file_2.png',
		'test_results/test_directory/dir_1/file_2.png',
		'test_results/test_directory/dir_1/file_4.png',
		'test_results/test_directory/dir_2/dir_6/file_9.png',
		'test_results/test_directory/dir_2/dir_7/file_20.png',
		'test_results/test_directory/dir_2/file_2.png',
		'test_results/test_directory/dir_3/file_4.png',
		'test_results/test_directory/file_20.png',
	}

	assert answer == correct_answer


def test_get_file_date_1():
	created_date = get_file_date('reference_test_directory/dir_1/dir_4/file_18.PNG')
	correct_answer = ('2020', '10', '08', '23', '29', '49')

	assert created_date == correct_answer


def test_get_file_date_2():
	created_date = get_file_date('reference_test_directory/dir_2/dir_6/file_24.HEIC', which_date='created')
	correct_answer = ('2020', '08', '06', '11', '48', '15')

	assert created_date == correct_answer


def test_get_file_date_3():
	created_date = get_file_date('reference_test_directory/dir_1/dir_5/file_12.HEIC', which_date='modified')
	correct_answer = ('2023', '03', '12', '15', '20', '24')

	assert created_date == correct_answer


def test_move_files_1():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	move_files(source_path=name_source_path, resulting_path='test_results/resulting_images',
			   copy_file_extensions=('.jpg', '.jpeg', '.png'), new_name=True, sorting_date='created',
			   mute=False, copy=False)

	answer = set(find_all_files('test_results', copy_file_extensions=''))

	shutil.rmtree('test_results')

	correct_answer = {
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_6.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_14.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_16.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/file_5.HEIC',
		'test_results/test_directory/dir_1/dir_4/file_1.HEIC',
		'test_results/test_directory/dir_1/dir_5/dir_10/file_24.HEIC',
		'test_results/test_directory/dir_1/dir_5/file_12.HEIC',
		'test_results/test_directory/dir_1/dir_5/file_26.HEIC',
		'test_results/test_directory/dir_1/file_1.HEIC',
		'test_results/test_directory/dir_2/dir_6/file_21.HEIC',
		'test_results/test_directory/dir_2/dir_6/file_24.HEIC',
		'test_results/test_directory/dir_2/file_6.HEIC',
		'test_results/test_directory/dir_2/file_8.HEIC',
		'test_results/test_directory/dir_2/file_16.HEIC',
		'test_results/test_directory/dir_3/file_1.HEIC',
		'test_results/test_directory/dir_3/file_5.HEIC',
		'test_results/test_directory/dir_3/file_10.HEIC',
		'test_results/test_directory/dir_3/file_12.HEIC',
		'test_results/test_directory/dir_3/file_25.HEIC',
		'test_results/test_directory/file_1.HEIC',
		'test_results/test_directory/file_12.HEIC',
		'test_results/test_directory/file_24.HEIC',
		'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45_1.jpg',
		'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08_1.jpg',
		'test_results/resulting_images/2016/2016_10/2016_10_26_03_11_28.jpg',
		'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45.jpg',
		'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_1.jpg',
		'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_2.jpg',
		'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_2.jpg',
		'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36.jpg',
		'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_1.jpg',
		'test_results/resulting_images/2020/2020_03/2020_03_23_21_35_28.jpg',
		'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08.jpg',
		'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11.jpg',
		'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22_1.png',
		'test_results/resulting_images/2019/2019_07/2019_07_23_22_16_39.png',
		'test_results/resulting_images/2020/2020_10/2020_10_08_23_29_49.png',
		'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44_1.png',
		'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44_2.png',
		'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22_2.png',
		'test_results/resulting_images/2014/2014_08/2014_08_10_15_46_40.png',
		'test_results/resulting_images/2022/2022_05/2022_05_06_14_42_07_1.png',
		'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44.png',
		'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22.png',
		'test_results/resulting_images/2022/2022_05/2022_05_06_14_42_07.png',
		'test_results/resulting_images/2021/2021_08/2021_08_20_12_50_05_1.jpeg',
		'test_results/resulting_images/2021/2021_08/2021_08_20_12_50_05.jpeg',
		'test_results/resulting_images/2022/2022_05/2022_05_04_15_55_13.jpeg',
	}

	assert answer == correct_answer


def test_move_files_2():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	move_files(source_path=name_source_path, resulting_path='test_results/resulting_images',
			   copy_file_extensions=('.png', '.heic'), new_name=True, sorting_date='created',
			   mute=False, copy=False)

	answer = set(find_all_files('test_results', copy_file_extensions=('.png', '.heic', '.jpeg')))

	shutil.rmtree('test_results')

	correct_answer = {
		'test_results/resulting_images/2022/2022_11/2022_11_07_20_02_43_1.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_59.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_11_10_08_29_1.heic',
		'test_results/resulting_images/2022/2022_08/2022_08_18_12_47_32_1.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_1.heic',
		'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15_1.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24_1.heic',
		'test_results/resulting_images/2021/2021_08/2021_08_23_14_52_57.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_2.heic',
		'test_results/resulting_images/2020/2020_08/2020_08_06_10_21_39.heic',
		'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15_2.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_07_20_02_43.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_11_10_02_47.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_11_10_08_29.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_3.heic',
		'test_results/resulting_images/2022/2022_08/2022_08_18_12_47_32.heic',
		'test_results/resulting_images/2022/2022_10/2022_10_17_06_55_16.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24_2.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_18_16_09_32.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24.heic',
		'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15.heic',
		'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22_1.png',
		'test_results/resulting_images/2019/2019_07/2019_07_23_22_16_39.png',
		'test_results/resulting_images/2020/2020_10/2020_10_08_23_29_49.png',
		'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44_1.png',
		'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44_2.png',
		'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22_2.png',
		'test_results/resulting_images/2014/2014_08/2014_08_10_15_46_40.png',
		'test_results/resulting_images/2022/2022_05/2022_05_06_14_42_07_1.png',
		'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44.png',
		'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22.png',
		'test_results/resulting_images/2022/2022_05/2022_05_06_14_42_07.png',
		'test_results/test_directory/dir_1/file_11.jpeg',
		'test_results/test_directory/dir_2/dir_7/file_11.jpeg',
		'test_results/test_directory/dir_2/file_23.jpeg',
	}

	assert answer == correct_answer


def test_move_files_3():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	move_files(source_path=name_source_path, resulting_path='test_results/resulting_images',
			   copy_file_extensions=('.jpg', '.jpeg'), new_name=True, sorting_date='modified',
			   mute=False, copy=False)

	answer = set(find_all_files('test_results', copy_file_extensions=('.jpg', '.heic', '.jpeg')))

	shutil.rmtree('test_results')

	correct_answer = {
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_6.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_14.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_16.HEIC',
		'test_results/test_directory/dir_1/dir_4/dir_8/file_5.HEIC',
		'test_results/test_directory/dir_1/dir_4/file_1.HEIC',
		'test_results/test_directory/dir_1/dir_5/dir_10/file_24.HEIC',
		'test_results/test_directory/dir_1/dir_5/file_12.HEIC',
		'test_results/test_directory/dir_1/dir_5/file_26.HEIC',
		'test_results/test_directory/dir_1/file_1.HEIC',
		'test_results/test_directory/dir_2/dir_6/file_21.HEIC',
		'test_results/test_directory/dir_2/dir_6/file_24.HEIC',
		'test_results/test_directory/dir_2/file_6.HEIC',
		'test_results/test_directory/dir_2/file_8.HEIC',
		'test_results/test_directory/dir_2/file_16.HEIC',
		'test_results/test_directory/dir_3/file_1.HEIC',
		'test_results/test_directory/dir_3/file_5.HEIC',
		'test_results/test_directory/dir_3/file_10.HEIC',
		'test_results/test_directory/dir_3/file_12.HEIC',
		'test_results/test_directory/dir_3/file_25.HEIC',
		'test_results/test_directory/file_1.HEIC',
		'test_results/test_directory/file_12.HEIC',
		'test_results/test_directory/file_24.HEIC',
		'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45_1.jpg',
		'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08_1.jpg',
		'test_results/resulting_images/2016/2016_10/2016_10_26_03_11_28.jpg',
		'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45.jpg',
		'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_1.jpg',
		'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_2.jpg',
		'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_2.jpg',
		'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36.jpg',
		'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_1.jpg',
		'test_results/resulting_images/2020/2020_03/2020_03_23_21_35_28.jpg',
		'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08.jpg',
		'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11.jpg',
		'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_27_1.jpeg',
		'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_27.jpeg',
		'test_results/resulting_images/2023/2023_07/2023_07_04_15_53_39.jpeg',
	}

	assert answer == correct_answer


def test_move_files_4():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	move_files(source_path=name_source_path, resulting_path='test_results/resulting_images',
			   copy_file_extensions=('.jpg', '.jpeg', '.heic'), new_name=True, sorting_date='modified',
			   mute=False, copy=False)

	answer = set(find_all_files('test_results', copy_file_extensions=''))

	shutil.rmtree('test_results')

	correct_answer = {
		'test_results/resulting_images/2022/2022_11/2022_11_07_20_02_43_1.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_59.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_11_10_08_29_1.heic',
		'test_results/resulting_images/2022/2022_08/2022_08_18_12_47_32_1.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_1.heic',
		'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15_1.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24_1.heic',
		'test_results/resulting_images/2021/2021_08/2021_08_23_14_52_57.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_2.heic',
		'test_results/resulting_images/2020/2020_08/2020_08_06_10_21_39.heic',
		'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15_2.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_07_20_02_43.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_11_10_02_47.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_11_10_08_29.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_3.heic',
		'test_results/resulting_images/2022/2022_08/2022_08_18_12_47_32.heic',
		'test_results/resulting_images/2022/2022_10/2022_10_17_06_55_16.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24_2.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_18_16_09_32.heic',
		'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56.heic',
		'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24.heic',
		'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15.heic',
		'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45_1.jpg',
		'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08_1.jpg',
		'test_results/resulting_images/2016/2016_10/2016_10_26_03_11_28.jpg',
		'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45.jpg',
		'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_1.jpg',
		'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_2.jpg',
		'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_2.jpg',
		'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36.jpg',
		'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_1.jpg',
		'test_results/resulting_images/2020/2020_03/2020_03_23_21_35_28.jpg',
		'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08.jpg',
		'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11.jpg',
		'test_results/test_directory/dir_1/dir_4/file_4.png',
		'test_results/test_directory/dir_1/dir_4/file_13.PNG',
		'test_results/test_directory/dir_1/dir_4/file_18.PNG',
		'test_results/test_directory/dir_1/dir_5/file_2.png',
		'test_results/test_directory/dir_1/file_2.png',
		'test_results/test_directory/dir_1/file_4.png',
		'test_results/test_directory/dir_2/dir_6/file_9.png',
		'test_results/test_directory/dir_2/dir_7/file_20.png',
		'test_results/test_directory/dir_2/file_2.png',
		'test_results/test_directory/dir_3/file_4.png',
		'test_results/test_directory/file_20.png',
		'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_27_1.jpeg',
		'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_27.jpeg',
		'test_results/resulting_images/2023/2023_07/2023_07_04_15_53_39.jpeg',
	}

	assert answer == correct_answer


def test_special_cases_1():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.heic', '.jpg', '.png', '.jpeg', '-m', 'false', '-r',
					'true', '-t' 'created', '-c', 'true', ])

	all_files = set(find_all_files('test_results', copy_file_extensions=''))
	shutil.rmtree('test_results')

	should_contain = {
		'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22.png',
		'test_results/resulting_images/2021/2021_08/2021_08_20_12_50_05.jpeg',
		'test_results/resulting_images/2022/2022_05/2022_05_06_14_42_07.png',
		'test_results/resulting_images/2022/2022_05/2022_05_04_15_55_13.jpeg',
	}

	assert should_contain.issubset(all_files)


def test_special_cases_2():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.heic', '.jpg', '.png', '.jpeg', '-m', 'false', '-r',
					'true', '-t' 'modified', '-c', 'true', ])

	all_files = set(find_all_files('test_results', copy_file_extensions=''))
	shutil.rmtree('test_results')

	should_contain = {
		'test_results/resulting_images/2023/2023_07/2023_07_04_15_55_17.png',
		'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_27.jpeg',
		'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_01.png',
		'test_results/resulting_images/2023/2023_07/2023_07_04_15_53_39.jpeg',
	}

	assert should_contain.issubset(all_files)


def test_special_cases_3():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.heic', '.jpg', '.png', '.jpeg', '-m', 'false', '-r',
					'false', '-t' 'created', '-c', 'true', ])

	all_files = set(find_all_files('test_results', copy_file_extensions=''))
	shutil.rmtree('test_results')

	should_contain = {
		'test_results/resulting_images/2021/2021_05/file_4.png',
		'test_results/resulting_images/2021/2021_08/file_11.jpeg',
		'test_results/resulting_images/2022/2022_05/file_20.png',
		'test_results/resulting_images/2022/2022_05/file_23.jpeg',
	}

	assert should_contain.issubset(all_files)


def test_special_cases_4():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.heic', '.jpg', '.png', '.jpeg', '-m', 'false', '-r',
					'false', '-t' 'modified', '-c', 'true', ])

	all_files = set(find_all_files('test_results', copy_file_extensions=''))
	shutil.rmtree('test_results')

	should_contain = {
		'test_results/resulting_images/2023/2023_07/file_4.png',
		'test_results/resulting_images/2023/2023_07/file_11.jpeg',
		'test_results/resulting_images/2023/2023_07/file_20.png',
		'test_results/resulting_images/2023/2023_07/file_23.jpeg',
	}

	assert should_contain.issubset(all_files)


def test_overall_program_1():

	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	# test number 1
	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.jpg', '.png', '.jpeg', '-m', 'false', '-r', 'true',
					'-t' 'created', '-c', 'true', ])
	extensions_to_search = '.jpg', '.png', '.jpeg',
	answer = set(find_all_files('test_results', copy_file_extensions=extensions_to_search))
	shutil.rmtree('test_results')
	correct_answer = {'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45_1.jpg',
					  'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08_1.jpg',
					  'test_results/resulting_images/2016/2016_10/2016_10_26_03_11_28.jpg',
					  'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_1.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_2.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_2.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_1.jpg',
					  'test_results/resulting_images/2020/2020_03/2020_03_23_21_35_28.jpg',
					  'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11.jpg',
					  'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22_1.png',
					  'test_results/resulting_images/2019/2019_07/2019_07_23_22_16_39.png',
					  'test_results/resulting_images/2020/2020_10/2020_10_08_23_29_49.png',
					  'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44_1.png',
					  'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44_2.png',
					  'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22_2.png',
					  'test_results/resulting_images/2014/2014_08/2014_08_10_15_46_40.png',
					  'test_results/resulting_images/2022/2022_05/2022_05_06_14_42_07_1.png',
					  'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44.png',
					  'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22.png',
					  'test_results/resulting_images/2022/2022_05/2022_05_06_14_42_07.png',
					  'test_results/resulting_images/2021/2021_08/2021_08_20_12_50_05_1.jpeg',
					  'test_results/resulting_images/2021/2021_08/2021_08_20_12_50_05.jpeg',
					  'test_results/resulting_images/2022/2022_05/2022_05_04_15_55_13.jpeg',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_7.JPG',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_22.JPG',
					  'test_results/test_directory/dir_1/dir_4/dir_8/file_17.jpg',
					  'test_results/test_directory/dir_1/dir_5/dir_10/file_7.JPG',
					  'test_results/test_directory/dir_1/file_3.JPG', 'test_results/test_directory/dir_1/file_15.JPG',
					  'test_results/test_directory/dir_2/dir_6/file_3.JPG',
					  'test_results/test_directory/dir_2/file_3.JPG', 'test_results/test_directory/dir_3/file_15.JPG',
					  'test_results/test_directory/dir_3/file_19.JPG', 'test_results/test_directory/dir_3/file_22.JPG',
					  'test_results/test_directory/file_15.JPG', 'test_results/test_directory/dir_1/dir_4/file_4.png',
					  'test_results/test_directory/dir_1/dir_4/file_13.PNG',
					  'test_results/test_directory/dir_1/dir_4/file_18.PNG',
					  'test_results/test_directory/dir_1/dir_5/file_2.png',
					  'test_results/test_directory/dir_1/file_2.png', 'test_results/test_directory/dir_1/file_4.png',
					  'test_results/test_directory/dir_2/dir_6/file_9.png',
					  'test_results/test_directory/dir_2/dir_7/file_20.png',
					  'test_results/test_directory/dir_2/file_2.png', 'test_results/test_directory/dir_3/file_4.png',
					  'test_results/test_directory/file_20.png', 'test_results/test_directory/dir_1/file_11.jpeg',
					  'test_results/test_directory/dir_2/dir_7/file_11.jpeg',
					  'test_results/test_directory/dir_2/file_23.jpeg', }

	assert answer == correct_answer


def test_overall_program_2():
	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	# test number 2
	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.heic', '.png', '.jpeg', '-m', 'false', '-r', 'false',
					'-t' 'created', '-c', 'true', ])
	extensions_to_search = '.heic', '.png', '.jpeg',
	answer = set(find_all_files('test_results', copy_file_extensions=extensions_to_search))
	shutil.rmtree('test_results')
	correct_answer = {'test_results/resulting_images/2022/2022_11/file_6_1.heic',
					  'test_results/resulting_images/2022/2022_11/file_14.heic',
					  'test_results/resulting_images/2023/2023_03/file_16_1.heic',
					  'test_results/resulting_images/2022/2022_08/file_5_1.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_1.heic',
					  'test_results/resulting_images/2020/2020_08/file_24_1.heic',
					  'test_results/resulting_images/2023/2023_03/file_12_1.heic',
					  'test_results/resulting_images/2021/2021_08/file_26.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_2.heic',
					  'test_results/resulting_images/2020/2020_08/file_21.heic',
					  'test_results/resulting_images/2020/2020_08/file_24_2.heic',
					  'test_results/resulting_images/2022/2022_11/file_6.heic',
					  'test_results/resulting_images/2023/2023_03/file_8.heic',
					  'test_results/resulting_images/2023/2023_03/file_16.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_3.heic',
					  'test_results/resulting_images/2022/2022_08/file_5.heic',
					  'test_results/resulting_images/2022/2022_10/file_10.heic',
					  'test_results/resulting_images/2023/2023_03/file_12_2.heic',
					  'test_results/resulting_images/2022/2022_11/file_25.heic',
					  'test_results/resulting_images/2022/2022_11/file_1.heic',
					  'test_results/resulting_images/2023/2023_03/file_12.heic',
					  'test_results/resulting_images/2020/2020_08/file_24.heic',
					  'test_results/resulting_images/2021/2021_05/file_4_1.png',
					  'test_results/resulting_images/2019/2019_07/file_13.png',
					  'test_results/resulting_images/2020/2020_10/file_18.png',
					  'test_results/resulting_images/2014/2014_12/file_2_1.png',
					  'test_results/resulting_images/2014/2014_12/file_2_2.png',
					  'test_results/resulting_images/2021/2021_05/file_4_2.png',
					  'test_results/resulting_images/2014/2014_08/file_9.png',
					  'test_results/resulting_images/2022/2022_05/file_20_1.png',
					  'test_results/resulting_images/2014/2014_12/file_2.png',
					  'test_results/resulting_images/2021/2021_05/file_4.png',
					  'test_results/resulting_images/2022/2022_05/file_20.png',
					  'test_results/resulting_images/2021/2021_08/file_11_1.jpeg',
					  'test_results/resulting_images/2021/2021_08/file_11.jpeg',
					  'test_results/resulting_images/2022/2022_05/file_23.jpeg',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_6.HEIC',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_14.HEIC',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_16.HEIC',
					  'test_results/test_directory/dir_1/dir_4/dir_8/file_5.HEIC',
					  'test_results/test_directory/dir_1/dir_4/file_1.HEIC',
					  'test_results/test_directory/dir_1/dir_5/dir_10/file_24.HEIC',
					  'test_results/test_directory/dir_1/dir_5/file_12.HEIC',
					  'test_results/test_directory/dir_1/dir_5/file_26.HEIC',
					  'test_results/test_directory/dir_1/file_1.HEIC',
					  'test_results/test_directory/dir_2/dir_6/file_21.HEIC',
					  'test_results/test_directory/dir_2/dir_6/file_24.HEIC',
					  'test_results/test_directory/dir_2/file_6.HEIC', 'test_results/test_directory/dir_2/file_8.HEIC',
					  'test_results/test_directory/dir_2/file_16.HEIC', 'test_results/test_directory/dir_3/file_1.HEIC',
					  'test_results/test_directory/dir_3/file_5.HEIC', 'test_results/test_directory/dir_3/file_10.HEIC',
					  'test_results/test_directory/dir_3/file_12.HEIC',
					  'test_results/test_directory/dir_3/file_25.HEIC', 'test_results/test_directory/file_1.HEIC',
					  'test_results/test_directory/file_12.HEIC', 'test_results/test_directory/file_24.HEIC',
					  'test_results/test_directory/dir_1/dir_4/file_4.png',
					  'test_results/test_directory/dir_1/dir_4/file_13.PNG',
					  'test_results/test_directory/dir_1/dir_4/file_18.PNG',
					  'test_results/test_directory/dir_1/dir_5/file_2.png',
					  'test_results/test_directory/dir_1/file_2.png', 'test_results/test_directory/dir_1/file_4.png',
					  'test_results/test_directory/dir_2/dir_6/file_9.png',
					  'test_results/test_directory/dir_2/dir_7/file_20.png',
					  'test_results/test_directory/dir_2/file_2.png', 'test_results/test_directory/dir_3/file_4.png',
					  'test_results/test_directory/file_20.png', 'test_results/test_directory/dir_1/file_11.jpeg',
					  'test_results/test_directory/dir_2/dir_7/file_11.jpeg',
					  'test_results/test_directory/dir_2/file_23.jpeg', }

	assert answer == correct_answer


def test_overall_program_3():
	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	# test number 3
	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.heic', '.jpg', '.jpeg', '-m', 'false', '-r', 'true',
					'-t' 'modified', '-c', 'true', ])
	extensions_to_search = '.heic', '.jpg', '.jpeg',
	answer = set(find_all_files('test_results', copy_file_extensions=extensions_to_search))
	shutil.rmtree('test_results')
	correct_answer = {'test_results/resulting_images/2022/2022_11/2022_11_07_20_02_43_1.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_59.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_11_10_08_29_1.heic',
					  'test_results/resulting_images/2022/2022_08/2022_08_18_12_47_32_1.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_1.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15_1.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24_1.heic',
					  'test_results/resulting_images/2021/2021_08/2021_08_23_14_52_57.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_2.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_10_21_39.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15_2.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_07_20_02_43.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_11_10_02_47.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_11_10_08_29.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_3.heic',
					  'test_results/resulting_images/2022/2022_08/2022_08_18_12_47_32.heic',
					  'test_results/resulting_images/2022/2022_10/2022_10_17_06_55_16.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24_2.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_18_16_09_32.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15.heic',
					  'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45_1.jpg',
					  'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08_1.jpg',
					  'test_results/resulting_images/2016/2016_10/2016_10_26_03_11_28.jpg',
					  'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_1.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_2.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_2.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_1.jpg',
					  'test_results/resulting_images/2020/2020_03/2020_03_23_21_35_28.jpg',
					  'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11.jpg',
					  'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_27_1.jpeg',
					  'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_27.jpeg',
					  'test_results/resulting_images/2023/2023_07/2023_07_04_15_53_39.jpeg',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_6.HEIC',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_14.HEIC',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_16.HEIC',
					  'test_results/test_directory/dir_1/dir_4/dir_8/file_5.HEIC',
					  'test_results/test_directory/dir_1/dir_4/file_1.HEIC',
					  'test_results/test_directory/dir_1/dir_5/dir_10/file_24.HEIC',
					  'test_results/test_directory/dir_1/dir_5/file_12.HEIC',
					  'test_results/test_directory/dir_1/dir_5/file_26.HEIC',
					  'test_results/test_directory/dir_1/file_1.HEIC',
					  'test_results/test_directory/dir_2/dir_6/file_21.HEIC',
					  'test_results/test_directory/dir_2/dir_6/file_24.HEIC',
					  'test_results/test_directory/dir_2/file_6.HEIC', 'test_results/test_directory/dir_2/file_8.HEIC',
					  'test_results/test_directory/dir_2/file_16.HEIC', 'test_results/test_directory/dir_3/file_1.HEIC',
					  'test_results/test_directory/dir_3/file_5.HEIC', 'test_results/test_directory/dir_3/file_10.HEIC',
					  'test_results/test_directory/dir_3/file_12.HEIC',
					  'test_results/test_directory/dir_3/file_25.HEIC', 'test_results/test_directory/file_1.HEIC',
					  'test_results/test_directory/file_12.HEIC', 'test_results/test_directory/file_24.HEIC',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_7.JPG',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_22.JPG',
					  'test_results/test_directory/dir_1/dir_4/dir_8/file_17.jpg',
					  'test_results/test_directory/dir_1/dir_5/dir_10/file_7.JPG',
					  'test_results/test_directory/dir_1/file_3.JPG', 'test_results/test_directory/dir_1/file_15.JPG',
					  'test_results/test_directory/dir_2/dir_6/file_3.JPG',
					  'test_results/test_directory/dir_2/file_3.JPG', 'test_results/test_directory/dir_3/file_15.JPG',
					  'test_results/test_directory/dir_3/file_19.JPG', 'test_results/test_directory/dir_3/file_22.JPG',
					  'test_results/test_directory/file_15.JPG', 'test_results/test_directory/dir_1/file_11.jpeg',
					  'test_results/test_directory/dir_2/dir_7/file_11.jpeg',
					  'test_results/test_directory/dir_2/file_23.jpeg', }

	assert answer == correct_answer


def test_overall_program_4():
	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	# test number 4
	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.heic', '.png', '-m', 'false', '-r', 'false',
					'-t' 'modified', '-c', 'true', ])
	extensions_to_search = '.heic', '.jpg',
	answer = set(find_all_files('test_results', copy_file_extensions=extensions_to_search))
	shutil.rmtree('test_results')
	correct_answer = {'test_results/resulting_images/2022/2022_11/file_6_1.heic',
					  'test_results/resulting_images/2022/2022_11/file_14.heic',
					  'test_results/resulting_images/2023/2023_03/file_16_1.heic',
					  'test_results/resulting_images/2022/2022_08/file_5_1.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_1.heic',
					  'test_results/resulting_images/2020/2020_08/file_24_1.heic',
					  'test_results/resulting_images/2023/2023_03/file_12_1.heic',
					  'test_results/resulting_images/2021/2021_08/file_26.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_2.heic',
					  'test_results/resulting_images/2020/2020_08/file_21.heic',
					  'test_results/resulting_images/2020/2020_08/file_24_2.heic',
					  'test_results/resulting_images/2022/2022_11/file_6.heic',
					  'test_results/resulting_images/2023/2023_03/file_8.heic',
					  'test_results/resulting_images/2023/2023_03/file_16.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_3.heic',
					  'test_results/resulting_images/2022/2022_08/file_5.heic',
					  'test_results/resulting_images/2022/2022_10/file_10.heic',
					  'test_results/resulting_images/2023/2023_03/file_12_2.heic',
					  'test_results/resulting_images/2022/2022_11/file_25.heic',
					  'test_results/resulting_images/2022/2022_11/file_1.heic',
					  'test_results/resulting_images/2023/2023_03/file_12.heic',
					  'test_results/resulting_images/2020/2020_08/file_24.heic',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_7.JPG',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_22.JPG',
					  'test_results/test_directory/dir_1/dir_4/dir_8/file_17.jpg',
					  'test_results/test_directory/dir_1/dir_5/dir_10/file_7.JPG',
					  'test_results/test_directory/dir_1/file_3.JPG', 'test_results/test_directory/dir_1/file_15.JPG',
					  'test_results/test_directory/dir_2/dir_6/file_3.JPG',
					  'test_results/test_directory/dir_2/file_3.JPG', 'test_results/test_directory/dir_3/file_15.JPG',
					  'test_results/test_directory/dir_3/file_19.JPG', 'test_results/test_directory/dir_3/file_22.JPG',
					  'test_results/test_directory/file_15.JPG',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_6.HEIC',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_14.HEIC',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_16.HEIC',
					  'test_results/test_directory/dir_1/dir_4/dir_8/file_5.HEIC',
					  'test_results/test_directory/dir_1/dir_4/file_1.HEIC',
					  'test_results/test_directory/dir_1/dir_5/dir_10/file_24.HEIC',
					  'test_results/test_directory/dir_1/dir_5/file_12.HEIC',
					  'test_results/test_directory/dir_1/dir_5/file_26.HEIC',
					  'test_results/test_directory/dir_1/file_1.HEIC',
					  'test_results/test_directory/dir_2/dir_6/file_21.HEIC',
					  'test_results/test_directory/dir_2/dir_6/file_24.HEIC',
					  'test_results/test_directory/dir_2/file_6.HEIC', 'test_results/test_directory/dir_2/file_8.HEIC',
					  'test_results/test_directory/dir_2/file_16.HEIC', 'test_results/test_directory/dir_3/file_1.HEIC',
					  'test_results/test_directory/dir_3/file_5.HEIC', 'test_results/test_directory/dir_3/file_10.HEIC',
					  'test_results/test_directory/dir_3/file_12.HEIC',
					  'test_results/test_directory/dir_3/file_25.HEIC', 'test_results/test_directory/file_1.HEIC',
					  'test_results/test_directory/file_12.HEIC', 'test_results/test_directory/file_24.HEIC', }

	assert answer == correct_answer


def test_overall_program_5():
	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	# test number 5
	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.heic', '.jpg', '.jpeg', '-m', 'false', '-r', 'true',
					'-t' 'created', '-c', 'false', ])
	extensions_to_search = '.heic', '.jpg', '.jpeg',
	answer = set(find_all_files('test_results', copy_file_extensions=extensions_to_search))
	shutil.rmtree('test_results')
	correct_answer = {'test_results/resulting_images/2022/2022_11/2022_11_07_20_02_43_1.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_59.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_11_10_08_29_1.heic',
					  'test_results/resulting_images/2022/2022_08/2022_08_18_12_47_32_1.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_1.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15_1.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24_1.heic',
					  'test_results/resulting_images/2021/2021_08/2021_08_23_14_52_57.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_2.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_10_21_39.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15_2.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_07_20_02_43.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_11_10_02_47.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_11_10_08_29.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_3.heic',
					  'test_results/resulting_images/2022/2022_08/2022_08_18_12_47_32.heic',
					  'test_results/resulting_images/2022/2022_10/2022_10_17_06_55_16.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24_2.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_18_16_09_32.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15.heic',
					  'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45_1.jpg',
					  'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08_1.jpg',
					  'test_results/resulting_images/2016/2016_10/2016_10_26_03_11_28.jpg',
					  'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_1.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_2.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_2.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_1.jpg',
					  'test_results/resulting_images/2020/2020_03/2020_03_23_21_35_28.jpg',
					  'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11.jpg',
					  'test_results/resulting_images/2021/2021_08/2021_08_20_12_50_05_1.jpeg',
					  'test_results/resulting_images/2021/2021_08/2021_08_20_12_50_05.jpeg',
					  'test_results/resulting_images/2022/2022_05/2022_05_04_15_55_13.jpeg', }

	assert answer == correct_answer


def test_overall_program_6():
	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	# test number 6
	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.heic', '.png', '-m', 'false', '-r', 'false',
					'-t' 'created', '-c', 'false', ])
	extensions_to_search = '.heic', '.png', '.jpeg',
	answer = set(find_all_files('test_results', copy_file_extensions=extensions_to_search))
	shutil.rmtree('test_results')
	correct_answer = {'test_results/resulting_images/2022/2022_11/file_6_1.heic',
					  'test_results/resulting_images/2022/2022_11/file_14.heic',
					  'test_results/resulting_images/2023/2023_03/file_16_1.heic',
					  'test_results/resulting_images/2022/2022_08/file_5_1.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_1.heic',
					  'test_results/resulting_images/2020/2020_08/file_24_1.heic',
					  'test_results/resulting_images/2023/2023_03/file_12_1.heic',
					  'test_results/resulting_images/2021/2021_08/file_26.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_2.heic',
					  'test_results/resulting_images/2020/2020_08/file_21.heic',
					  'test_results/resulting_images/2020/2020_08/file_24_2.heic',
					  'test_results/resulting_images/2022/2022_11/file_6.heic',
					  'test_results/resulting_images/2023/2023_03/file_8.heic',
					  'test_results/resulting_images/2023/2023_03/file_16.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_3.heic',
					  'test_results/resulting_images/2022/2022_08/file_5.heic',
					  'test_results/resulting_images/2022/2022_10/file_10.heic',
					  'test_results/resulting_images/2023/2023_03/file_12_2.heic',
					  'test_results/resulting_images/2022/2022_11/file_25.heic',
					  'test_results/resulting_images/2022/2022_11/file_1.heic',
					  'test_results/resulting_images/2023/2023_03/file_12.heic',
					  'test_results/resulting_images/2020/2020_08/file_24.heic',
					  'test_results/resulting_images/2021/2021_05/file_4_1.png',
					  'test_results/resulting_images/2019/2019_07/file_13.png',
					  'test_results/resulting_images/2020/2020_10/file_18.png',
					  'test_results/resulting_images/2014/2014_12/file_2_1.png',
					  'test_results/resulting_images/2014/2014_12/file_2_2.png',
					  'test_results/resulting_images/2021/2021_05/file_4_2.png',
					  'test_results/resulting_images/2014/2014_08/file_9.png',
					  'test_results/resulting_images/2022/2022_05/file_20_1.png',
					  'test_results/resulting_images/2014/2014_12/file_2.png',
					  'test_results/resulting_images/2021/2021_05/file_4.png',
					  'test_results/resulting_images/2022/2022_05/file_20.png',
					  'test_results/test_directory/dir_1/file_11.jpeg',
					  'test_results/test_directory/dir_2/dir_7/file_11.jpeg',
					  'test_results/test_directory/dir_2/file_23.jpeg', }

	assert answer == correct_answer


def test_overall_program_7():
	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	# test number 7
	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.jpg', '.png', '.jpeg', '-m', 'false', '-r', 'true',
					'-t' 'modified', '-c', 'false', ])
	extensions_to_search = '.jpg', '.png', '.jpeg',
	answer = set(find_all_files('test_results', copy_file_extensions=extensions_to_search))
	shutil.rmtree('test_results')
	correct_answer = {'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45_1.jpg',
					  'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08_1.jpg',
					  'test_results/resulting_images/2016/2016_10/2016_10_26_03_11_28.jpg',
					  'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_1.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_2.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_2.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_1.jpg',
					  'test_results/resulting_images/2020/2020_03/2020_03_23_21_35_28.jpg',
					  'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11.jpg',
					  'test_results/resulting_images/2023/2023_07/2023_07_04_15_55_17_1.png',
					  'test_results/resulting_images/2019/2019_07/2019_07_23_22_16_39.png',
					  'test_results/resulting_images/2020/2020_10/2020_10_08_21_29_49.png',
					  'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44_1.png',
					  'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44_2.png',
					  'test_results/resulting_images/2023/2023_07/2023_07_04_15_55_17_2.png',
					  'test_results/resulting_images/2014/2014_08/2014_08_10_15_46_40.png',
					  'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_01_1.png',
					  'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44.png',
					  'test_results/resulting_images/2023/2023_07/2023_07_04_15_55_17.png',
					  'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_01.png',
					  'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_27_1.jpeg',
					  'test_results/resulting_images/2023/2023_07/2023_07_04_15_54_27.jpeg',
					  'test_results/resulting_images/2023/2023_07/2023_07_04_15_53_39.jpeg', }

	assert answer == correct_answer


def test_overall_program_8():
	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	# test number 8
	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.heic', '.png', '.jpeg', '-m', 'false', '-r', 'false',
					'-t' 'modified', '-c', 'false', ])
	extensions_to_search = '.heic', '.jpg', '.jpeg',
	answer = set(find_all_files('test_results', copy_file_extensions=extensions_to_search))
	shutil.rmtree('test_results')
	correct_answer = {'test_results/resulting_images/2022/2022_11/file_6_1.heic',
					  'test_results/resulting_images/2022/2022_11/file_14.heic',
					  'test_results/resulting_images/2023/2023_03/file_16_1.heic',
					  'test_results/resulting_images/2022/2022_08/file_5_1.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_1.heic',
					  'test_results/resulting_images/2020/2020_08/file_24_1.heic',
					  'test_results/resulting_images/2023/2023_03/file_12_1.heic',
					  'test_results/resulting_images/2021/2021_08/file_26.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_2.heic',
					  'test_results/resulting_images/2020/2020_08/file_21.heic',
					  'test_results/resulting_images/2020/2020_08/file_24_2.heic',
					  'test_results/resulting_images/2022/2022_11/file_6.heic',
					  'test_results/resulting_images/2023/2023_03/file_8.heic',
					  'test_results/resulting_images/2023/2023_03/file_16.heic',
					  'test_results/resulting_images/2022/2022_11/file_1_3.heic',
					  'test_results/resulting_images/2022/2022_08/file_5.heic',
					  'test_results/resulting_images/2022/2022_10/file_10.heic',
					  'test_results/resulting_images/2023/2023_03/file_12_2.heic',
					  'test_results/resulting_images/2022/2022_11/file_25.heic',
					  'test_results/resulting_images/2022/2022_11/file_1.heic',
					  'test_results/resulting_images/2023/2023_03/file_12.heic',
					  'test_results/resulting_images/2020/2020_08/file_24.heic',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_7.JPG',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_22.JPG',
					  'test_results/test_directory/dir_1/dir_4/dir_8/file_17.jpg',
					  'test_results/test_directory/dir_1/dir_5/dir_10/file_7.JPG',
					  'test_results/test_directory/dir_1/file_3.JPG', 'test_results/test_directory/dir_1/file_15.JPG',
					  'test_results/test_directory/dir_2/dir_6/file_3.JPG',
					  'test_results/test_directory/dir_2/file_3.JPG', 'test_results/test_directory/dir_3/file_15.JPG',
					  'test_results/test_directory/dir_3/file_19.JPG', 'test_results/test_directory/dir_3/file_22.JPG',
					  'test_results/test_directory/file_15.JPG',
					  'test_results/resulting_images/2023/2023_07/file_11_1.jpeg',
					  'test_results/resulting_images/2023/2023_07/file_11.jpeg',
					  'test_results/resulting_images/2023/2023_07/file_23.jpeg', }

	assert answer == correct_answer


def test_overall_program_9():
	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	# test number 9
	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.heic', '-m', 'false', '-r', 'true', '-t' 'created', '-c',
					'false', ])
	extensions_to_search = ''
	answer = set(find_all_files('test_results', copy_file_extensions=extensions_to_search))
	shutil.rmtree('test_results')
	correct_answer = {'test_results/resulting_images/2022/2022_11/2022_11_07_20_02_43_1.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_59.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_11_10_08_29_1.heic',
					  'test_results/resulting_images/2022/2022_08/2022_08_18_12_47_32_1.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_1.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15_1.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24_1.heic',
					  'test_results/resulting_images/2021/2021_08/2021_08_23_14_52_57.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_2.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_10_21_39.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15_2.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_07_20_02_43.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_11_10_02_47.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_11_10_08_29.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56_3.heic',
					  'test_results/resulting_images/2022/2022_08/2022_08_18_12_47_32.heic',
					  'test_results/resulting_images/2022/2022_10/2022_10_17_06_55_16.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24_2.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_18_16_09_32.heic',
					  'test_results/resulting_images/2022/2022_11/2022_11_29_09_25_56.heic',
					  'test_results/resulting_images/2023/2023_03/2023_03_12_15_20_24.heic',
					  'test_results/resulting_images/2020/2020_08/2020_08_06_11_48_15.heic',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_7.JPG',
					  'test_results/test_directory/dir_1/dir_4/dir_8/dir_9/file_22.JPG',
					  'test_results/test_directory/dir_1/dir_4/dir_8/file_17.jpg',
					  'test_results/test_directory/dir_1/dir_5/dir_10/file_7.JPG',
					  'test_results/test_directory/dir_1/file_3.JPG', 'test_results/test_directory/dir_1/file_15.JPG',
					  'test_results/test_directory/dir_2/dir_6/file_3.JPG',
					  'test_results/test_directory/dir_2/file_3.JPG', 'test_results/test_directory/dir_3/file_15.JPG',
					  'test_results/test_directory/dir_3/file_19.JPG', 'test_results/test_directory/dir_3/file_22.JPG',
					  'test_results/test_directory/file_15.JPG', 'test_results/test_directory/dir_1/dir_4/file_4.png',
					  'test_results/test_directory/dir_1/dir_4/file_13.PNG',
					  'test_results/test_directory/dir_1/dir_4/file_18.PNG',
					  'test_results/test_directory/dir_1/dir_5/file_2.png',
					  'test_results/test_directory/dir_1/file_2.png', 'test_results/test_directory/dir_1/file_4.png',
					  'test_results/test_directory/dir_2/dir_6/file_9.png',
					  'test_results/test_directory/dir_2/dir_7/file_20.png',
					  'test_results/test_directory/dir_2/file_2.png', 'test_results/test_directory/dir_3/file_4.png',
					  'test_results/test_directory/file_20.png', 'test_results/test_directory/dir_1/file_11.jpeg',
					  'test_results/test_directory/dir_2/dir_7/file_11.jpeg',
					  'test_results/test_directory/dir_2/file_23.jpeg', }

	assert answer == correct_answer


def test_overall_program_10():
	name_source_path = 'test_results/test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	# test number 10
	subprocess.run(['python', 'move_chronologically.py', '-s', 'test_results/test_directory', '-d',
					'test_results/resulting_images', '-e', '.jpg', '.png', '.jpeg', '-m', 'false', '-r', 'true',
					'-t' 'created', '-c', 'false', ])
	extensions_to_search = '.jpg', '.png', '.jpeg',
	answer = set(find_all_files('test_results', copy_file_extensions=extensions_to_search))
	shutil.rmtree('test_results')
	correct_answer = {'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45_1.jpg',
					  'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08_1.jpg',
					  'test_results/resulting_images/2016/2016_10/2016_10_26_03_11_28.jpg',
					  'test_results/resulting_images/2021/2021_03/2021_03_29_07_52_45.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_1.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_2.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36_2.jpg',
					  'test_results/resulting_images/2020/2020_09/2020_09_10_13_54_36.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11_1.jpg',
					  'test_results/resulting_images/2020/2020_03/2020_03_23_21_35_28.jpg',
					  'test_results/resulting_images/2020/2020_10/2020_10_11_21_17_08.jpg',
					  'test_results/resulting_images/2021/2021_04/2021_04_11_15_52_11.jpg',
					  'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22_1.png',
					  'test_results/resulting_images/2019/2019_07/2019_07_23_22_16_39.png',
					  'test_results/resulting_images/2020/2020_10/2020_10_08_23_29_49.png',
					  'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44_1.png',
					  'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44_2.png',
					  'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22_2.png',
					  'test_results/resulting_images/2014/2014_08/2014_08_10_15_46_40.png',
					  'test_results/resulting_images/2022/2022_05/2022_05_06_14_42_07_1.png',
					  'test_results/resulting_images/2014/2014_12/2014_12_26_15_16_44.png',
					  'test_results/resulting_images/2021/2021_05/2021_05_30_14_42_22.png',
					  'test_results/resulting_images/2022/2022_05/2022_05_06_14_42_07.png',
					  'test_results/resulting_images/2021/2021_08/2021_08_20_12_50_05_1.jpeg',
					  'test_results/resulting_images/2021/2021_08/2021_08_20_12_50_05.jpeg',
					  'test_results/resulting_images/2022/2022_05/2022_05_04_15_55_13.jpeg', }

	assert answer == correct_answer









