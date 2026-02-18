from tkinter import *
import os
import sys

def get_terminal():
    shell_pid = os.getppid()
    with open(f"/proc/{shell_pid}/status", "r") as f:
        for line in f:
            if line.startswith("PPid:"):
                term_pid = line.split()[1]
                break
    with open(f"/proc/{term_pid}/comm", "r") as f:
        return f.read().strip()

term = get_terminal()
print('Terminal ' + term)

main = Tk()
main.geometry("330x350")
main.title("Pymaneg")
main.resizable(width=False, height=False)

os.system('mkdir ~/PythonFiles')
os.system('mkdir ~/PythonProjects')

def openfilewin():

    def openfile():
         os.system('exec ' + term + ' nvim ~/PythonFiles/' + openfnamespace.get() + ".py")
         openfilewindow.destroy()
    

    openfilewindow = Tk()

    openfilewindow.geometry("390x130")
    openfilewindow.resizable(width=False, height=False)
    openfilewindow.title("Open file")

    enterofnametxt = Label(openfilewindow, text="Enter file name:")
    enterofnametxt.pack(side="left")

    openfnamespace = Entry(openfilewindow)
    openfnamespace.pack(side="left")

    openbutt = Button(openfilewindow, text="Open", command=openfile)
    openbutt.pack(side="left")

    openfilewindow.mainloop()
def newfilewin():
    def newfile():
        os.system('touch ~/PythonFiles/' + newfnamespace.get() + '.py')
        newfilewindow.destroy()
    
    newfilewindow = Tk()
    newfilewindow.geometry("390x130")
    newfilewindow.resizable(width=False, height=False)
    newfilewindow.title("New file")

    enternfnametxt = Label(newfilewindow, text="Enter file name:")
    enternfnametxt.pack(side="left")

    newfnamespace = Entry(newfilewindow)
    newfnamespace.pack(side="left")

    createbutt = Button(newfilewindow, text="Create", command=newfile)
    createbutt.pack(side="left")

    newfilewindow.mainloop()

def delfilewin():

    def delfile():
        
        def yespress():
            os.system('rm -rf ~/PythonFiles/' + delfnamespace.get() + '.py')
            delfilewindow.destroy()
            areusurewin.destroy()

        def nopress():
            delfilewindow.destroy()
            areusurewin.destroy()

        areusurewin = Tk()
        areusurewin.geometry("230x165")
        areusurewin.resizable(width=False, height=False)
        areusurewin.title("Sure?")

        quest = Label(areusurewin, text='Are you sure?')
        quest.pack()

        yesbutt = Button(areusurewin, text="Yes", command=yespress)
        yesbutt.pack(side='left')

        nobutt = Button(areusurewin, text='No', command=nopress)
        nobutt.pack(side='right')
        
    delfilewindow = Tk()
    delfilewindow.geometry("390x130")
    delfilewindow.resizable(width=False, height=False)
    delfilewindow.title("Delete file")

    enternfnametxt = Label(delfilewindow, text="Enter file name:")
    enternfnametxt.pack(side="left")

    delfnamespace = Entry(delfilewindow)
    delfnamespace.pack(side="left")

    delbutt = Button(delfilewindow, text="Delete", command=delfile)
    delbutt.pack(side="left")

    delfilewindow.mainloop()

def renamewin():

    def rename():
        os.system('mv ~/PythonFiles/' + oldfilenamespace.get() + '.py' + " ~/PythonFiles/" + newnamefilespace.get() + ".py")
        renamewindow.destroy()

    renamewindow = Tk()
    renamewindow.geometry('285x290')
    renamewindow.resizable(width=False, height=False)
    renamewindow.title('Rename file')

    oldfilenametxt = Label(renamewindow, text='Old name file:')
    oldfilenametxt.pack()

    oldfilenamespace = Entry(renamewindow)
    oldfilenamespace.pack()

    newfilenametxt = Label(renamewindow, text="New name file:")
    newfilenametxt.pack()

    newnamefilespace = Entry(renamewindow)
    newnamefilespace.pack()

    renamefilebutt = Button(renamewindow, text='Rename', command=rename)
    renamefilebutt.pack(side='bottom')

    renamewindow.mainloop()

def exitfromapp():
    sys.exit()

def launchfilewin():

    def launchfile():
        os.system('exec ' + term + ' python ~/PythonFiles/' + laucnhfnamespace.get() + '.py')
    
    launchfilewindow = Tk()
    launchfilewindow.geometry("390x130")
    launchfilewindow.resizable(width=False, height=False)
    launchfilewindow.title("Laucnh file")

    enterlfnametxt = Label(launchfilewindow, text="Enter file name:")
    enterlfnametxt.pack(side="left")

    laucnhfnamespace = Entry(launchfilewindow)
    laucnhfnamespace.pack(side="left")

    launchbutt = Button(launchfilewindow, text="Launch", command=launchfile)
    launchbutt.pack(side="left")

    launchfilewindow.mainloop()

