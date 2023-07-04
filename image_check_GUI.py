import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from os import walk, rename, remove
import os.path
import datetime
import shutil

global image_index, current_image_path, num_images, movement_records, directory_dictionary, file_log

name_source_path = 'images_GUI'
root_sorted_path = 'sorted_images'
name_saved_path = root_sorted_path + '/saved_images'
name_removed_path = root_sorted_path + '/removed_images'


def create_directory(directory_name, source_path=name_source_path):
	complete_path = source_path + '/' + directory_name
	if not os.path.exists(complete_path):
		os.makedirs(complete_path)

	return complete_path


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


def move_image(dictionary_key):
	file_name = os.path.basename(current_image_path)
	original_file_name, file_extension = os.path.splitext(file_name)
	directory_path = directory_dictionary[dictionary_key]
	new_name = directory_path + '/' + file_name

	# This is necessary, in case the file already exists
	copy_counter = 0
	moved_image = False
	while not moved_image:
		if not os.path.exists(new_name):
			rename(current_image_path, new_name)
			movement_records.append([current_image_path, new_name])
			print(movement_records)
			moved_image = True
		else:
			copy_counter += 1
			new_name = directory_path + '/' + original_file_name + '_' + str(copy_counter) + file_extension


def undo(event):
	global image_index, current_image_path

	last_movement = movement_records.pop()
	old_path = last_movement[1]
	new_path = last_movement[0]
	now = datetime.datetime.now()
	file_log.write('\tUNDO\t\t\t' + str(now)[:19] + '\t' + old_path + ' -> ' + new_path + '\n')
	rename(old_path, new_path)
	image_index -= 1
	current_image_path = all_images_path[image_index]
	update_image()


def next_image(event):

	inp = inputtxt.get(1.0, "end-1c")
	inp = inp.replace('\n', '')

	try:
		command = event.keysym
	except:
		command = event

	if not inp:
		# If the text input was empty

		global image_index
		global current_image_path

		now = datetime.datetime.now()

		if command == 'Right':
			file_log.write('\tREMOVED\t\t\t' + str(now)[:19] + '\t' + current_image_path + '\n')
			move_image('removed')
		elif command == 'Down':
			file_log.write('\tSAVED\t\t\t' + str(now)[:19] + '\t' + current_image_path + '\n')
			move_image('saved')

		image_index += 1
		if image_index < num_images:
			current_image_path = all_images_path[image_index]
			update_image()
			print('next image')
		else:
			no_more_photos()

	else:
		entered_text('event')


def no_more_photos():

	print('no more photos')

	file_log.close()

	image_frame.destroy()
	image_label.destroy()

	text_label.config(text="No more photos. Type 'exit'", font=("Helvetica", 40))

	text_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
	text_input_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)


