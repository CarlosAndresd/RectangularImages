# Rectangular Images

This is an ongoing personal project

## **Idea:** 

The program consists of two parts:

### Part 1

When executing this project a GUI will appear, in that GUI the user will be able to select a directory, lets call this directory `root`. The program will scan all the contents of the `root` directory and create a list of all the files contained in `root` that have a `.jpg`, `.jpeg` or `.png` extension.

Then the GUI will show the user the first image. The user can do one of five things:

1. Press the **Right** arrow: this means that that image will be erased.
2. Press the **Down** arrow: this means that the image will be saved in a separate directory with a default name.
3. Type `exit`, this will exit the program, more on that later.
4. Type any name (except for reserved names like `exit`) and then press **Return** of the **Right** arrow. This will move the images to a directory with that name, if the directory does not exist, it is created.
5. Press the **Left** arrow: this will undo the last action, unless it was exit (the creation of a new directory is not undone either).

By doing actions 1, 2, or 4, the user goes along all the images that were originally listed. Except for action 3, all actions are in reality moving one file at a time (and if necessary creating new directories). Because this is done in real time, when the user types `exit` all changes are kept and if the same `root` directory is selected later, then the user can continue where it was left off.

The saved images are stored in a directory inside `root` called `sorted_images`, this directory is ignored when the program first looks for the images.

**About `exit`** 

When the user exits the program, all the files that should be erased (because the user pressed **Right**) are erased.

Once the user has classified all the images the program goes to Part 2.

### Part 2

At the start of this part, the directory `sorted_images` should contain other directories, and these directories contain `jpg`, `jpeg`, or `png` files. The program first makes a list of all the directories contained in `sorted_images` and asks the user to provide a number between 0 and 1 for each directory, then it lists all the images contained in the `sorted_images` directory assigning them the number corresponding to the directory that contains them.

After this is done, all the listed images are arranged randomly in a sort of collage, where the size of the image is proportional to the number it was assigned. The resulting collage is presented to the user which can decide to save it, or to create another collage (since the positioning of the images is random there are many possibilities).

### Part 0

Technically, this is not a part of the program, but is something in the project. 

This is a separate script that organises files depending on the creation or modification date. If it is an image it will try to look into the exif data for the creation date.

This complementary program can be used as a preparation step, since this file organisation can be used to determine which images to include in the collage.

## Execution:

All the programs will be writen in Python, however LaTex will be used for the creation of the final collage.

I envision this project as being composed of four main parts or scripts:

1. The *organising program*: This is the script that organises all the files contained in a source directory in a destination directory according to the creation or modification date.
2. The *classification program*: This is the GUI that shows the user the images, such that the used can easily and fast classify which images to keep and in which directories.
3. The *numbering program*: This is also part of the GUI, it will look for the directories in the `sorted_images` directory and ask the user for a number, then it will do all the preprocessing of listing all the images and assigning them a number for the collage to be created.
4. The *collage program*: This is the program that creates the collage and shows it to the user.

The first script will work independently. While the other three work together in the same GUI.

## Current state:

### *organising program*:
This part of the program is completed, name of the main script is `move_chronologically.py`. This part has some auxiliary files/directories:

- `tests_move_chronologically.py` is the module that contains the tests for this part. To execute it simply type `pytest tests_move_chronologically.py -vv` (before, make sure you are in a virtual environment, type `source venv/bin/activate`).
- `reference_test_directory` this is the directory that contains all the files that are used for the testing.
- `Test_Photo_Information.xlsx` this is the Excel file that can be used to write the tests.

Documentation is still missing.

### *classification program*:
The main functionality of the program is completed, but the tests are missing. The name of the main script is `image_check_GUI.py`, it will execute the GUI and all the functionality should be there (the only thing missing is that after the user exists, the directory containing the images to be erased, is actually erased).

Some other details also need to be ironed out, like asking the user for the directory to be analysed (right now, it looks for a directory called `images_GUI`).

However, tests are still missing. By the nature of the GUI I decided to incorporate the tests in the main program itself and not use `pytest`. The images that are used for testing are also the ones from the `reference_test_directory` directory.

Documentation is still missing.

### *numbering program*:
I have not done anything regarding this program.

### *collage program*:
The core functionality of this program sort of exist, however, many things still need to be done. Currently, the program reads the image name and number from an Excel file, it also has hardcoded the relative image size and assumes that all the images have the same aspect ratio.

The main script is called `main.py`, when executed, it reads the Excel file and writes the LaTex file that when compiled creates the collage.