def openprojectwin():

    def openprj():

        def openmainpy():
            os.system('exec ' + term + ' nvim ~/PythonProjects/' + openpnamespace.get() + '/main.py')
            
        def exitprj():
            openprjwindow.destroy()
            prjwindow.destroy()
        
        def newfileinprj():

            def newfileprj():
                os.system('touch ~/PythonProjects/' + openpnamespace.get() + '/' + newfipnamespace.get() + '.py')
                newfileinprjwindow.destroy()

            newfileinprjwindow = Tk()
            newfileinprjwindow.geometry("390x130")
            newfileinprjwindow.resizable(width=False, height=False)
            newfileinprjwindow.title("New file")

            enternfipnametxt = Label(newfileinprjwindow, text="Enter file name:")
            enternfipnametxt.pack(side="left")

            newfipnamespace = Entry(newfileinprjwindow)
            newfipnamespace.pack(side="left")

            createbutt = Button(newfileinprjwindow, text="Create", command=newfileprj)
            createbutt.pack(side="left")

            newfileinprjwindow.mainloop()

        def openfileinprj():

            def openfileip():
                os.system('exec ' + term + ' nvim ~/PythonProjects/' + openpnamespace.get() + '/' + openfipnamespace.get() + '.py')
                openfileinprjwindow.destroy()

            openfileinprjwindow = Tk()

            openfileinprjwindow.geometry("390x130")
            openfileinprjwindow.resizable(width=False, height=False)
            openfileinprjwindow.title("Open file")

            enterofipnametxt = Label(openfileinprjwindow, text="Enter file name:")
            enterofipnametxt.pack(side="left")

            openfipnamespace = Entry(openfileinprjwindow)
            openfipnamespace.pack(side="left")

            openfipbutt = Button(openfileinprjwindow, text="Open", command=openfileip)
            openfipbutt.pack(side="left")

            openfileinprjwindow.mainloop()

        prjwindow = Tk()

        prjwindow.geometry("410x315")
        prjwindow.resizable(width=False, height=False)
        prjwindow.title(openpnamespace.get())

        openmpyButt = Button(prjwindow, text='Open main.py', command=openmainpy)
        openmpyButt.pack()

        newfButt = Button(prjwindow, text='New file', command=newfileinprj)
        newfButt.pack() 

        openfButt = Button(prjwindow, text='Open file', command=openfileinprj)
        openfButt.pack() 

        exitButt = Button(prjwindow, text='Exit', command=exitprj)
        exitButt.pack(side='bottom')

        prjwindow.mainloop()

    openprjwindow = Tk()
    openprjwindow.geometry("390x130")
    openprjwindow.resizable(width=False, height=False)
    openprjwindow.title("Open project")

    enteropnametxt = Label(openprjwindow, text="Enter project name:")
    enteropnametxt.pack(side="left")

    openpnamespace = Entry(openprjwindow)
    openpnamespace.pack(side="left")

    openbutt = Button(openprjwindow, text="Open", command=openprj)
    openbutt.pack(side="left")

    openprjwindow.mainloop()
def newprojectwin():

    def newprj():
        os.system('mkdir ~/PythonProjects/' + newpnamespace.get())
        os.system('touch ~/PythonProjects/' + newpnamespace.get() + '/main.py')
        os.system('python -m venv ~/PythonProjects/' + newpnamespace.get() + '/venv/')
        newprjwindow.destroy()
        
    newprjwindow = Tk()
    newprjwindow.geometry("390x130")
    newprjwindow.resizable(width=False, height=False)
    newprjwindow.title("New project")

    enternpnametxt = Label(newprjwindow, text="Enter project name:")
    enternpnametxt.pack(side="left")

    newpnamespace = Entry(newprjwindow)
    newpnamespace.pack(side="left")

    newprjbutt = Button(newprjwindow, text="Create", command=newprj)
    newprjbutt.pack(side="left")

welcometxt = Label(text="Welcome!")
welcometxt.pack()

openfilebutt = Button(main, text="Open file", command=openfilewin)
openfilebutt.pack()

newfilebutt = Button(main, text="New file", command=newfilewin)
newfilebutt.pack()

openprojectbutt = Button(main, text="Open project", command=openprojectwin)
openprojectbutt.pack()

newprojectbutt = Button(main, text="New project", command=newprojectwin)
newprojectbutt.pack()

launchfilebutt = Button(main, text="Launch file", command=launchfilewin)
launchfilebutt.pack()

renamefilebutt = Button(main, text="Rename file", command=renamewin)
renamefilebutt.pack()

delfilebutt = Button(main, text="Delete file", command=delfilewin)
delfilebutt.pack()

exitbutt = Button(main, text="Exit", command=exitfromapp)
exitbutt.pack(side="bottom")

main.mainloop()
