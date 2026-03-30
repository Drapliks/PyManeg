from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from newfile import newFile
from datetime import date
from openfile import openFile
from deletefile import deleteFile
from newproject import newProject
from openproject import openProject
from deleteproject import deleteProject
import os
import sys

def closeProggram():
    sys.exit()

today = date.today()
username = os.getlogin()

root = Tk()
root.geometry("330x410")
root.title("Pysapce")
root.resizable(width=False, height=False)

welcomeText = Label(root, text="Welcome " + username + "!")
welcomeText.pack()

todayDateText = Label(root, text="Today is " + str(today))
todayDateText.pack()

emptySpace = Label(root, text="")
emptySpace.pack()

filesParter1 = Label(root, text="------Files------")
filesParter1.pack()

newFileButt = Button(root, text="New file", command=newFile)
newFileButt.pack()

openFileButt = Button(root, text="Open file", command=openFile)
openFileButt.pack()

deleteFileButt = Button(root, text="Delete file", command=deleteFile)
deleteFileButt.pack()

filesParter2 = Label(root, text="-----------------")
filesParter2.pack()

emptySpace = Label(root, text="")
emptySpace.pack()

projectsParter1 = Label(root, text="------Projects------")
projectsParter1.pack()

newProjectButt = Button(root, text="New project", command=newProject)
newProjectButt.pack()

openProjectButt = Button(root, text="Open project", command=openProject)
openProjectButt.pack()

deleteProjectButt = Button(root, text="Delete project", command=deleteProject)
deleteProjectButt.pack()

projectsParter2 = Label(root, text="--------------------")
projectsParter2.pack()

exitButt = Button(root, text="Exit", command=closeProggram)
exitButt.pack(side=BOTTOM)

root.mainloop()