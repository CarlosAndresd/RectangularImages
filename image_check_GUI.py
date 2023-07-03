import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from os import walk
import os.path

global image_index, current_image_path

def find_all_files(source_directory_path='images_GUI', copy_file_extensions=('.jpg', '.png', '.jpeg')):
	file_names = []

	for (directory_path, _, filenames) in walk(source_directory_path):
		for single_file in filenames:
			if single_file != '.DS_Store':
				# print(single_file)
				complete_path = directory_path + '/' + single_file
				_, file_extension = os.path.splitext(complete_path)

				if file_extension.lower() in copy_file_extensions:
					file_names.append(complete_path)

	return file_names


def next_image(event):

	global image_index
	global current_image_path

	image_index += 1
	current_image_path = all_images_path[image_index]
	update_image()
	print('next image')


def save_image(event):
	print('save image')


def entered_text(event):
	inp = inputtxt.get(1.0, "end-1c")
	print(f'Text = {inp}')
	inputtxt.delete(1.0, tk.END)
	if inp.lower() == 'exit':
		root.destroy()


def update_image():

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
image_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER, relwidth=0.7, relheight=0.7)


text_input_frame = ttk.Frame(root)
text_input_frame.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

image_label = tk.Label(image_frame)
image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


all_images_path = find_all_files()
selected_images = []
image_index = 0
current_image_path = all_images_path[image_index]
update_image()

inputtxt = tk.Text(text_input_frame,height=5,width=20)
inputtxt.pack()
inputtxt.bind('<Right>', next_image)
inputtxt.bind('<Down>', save_image)
inputtxt.bind('<Return>', entered_text)
inputtxt.bind("<Shift_L>", window_resize)
inputtxt.focus()

root.mainloop()
