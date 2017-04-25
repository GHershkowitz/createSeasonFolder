import os
import shutil
from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
# show an "Open" dialog box and return the path to the selected file

# ask for the directory the user wants to use
location = askdirectory(
    initialdir="C:/Users/Greg/Downloads/Media/TV Shows/")


def folderMaker(one_up):
    for num in range(1, 50):
        if num < 10:
            seasonNum = "S0" + str(num)
        else:
            seasonNum = "S" + str(num)

        if filename.startswith(seasonNum):
            directory = one_up + "/Season " + str(num)

            if not os.path.exists(directory):
                os.makedirs(directory)
                shutil.move(f, directory)
            else:
                shutil.move(f, directory)


for path, subdirs, files in os.walk(location):
    for filename in sorted(files):
        f = os.path.join(path, filename)
        SearchResultFileName = (os.path.split(f)[1])
        one_up = os.path.normpath(os.path.join(f, '../'))

        folderMaker(one_up)
