from tkinter import *
from tkinter import ttk
from tkinter import filedialog

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

if __name__ == "__main__":
    root = Tk()
    openFile(root)
    root.mainloop()