import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from os import walk


def find_all_files(source_directory_path, copy_file_extensions=('.jpg', '.png', '.jpeg')):
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
	print('next image')


def save_image(event):
	print('save image')


def entered_text(event):
	inp = inputtxt.get(1.0, "end-1c")
	print(f'Text = {inp}')
	inputtxt.delete(1.0, tk.END)
	if inp.lower() == 'exit':
		root.destroy()

root = tk.Tk()

image_frame = ttk.Frame(root)
image_frame.pack()

text_input_frame = ttk.Frame(root)
text_input_frame.pack()


image_path = 'images_GUI/5QpPfOY-mathematics-wallpaper.jpg'
img = ImageTk.PhotoImage(Image.open(image_path))
image_label = tk.Label(image_frame, image=img)
image_label.pack(side="bottom", fill="both", expand="yes")


inputtxt = tk.Text(text_input_frame,height=5,width=20)
inputtxt.pack()
inputtxt.bind('<Right>', next_image)
inputtxt.bind('<Down>', save_image)
inputtxt.bind('<Return>', entered_text)
inputtxt.focus()

root.mainloop()
