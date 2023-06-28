from exif import Image

folder_path = 'other_images'
img_filename = 'IMG_9314 Large.jpeg'

img_path = f'{folder_path}/{img_filename}'

with open(img_path, 'rb') as img_file:
	img = Image(img_file)

print(img.has_exif)

# Original datetime that image was taken (photographed)
print(f'DateTime (Original): {img.get("datetime_original")}')

