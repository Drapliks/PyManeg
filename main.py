from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from newfile import newFile
from datetime import date
from openfile import openFile
from deletefile import deleteFile
import os
import sys

today = date.today()
username = os.getlogin()

root = Tk()
root.geometry("330x450")
root.title("Pysapce")
root.resizable(width=False, height=False)

welcomeText = Label(root, text="Welcome " + username + "!")
welcomeText.pack()

todayDateText = Label(root, text="Today is " + str(today))
todayDateText.pack()

newFileButt = Button(root, text="New file", command=newFile)
newFileButt.pack()

openFileButt = Button(root, text="Open file", command=openFile)
openFileButt.pack()

renameFileButt = Button(root, text="Rename file", command=renameFile)
renameFileButt.pack()

deleteFileButt = Button(root, text="Delete file", command=deleteFile)
deleteFileButt.pack()

root.mainloop()