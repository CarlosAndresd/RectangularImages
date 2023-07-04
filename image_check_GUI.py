import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from os import walk, rename, remove
import os.path
import datetime
import shutil

global image_index, current_image_path, num_images, movement_records, directory_dictionary, file_log

name_source_path = 'images_GUI'
name_saved_path = 'saved_images'
name_removed_path = 'removed_images'


def create_directory(directory_name, source_path=name_source_path):
	complete_path = source_path + '/' + directory_name
	if not os.path.exists(complete_path):
		os.makedirs(complete_path)

	return complete_path


def find_all_files(source_directory_path=name_source_path, copy_file_extensions=('.jpg', '.png', '.jpeg')):
	file_names = []

	for (directory_path, directory_name, filenames) in walk(source_directory_path):
		if directory_path != name_source_path + '/' + name_saved_path:
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
	file_log.write('\tUNDO\t\t' + str(now)[:19] + '\t' + old_path + ' -> ' + new_path + '\n')
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

	image_frame.destroy()
	image_label.destroy()

	text_label.config(text="Type 'exit'", font=("Helvetica", 40))

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
	print(all_images_path)

	# Test 'saving' and 'removing' images
	next_image('Right')
	next_image('Down')
	next_image('Right')
	next_image('Right')
	next_image('Down')

	# Test the undo functionality
	next_image('Down')
	undo('event')
	next_image('Right')
	next_image('Right')



def other_input(inp):
	global directory_dictionary, image_index, current_image_path

	directory_dictionary[inp] = create_directory(inp)
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


def entered_text(event):

	inp = inputtxt.get(1.0, "end-1c")
	inp = inp.replace('\n', '')
	print(f'Text = {inp}')
	inputtxt.delete(1.0, tk.END)
	if inp.lower() == 'exit':
		root.destroy()
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
		save_images_directory_path = create_directory(name_saved_path)
		removed_images_directory_path = create_directory(name_removed_path)

		directory_dictionary = {'saved': save_images_directory_path, 'removed': removed_images_directory_path}

		image_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER, relwidth=0.7, relheight=0.7)
		text_input_frame.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
		image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
		text_label.place(relx=0.7, rely=0.9, anchor=tk.CENTER)

		current_image_path = all_images_path[image_index]
		update_image()
	else:
		print('no images')


def update_image():
	text_label.config(text=f'Image {image_index+1} of {num_images}', font=("Helvetica", 40))

	print(f'Current image = {current_image_path}')
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

	print(f'width = {new_image_width}, height = {new_image_height}')

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
