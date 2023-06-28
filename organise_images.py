import os.path, time
from PIL import Image, ExifTags

folder_path = 'other_images'

# img_filename = '0b0a9861-9f3d-4801-94dd-9c9db7056889.jpg'
# img_filename = 'IMG_5041.PNG'
# img_filename = 'IMG_9314 Large.jpeg'
# img_filename = 'IMG_9314.HEIC'
# img_filename = 'IMG_1415.HEIC'
img_filename = 'IMG_1415 Large.jpeg'
# img_filename = 'IMG_1535.PNG'



img_path = f'{folder_path}/{img_filename}'


print("created: %s" % time.ctime(os.stat(img_path).st_birthtime))


img = Image.open(img_path)

image_exif = img._getexif()

if image_exif is not None:
	exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
	print(f"Date Time Original = {exif['DateTimeOriginal']}")

else:
	print('No Exif')

