from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

def openProject():

    def closeProject():
        projectWindow.destroy()
    def openMaindotPy():
        path2file = path2Dir + "/main.py"
        
        def save():
            if path2file != "":
                text = codeEditor.get("1.0", END)
                with open(path2file, "w") as file:
                    file.write(text)

        def saveAndExit():
            if path2file != "":
                text = codeEditor.get("1.0", END)
                with open(path2file, "w") as file:
                    file.write(text)
            codeSpace.destroy()
        
        def exitFromFile():
            codeSpace.destroy()

        codeSpace = Toplevel()
        codeSpace.title(path2file)
        codeSpace.resizable(width=False,height=False)

        codeEditor = Text(codeSpace)
        codeEditor.pack()
        
        saveFileButt = Button(codeSpace, text="Save", command=save)
        saveFileButt.pack(side=LEFT)

        saveAndExitFileButt = Button(codeSpace, text="Save&Exit", command=saveAndExit)
        saveAndExitFileButt.pack(side=LEFT)

        saveAndExitFileButt = Button(codeSpace, text="Exit", command=exitFromFile)
        saveAndExitFileButt.pack(side=RIGHT)

        if path2file != "":
            with open(path2file, "r") as file:
                text = file.read()
                codeEditor.delete("1.0", END)
                codeEditor.insert("1.0", text)

    def newFile():
        def openDir():
            path2file = path2Dir + "/" + newFileName.get()
            os.system("touch " + path2file)
            newfileNameWindow.destroy()

        newfileNameWindow = Toplevel()
        newfileNameWindow.geometry("390x130")
        newfileNameWindow.resizable(width=False, height=False)
        newfileNameWindow.title("New file")

        enterNewFileNameText = Label(newfileNameWindow, text="Enter file name:")
        enterNewFileNameText.pack(side=LEFT)
        
        newFileName = Entry(newfileNameWindow)
        newFileName.pack(side=LEFT)
        
        createbutt = Button(newfileNameWindow, text="Create", command=openDir)
        createbutt.pack(side=LEFT)

    def openFile():
        path2file = filedialog.askopenfilename()
        def save():
            if path2file != "":
                text = codeEditor.get("1.0", END)
                with open(path2file, "w") as file:
                    file.write(text)

        def saveAndExit():
            if path2file != "":
                text = codeEditor.get("1.0", END)
                with open(path2file, "w") as file:
                    file.write(text)
            codeSpace.destroy()
        
        def exitFromFile():
            codeSpace.destroy()

        codeSpace = Toplevel()
        codeSpace.title(path2file)
        codeSpace.resizable(width=False,height=False)

        codeEditor = Text(codeSpace)
        codeEditor.pack()
        
        saveFileButt = Button(codeSpace, text="Save", command=save)
        saveFileButt.pack(side=LEFT)

        saveAndExitFileButt = Button(codeSpace, text="Save&Exit", command=saveAndExit)
        saveAndExitFileButt.pack(side=LEFT)

        saveAndExitFileButt = Button(codeSpace, text="Exit", command=exitFromFile)
        saveAndExitFileButt.pack(side=RIGHT)

        if path2file != "":
            with open(path2file, "r") as file:
                text = file.read()
                codeEditor.delete("1.0", END)
                codeEditor.insert("1.0", text)

    def deleteFile():
        path2file = filedialog.askopenfilename()
        if path2file != "":
            def yespress():
                os.system(f'rm -rf ' + path2file)
                areYouSureWindow.destroy()
                    
            def nopress():
                areYouSureWindow.destroy()
                    
            areYouSureWindow = Toplevel()
            areYouSureWindow.geometry("230x165")
            areYouSureWindow.resizable(width=False, height=False)
            areYouSureWindow.title("Are you sure?")
                    
            quest = Label(areYouSureWindow, text=f'Delete file?')
            quest.pack()
                    
            yesbutt = Button(areYouSureWindow, text="Yes", command=yespress)
            yesbutt.pack(side=LEFT)
                    
            nobutt = Button(areYouSureWindow, text='No', command=nopress)
            nobutt.pack(side=RIGHT)

    path2Dir = filedialog.askdirectory()
    projectWindow = Toplevel()
    projectWindow.geometry("410x315")
    projectWindow.resizable(width=False, height=False)
    projectWindow.title(path2Dir)

    openMaindotPyButt = Button(projectWindow, text="Open main.py", command=openMaindotPy)
    openMaindotPyButt.pack()

    emptySpace = Label(projectWindow, text="")
    emptySpace.pack()
    emptySpace = Label(projectWindow, text="")
    emptySpace.pack()
    emptySpace = Label(projectWindow, text="")
    emptySpace.pack()

    newFileInProjectButt = Button(projectWindow, text="New file", command=newFile)
    newFileInProjectButt.pack()
    
    openFileInProjectButt = Button(projectWindow, text="Open file", command=openFile)
    openFileInProjectButt.pack()

    deleteFileInProjectButt = Button(projectWindow, text="Delete file", command=deleteFile)
    deleteFileInProjectButt.pack()

    exitButt = Button(projectWindow, text="Exit", command=closeProject)
    exitButt.pack(side=BOTTOM)

if __name__ == "__main__":
    root = Tk()
    openProject(root)
    root.mainloop()