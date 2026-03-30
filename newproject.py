from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

def newProject():

    def creating():
        path2Dir = filedialog.askdirectory()
        print(path2Dir)
        os.mkdir(path2Dir + "/" + newProjectName.get())
        os.system("python -m venv " + path2Dir + "/" + newProjectName.get() + "/venv")
        os.system("touch " + path2Dir + "/" + newProjectName.get() + "/main.py")
        newProjectNameWindow.destroy()

    newProjectNameWindow = Toplevel()
    newProjectNameWindow.geometry("390x130")
    newProjectNameWindow.resizable(width=False, height=False)
    newProjectNameWindow.title("New project")

    enterNewProjectNameText = Label(newProjectNameWindow, text="Enter project name:")
    enterNewProjectNameText.pack(side=LEFT)
    
    newProjectName = Entry(newProjectNameWindow)
    newProjectName.pack(side=LEFT)
    
    createbutt = Button(newProjectNameWindow, text="Create", command=creating)
    createbutt.pack(side=LEFT)


if __name__ == "__main__":
    root = Tk()
    newProject(root)
    root.mainloop()