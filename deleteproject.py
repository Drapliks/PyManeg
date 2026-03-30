from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

def deleteProject():
    path2Dir = filedialog.askdirectory()
    if path2Dir != "":
        def yespress():
            os.system(f'rm -rf ' + path2Dir)
            areYouSureWindow.destroy()
                
        def nopress():
            areYouSureWindow.destroy()
                
        areYouSureWindow = Toplevel()
        areYouSureWindow.geometry("230x165")
        areYouSureWindow.resizable(width=False, height=False)
        areYouSureWindow.title("Are you sure?")
                
        quest = Label(areYouSureWindow, text=f'Delete project?')
        quest.pack()
                
        yesbutt = Button(areYouSureWindow, text="Yes", command=yespress)
        yesbutt.pack(side=LEFT)
                
        nobutt = Button(areYouSureWindow, text='No', command=nopress)
        nobutt.pack(side=RIGHT)

if __name__ == "__main__":
    root = Tk()
    deleteProject(root)
    root.mainloop()