def t_program():
	global name_source_path, file_log

	name_source_path = 'test_directory'
	reference_test_path = 'reference_test_directory'

	if os.path.exists(name_source_path):
		shutil.rmtree(name_source_path)

	shutil.copytree(reference_test_path, name_source_path)

	start_process(source_directory_path=name_source_path)
	answer_1 = set(find_all_files(source_directory_path=name_source_path, filter_results=False))

	correct_answer_1 = {
		'test_directory/file_20.PNG',
		'test_directory/file_15.JPG',
		'test_directory/directory_3/file_19.JPG',
		'test_directory/directory_3/file_4.PNG',
		'test_directory/directory_3/file_22.JPG',
		'test_directory/directory_3/file_15.JPG',
		'test_directory/directory_2/file_23.JPG',
		'test_directory/directory_2/file_3.JPG',
		'test_directory/directory_2/file_2.png',
		'test_directory/directory_2/directory_7/file_20.PNG',
		'test_directory/directory_2/directory_7/file_11.jpg',
		'test_directory/directory_2/directory_6/file_3.JPG',
		'test_directory/directory_2/directory_6/file_9.png',
		'test_directory/directory_1/file_4.PNG',
		'test_directory/directory_1/file_3.JPG',
		'test_directory/directory_1/file_2.png',
		'test_directory/directory_1/file_11.jpg',
		'test_directory/directory_1/file_15.JPG',
		'test_directory/directory_1/directory_4/file_4.PNG',
		'test_directory/directory_1/directory_4/file_18.PNG',
		'test_directory/directory_1/directory_4/file_13.PNG',
		'test_directory/directory_1/directory_4/directory_8/file_17.jpg',
		'test_directory/directory_1/directory_4/directory_8/directory_9/file_7.JPG',
		'test_directory/directory_1/directory_4/directory_8/directory_9/file_22.JPG',
		'test_directory/directory_1/directory_5/file_2.png',
		'test_directory/directory_1/directory_5/directory_10/file_7.JPG'
	}

	next_image('Right')  # 1
	next_image('Right')  # 2
	next_image('Right')  # 3
	next_image('Right')  # 4
	next_image('Down')  # 5
	next_image('Right')  # 6
	next_image('Right')  # 7
	undo('event')  # 8
	next_image('Down')  # 9
	next_image('Right')  # 10
	next_image('Down')  # 11
	next_image('Down')  # 12
	undo('event')  # 13
	next_image('Right')  # 14
	next_image('Down')  # 15
	other_input('ab')  # 16
	next_image('Down')  # 17
	next_image('Right')  # 18
	other_input('ac')  # 19
	undo('event')  # 20
	other_input('ab')  # 21
	next_image('Down')  # 22

	answer_2 = set(find_all_files(source_directory_path=name_source_path, filter_results=False))

	correct_answer_2 = {
		'test_directory/sorted_images/removed_images/file_19.JPG',
		'test_directory/sorted_images/removed_images/file_4.PNG',
		'test_directory/sorted_images/removed_images/file_20.PNG',
		'test_directory/sorted_images/removed_images/file_15_1.JPG',
		'test_directory/sorted_images/removed_images/file_3.JPG',
		'test_directory/sorted_images/removed_images/file_15.JPG',
		'test_directory/sorted_images/removed_images/file_20_1.PNG',
		'test_directory/sorted_images/removed_images/file_4_1.PNG',
		'test_directory/sorted_images/ab/file_3.JPG',
		'test_directory/sorted_images/ab/file_3_1.JPG',
		'test_directory/sorted_images/saved_images/file_23.JPG',
		'test_directory/sorted_images/saved_images/file_2.png',
		'test_directory/sorted_images/saved_images/file_22.JPG',
		'test_directory/sorted_images/saved_images/file_11.jpg',
		'test_directory/sorted_images/saved_images/file_9.png',
		'test_directory/sorted_images/saved_images/file_2_1.png',
		'test_directory/directory_1/file_11.jpg',
		'test_directory/directory_1/file_15.JPG',
		'test_directory/directory_1/directory_4/file_4.PNG',
		'test_directory/directory_1/directory_4/file_18.PNG',
		'test_directory/directory_1/directory_4/file_13.PNG',
		'test_directory/directory_1/directory_4/directory_8/file_17.jpg',
		'test_directory/directory_1/directory_4/directory_8/directory_9/file_7.JPG',
		'test_directory/directory_1/directory_4/directory_8/directory_9/file_22.JPG',
		'test_directory/directory_1/directory_5/file_2.png',
		'test_directory/directory_1/directory_5/directory_10/file_7.JPG'
	}

	next_image('Down')  # 23
	next_image('Right')  # 24
	next_image('Right')  # 25
	other_input('1121')  # 26
	next_image('Down')  # 27
	undo('event')  # 28
	undo('event')  # 29
	undo('event')  # 30
	undo('event')  # 31
	other_input('new')  # 32
	next_image('Right')  # 33
	other_input('1122')  # 34
	next_image('Down')  # 35
	next_image('Down')  # 36

	answer_3 = set(find_all_files(source_directory_path=name_source_path, filter_results=False))

	correct_answer_3 = {
		'test_directory/sorted_images/removed_images/file_19.JPG',
		'test_directory/sorted_images/removed_images/file_4.PNG',
		'test_directory/sorted_images/removed_images/file_20.PNG',
		'test_directory/sorted_images/removed_images/file_15_1.JPG',
		'test_directory/sorted_images/removed_images/file_3.JPG',
		'test_directory/sorted_images/removed_images/file_15.JPG',
		'test_directory/sorted_images/removed_images/file_20_1.PNG',
		'test_directory/sorted_images/removed_images/file_4_2.PNG',
		'test_directory/sorted_images/removed_images/file_4_1.PNG',
		'test_directory/sorted_images/1122/file_18.PNG',
		'test_directory/sorted_images/ab/file_3.JPG',
		'test_directory/sorted_images/ab/file_3_1.JPG',
		'test_directory/sorted_images/saved_images/file_11_1.jpg',
		'test_directory/sorted_images/saved_images/file_23.JPG',
		'test_directory/sorted_images/saved_images/file_2.png',
		'test_directory/sorted_images/saved_images/file_22.JPG',
		'test_directory/sorted_images/saved_images/file_13.PNG',
		'test_directory/sorted_images/saved_images/file_11.jpg',
		'test_directory/sorted_images/saved_images/file_9.png',
		'test_directory/sorted_images/saved_images/file_17.jpg',
		'test_directory/sorted_images/saved_images/file_2_1.png',
		'test_directory/sorted_images/new/file_15.JPG',
		'test_directory/directory_1/directory_4/directory_8/directory_9/file_7.JPG',
		'test_directory/directory_1/directory_4/directory_8/directory_9/file_22.JPG',
		'test_directory/directory_1/directory_5/file_2.png',
		'test_directory/directory_1/directory_5/directory_10/file_7.JPG'
	}

	next_image('Down')  # 37
	other_input('ac')  # 38
	other_input('new')  # 39
	undo('event')  # 40
	other_input('1122')  # 41
	next_image('Down')  # 42

	answer_4 = set(find_all_files(source_directory_path=name_source_path, filter_results=False))

	correct_answer_4 = {
		'test_directory/sorted_images/removed_images/file_19.JPG',
		'test_directory/sorted_images/removed_images/file_4.PNG',
		'test_directory/sorted_images/removed_images/file_20.PNG',
		'test_directory/sorted_images/removed_images/file_15_1.JPG',
		'test_directory/sorted_images/removed_images/file_3.JPG',
		'test_directory/sorted_images/removed_images/file_15.JPG',
		'test_directory/sorted_images/removed_images/file_20_1.PNG',
		'test_directory/sorted_images/removed_images/file_4_2.PNG',
		'test_directory/sorted_images/removed_images/file_4_1.PNG',
		'test_directory/sorted_images/ac/file_22.JPG',
		'test_directory/sorted_images/1122/file_18.PNG',
		'test_directory/sorted_images/1122/file_2.png',
		'test_directory/sorted_images/ab/file_3.JPG',
		'test_directory/sorted_images/ab/file_3_1.JPG',
		'test_directory/sorted_images/saved_images/file_7.JPG',
		'test_directory/sorted_images/saved_images/file_11_1.jpg',
		'test_directory/sorted_images/saved_images/file_23.JPG',
		'test_directory/sorted_images/saved_images/file_2.png',
		'test_directory/sorted_images/saved_images/file_22.JPG',
		'test_directory/sorted_images/saved_images/file_13.PNG',
		'test_directory/sorted_images/saved_images/file_7_1.JPG',
		'test_directory/sorted_images/saved_images/file_11.jpg',
		'test_directory/sorted_images/saved_images/file_9.png',
		'test_directory/sorted_images/saved_images/file_17.jpg',
		'test_directory/sorted_images/saved_images/file_2_1.png',
		'test_directory/sorted_images/new/file_15.JPG',
	}

	all_tests_passed = True

	if answer_1 == correct_answer_1:
		print('Test 1 passed')
	else:
		print('Test 1 NOT passed')
		all_tests_passed = False

	if answer_2 == correct_answer_2:
		print('Test 2 passed')
	else:
		print('Test 2 NOT passed')
		all_tests_passed = False

	if answer_3 == correct_answer_3:
		print('Test 3 passed')
	else:
		print('Test 3 NOT passed')
		all_tests_passed = False

	if answer_4 == correct_answer_4:
		print('Test 4 passed')
	else:
		print('Test 4 NOT passed')
		all_tests_passed = False

	if all_tests_passed:
		information_text_label.config(text='All tests passed', font=("Helvetica", 30))
	else:
		information_text_label.config(text='Some testst failed', font=("Helvetica", 30))


