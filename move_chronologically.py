import os.path, time
from PIL import Image, ExifTags
from os import walk, rename

folder_path = 'other_images'
resulting_folder = 'resulting_images'
new_path = resulting_folder + '/' + 'all_photos_and_images'

if not os.path.exists(new_path):
    os.makedirs(new_path)

copy_file_extensions = ['.jpg', '.jpeg', '.png']

file_names = []
assigned_years = []


def create_year_directory(year, source_path):
    year_path = source_path + '/' + year
    os.makedirs(year_path)

    for month_number in range(12):
        month_path = year_path + '/' + year + '_' + str(month_number + 1).zfill(2)
        os.makedirs(month_path)


for (dirpath, dirnames, filenames) in walk(folder_path):
    for single_file in filenames:
        complete_path = dirpath + '/' + single_file
        file_name, file_extension = os.path.splitext(complete_path)

        if file_extension.lower() in copy_file_extensions:
            file_names.append(complete_path)

assigned_names = []

for img_path in file_names:

    _, file_extension = os.path.splitext(img_path)
    img = Image.open(img_path)

    image_exif = img._getexif()

    original_time = None

    if image_exif is not None:
        exif = {ExifTags.TAGS[k]: v for k, v in image_exif.items() if k in ExifTags.TAGS}

        if 'DateTimeOriginal' in exif.keys():
            original_time = exif['DateTimeOriginal']
            creation_time = original_time[0:4] + '_' + original_time[5:7] + '_' + original_time[8:10] + '_' + \
                            original_time[11:13] + '_' + original_time[14:16] + '_' + original_time[17:19]
            creation_year = int(original_time[0:4])
            creation_month = int(original_time[5:7])

    if original_time is None:
        original_time = time.gmtime(os.stat(img_path).st_birthtime)
        creation_time = str(original_time.tm_year) + '_' + str(original_time.tm_mon).zfill(2) + '_' + \
                        str(original_time.tm_mday).zfill(2) + '_' + str(original_time.tm_hour).zfill(2) \
                        + '_' + str(original_time.tm_min).zfill(2) + '_' + \
                        str(original_time.tm_sec).zfill(2)
        creation_year = original_time.tm_year
        creation_month = original_time.tm_mon

    original_name = img_path
    new_name = new_path + '/' + str(creation_year) + '/' + str(creation_year) + '_' + str(creation_month).zfill(2) + '/' + creation_time + file_extension.lower()
    if new_name in assigned_names:
        repeated_counter = 0
        repeated_name = True
        while repeated_name:
            repeated_counter += 1
            new_name = new_path + '/' + str(creation_year) + '/' + str(creation_year) + '_' + str(creation_month).zfill(2) + '/' + creation_time + '_' + str(repeated_counter) + file_extension.lower()
            if not(new_name in assigned_names):
                repeated_name = False

    if not (creation_year in assigned_years):
        create_year_directory(str(creation_year), new_path)
        assigned_years.append(creation_year)

    rename(original_name, new_name)
    print(f"{original_name} -> {new_name}")
    assigned_names.append(new_name)


