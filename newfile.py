from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

def newFile():
    
    def openDir():
        path2file = filedialog.askdirectory() + " " + newFileName.get()

        os.system("touch " + path2file)

        fileNameWindow.destroy()

    fileNameWindow = Toplevel()
    fileNameWindow.geometry("390x130")
    fileNameWindow.resizable(width=False, height=False)
    fileNameWindow.title("New file")

    enterNewFileNameText = Label(fileNameWindow, text="Enter file name:")
    enterNewFileNameText.pack(side=LEFT)
    
    newFileName = Entry(fileNameWindow)
    newFileName.pack(side=LEFT)
    
    createbutt = Button(fileNameWindow, text="Create", command=openDir)
    createbutt.pack(side=LEFT)

if __name__ == "__main__":
    root = Tk()
    newFile(root)
    root.mainloop()