def other_input(inp):
	global directory_dictionary, image_index, current_image_path

	directory_dictionary[inp] = create_directory( root_sorted_path + '/' + inp, source_path=name_source_path)
	now = datetime.datetime.now()
	file_log.write('\tMoved to ' + inp + '\t\t' + str(now)[:19] + '\t' + current_image_path + '\n')
	move_image(inp)
	image_index += 1
	if image_index < num_images:
		current_image_path = all_images_path[image_index]
		update_image()
		print('next image')
	else:
		no_more_photos()


def exit_program():
	root.destroy()


def entered_text(event):

	inp = inputtxt.get(1.0, "end-1c")
	inp = inp.replace('\n', '')
	if inp:
		print(f'Text = {inp}')
		inputtxt.delete(1.0, tk.END)
		if inp.lower() == 'exit':
			exit_program()
		elif inp.lower() == 'start':
			start_process()
		elif inp.lower() == 'test':
			t_program()
		else:
			other_input(inp)


def start_process(source_directory_path=name_source_path):
	global all_images_path, num_images, image_index, current_image_path, movement_records
	global directory_dictionary, file_log

	file_log = open(source_directory_path + '/image_changes.txt', 'a')

	all_images_path = find_all_files(source_directory_path=source_directory_path)
	num_images = len(all_images_path)
	image_index = 0
	if len(all_images_path) > 0:

		movement_records = []
		save_images_directory_path = create_directory(name_saved_path, source_path=name_source_path)
		removed_images_directory_path = create_directory(name_removed_path, source_path=name_source_path)

		directory_dictionary = {'saved': save_images_directory_path, 'removed': removed_images_directory_path}

		image_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER, relwidth=0.7, relheight=0.7)
		text_input_frame.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
		image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
		text_label.place(relx=0.7, rely=0.9, anchor=tk.CENTER)
		information_text_label.place(relx=0.1, rely=0.025, anchor=tk.NW)

		current_image_path = all_images_path[image_index]
		update_image()
	else:
		print('no images')


