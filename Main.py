#1. Get StartText and EndText which will be appended onto the Filenames and Foldernames
#1.1 Inputbox for StartText and EndText

#2. Changing folder and file names   
#2.1 Select directory 
#2.2 Work through all Folders
#2.3 Get all file paths

import turtle 
import tkinter
from tkinter import filedialog
import os
StartText = ''
StartText = tkinter.simpledialog.askstring("StartText", "please enter the text which should be added to the beginning of the filename.")
#EndText = tkinter.simpledialog.askstring("EndText", "please enter the text which should be added to the ending of the filename.")
DirPath = filedialog.askdirectory()
DirPath += '/'


for path, subdirs, files in os.walk(DirPath):
    for name in files:
        if not (str.__contains__(name,StartText)):
            NewFileName = os.path.join(path, StartText + name)
            os.rename(os.path.join(path, name),NewFileName)
        else:
            print("Doesnt need to be changed!")
