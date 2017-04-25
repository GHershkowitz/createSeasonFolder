import os
import shutil
from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw()
# show an "Open" dialog box and return the path to the selected file

# ask for the directory the user wants to use
location = askdirectory()

# function to create Folders and sort filess.


def folderMaker(one_up):
    for num in range(1, 50):
        #Format files S0XEXX - Season # Episode #
        if num < 10:
            seasonNum = "S0" + str(num)
        #Format Files SXXEXX - Season # Episode #
        else:
            seasonNum = "S" + str(num)

        # checking for files with those prefixes
        if filename.startswith(seasonNum):
            directory = one_up + "/Season " + str(num)

            # move into directory if it exists, if not, create one
            if not os.path.exists(directory):
                os.makedirs(directory)
                shutil.move(f, directory)
            else:
                shutil.move(f, directory)


for path, subdirs, files in os.walk(location):
    for filename in sorted(files):
        f = os.path.join(path, filename)

        # folder name one up, containing the file
        one_up = os.path.normpath(os.path.join(f, '../'))

        folderMaker(one_up)