def update_image():
	text_label.config(text=f'Image {image_index+1} of {num_images}', font=("Helvetica", 40))
	information_text_label.config(text=current_image_path, font=("Helvetica", 30))

	# print(f'Current image = {current_image_path}')
	original_image = Image.open(current_image_path)

	image_height = original_image.size[1]
	image_width = original_image.size[0]

	image_as = image_width/image_height

	image_frame.update()
	image_frame_width = image_frame.winfo_width()
	image_frame_height = image_frame.winfo_height()

	frame_as = image_frame_width/image_frame_height

	if image_as > frame_as:
		new_image_width = int(round(image_frame_width))
		new_image_height = int(round((1/image_as)*image_frame_width))
	else:
		new_image_height = int(round(image_frame_height))
		new_image_width = int(round(image_as*image_frame_height))

	# print(f'width = {new_image_width}, height = {new_image_height}')

	resized = original_image.resize((new_image_width, new_image_height), Image.LANCZOS)
	img = ImageTk.PhotoImage(resized)
	image_label.image = img
	image_label.config(image=img)


def window_resize(event):
	update_image()
	print(event)


root = tk.Tk()
root.title("Image view")

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

w = int(round(ws*0.8)) # width for the Tk root
h = int(round(hs*0.8)) # height for the Tk root

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))


image_frame = tk.Frame(root)
text_input_frame = ttk.Frame(root)
image_label = tk.Label(image_frame)
text_label = tk.Label(root)
information_text_label = tk.Label(root)

text_label.config(text="Type 'start'", font=("Helvetica", 40))

text_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
text_input_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)



inputtxt = tk.Text(text_input_frame, height=1, width=20, font=("Helvetica", 40))
inputtxt.pack()
inputtxt.bind('<Right>', next_image)
inputtxt.bind('<Left>', undo)
inputtxt.bind('<Down>', next_image)
inputtxt.bind('<Return>', entered_text)
inputtxt.bind("<Shift_L>", window_resize)
inputtxt.focus()





root.mainloop()
