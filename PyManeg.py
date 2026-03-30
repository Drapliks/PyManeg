from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import sys

root = Tk()
root.geometry("330x450")
root.title("Pysapce")
root.resizable(width=False, height=False)

os.makedirs(os.path.expanduser('~/PythonFiles'), exist_ok=True)
os.makedirs(os.path.expanduser('~/PythonProjects'), exist_ok=True)

def show_error(message):
    error_win = Toplevel()
    error_win.geometry("300x100")
    error_win.resizable(width=False, height=False)
    error_win.title("Error")
    
    error_label = Label(error_win, text=message)
    error_label.pack(pady=20)
    
    ok_button = Button(error_win, text="OK", command=error_win.destroy)
    ok_button.pack()

def check_file_exists(filename, should_exist=True):
    filepath = os.path.expanduser(f'~/PythonFiles/{filename}.py')
    exists = os.path.isfile(filepath)
    
    if should_exist and not exists:
        show_error(f"File '{filename}.py' does not exist!")
        return False
    elif not should_exist and exists:
        show_error(f"File '{filename}.py' already exists!")
        return False
    return True

def check_project_exists(projectname, should_exist=True):
    projectpath = os.path.expanduser(f'~/PythonProjects/{projectname}')
    exists = os.path.isdir(projectpath)
    
    if should_exist and not exists:
        show_error(f"Project '{projectname}' does not exist!")
        return False
    elif not should_exist and exists:
        show_error(f"Project '{projectname}' already exists!")
        return False
    return True

def openfilewin():
    File2open = filedialog.askopenfilename()

    def saveFile():
        if File2open != "":
            text = codeEditor.get("1.0", END)
            with open(File2open, "w") as file:
                file.write(text)

    codeSpace = Toplevel()
    codeSpace.title(File2open)

    codeEditor = Text(codeSpace)
    codeEditor.pack()

    savefilebutt = Button(codeSpace, text="Save file", command=saveFile)
    savefilebutt.pack(side=LEFT)

    if File2open != "":
        with open(File2open, "r") as file:
            text =file.read()
            codeEditor.delete("1.0", END)
            codeEditor.insert("1.0", text)

def newfilewin():
    def newfile():
        filename = newfnamespace.get().strip()
        if not filename:
            show_error("Please enter a file name!")
            return
        if check_file_exists(filename, should_exist=False):
            os.system(f'touch ~/PythonFiles/{filename}.py')
            newfilewindow.destroy()
    
    newfilewindow = Toplevel()
    newfilewindow.geometry("390x130")
    newfilewindow.resizable(width=False, height=False)
    newfilewindow.title("New file")
    
    enternfnametxt = Label(newfilewindow, text="Enter file name:")
    enternfnametxt.pack(side="left")
    
    newfnamespace = Entry(newfilewindow)
    newfnamespace.pack(side="left")
    
    createbutt = Button(newfilewindow, text="Create", command=newfile)
    createbutt.pack(side="left")

def delfilewin():
    def confirm_delete():
        filename = delfnamespace.get().strip()
        if not filename:
            show_error("Please enter a file name!")
            return
        if check_file_exists(filename, should_exist=True):
            delfilewindow.destroy()
            
            def yespress():
                os.system(f'rm -f ~/PythonFiles/{filename}.py')
                areusurewin.destroy()
            
            def nopress():
                areusurewin.destroy()
            
            areusurewin = Toplevel()
            areusurewin.geometry("230x165")
            areusurewin.resizable(width=False, height=False)
            areusurewin.title("Are you sure?")
            
            quest = Label(areusurewin, text=f'Delete file {filename}.py?')
            quest.pack()
            
            yesbutt = Button(areusurewin, text="Yes", command=yespress)
            yesbutt.pack(side='left')
            
            nobutt = Button(areusurewin, text='No', command=nopress)
            nobutt.pack(side='right')
    
    delfilewindow = Toplevel()
    delfilewindow.geometry("390x130")
    delfilewindow.resizable(width=False, height=False)
    delfilewindow.title("Delete file")
    
    enternfnametxt = Label(delfilewindow, text="Enter file name:")
    enternfnametxt.pack(side="left")
    
    delfnamespace = Entry(delfilewindow)
    delfnamespace.pack(side="left")
    
    delbutt = Button(delfilewindow, text="Delete", command=confirm_delete)
    delbutt.pack(side="left")

def renamewin():
    def rename():
        oldname = oldfilenamespace.get().strip()
        newname = newnamefilespace.get().strip()
        
        if not oldname or not newname:
            show_error("Please enter both file names!")
            return
        
        if not check_file_exists(oldname, should_exist=True):
            return
        
        if not check_file_exists(newname, should_exist=False):
            return
        
        os.system(f'mv ~/PythonFiles/{oldname}.py ~/PythonFiles/{newname}.py')
        renamewindow.destroy()
    
    renamewindow = Toplevel()
    renamewindow.geometry('285x290')
    renamewindow.resizable(width=False, height=False)
    renamewindow.title('Rename file')
    
    oldfilenametxt = Label(renamewindow, text='Old file name:')
    oldfilenametxt.pack()
    
    oldfilenamespace = Entry(renamewindow)
    oldfilenamespace.pack()
    
    newfilenametxt = Label(renamewindow, text="New file name:")
    newfilenametxt.pack()
    
    newnamefilespace = Entry(renamewindow)
    newnamefilespace.pack()
    
    renamefilebutt = Button(renamewindow, text='Rename', command=rename)
    renamefilebutt.pack(side='bottom')

def exitfromapp():
    sys.exit()

def launchfilewin():
    def launchfile():
        filename = laucnhfnamespace.get().strip()
        if not filename:
            show_error("Please enter a file name!")
            return
        if check_file_exists(filename, should_exist=True):
            os.system(f'exec kitty python ~/PythonFiles/{filename}.py')
    
    launchfilewindow = Toplevel()
    launchfilewindow.geometry("390x130")
    launchfilewindow.resizable(width=False, height=False)
    launchfilewindow.title("Launch file")
    
    enterlfnametxt = Label(launchfilewindow, text="Enter file name:")
    enterlfnametxt.pack(side="left")
    
    laucnhfnamespace = Entry(launchfilewindow)
    laucnhfnamespace.pack(side="left")
    
    launchbutt = Button(launchfilewindow, text="Launch", command=launchfile)
    launchbutt.pack(side="left")

def openprojectwin():
    def openprj():
        projectname = openpnamespace.get().strip()
        if not projectname:
            show_error("Please enter a project name!")
            return
        if check_project_exists(projectname, should_exist=True):
            openprjwindow.destroy()
            
            def openmainpy():
                os.system(f'exec kitty nvim ~/PythonProjects/{projectname}/main.py')
            
            def exitprj():
                prjwindow.destroy()
            
            def newfileinprj():
                def newfileprj():
                    filename = newfipnamespace.get().strip()
                    if not filename:
                        show_error("Please enter a file name!")
                        return
                    
                    filepath = os.path.expanduser(f'~/PythonProjects/{projectname}/{filename}.py')
                    if os.path.isfile(filepath):
                        show_error(f"File '{filename}.py' already exists in project!")
                        return
                    
                    os.system(f'touch ~/PythonProjects/{projectname}/{filename}.py')
                    newfileinprjwindow.destroy()
                
                newfileinprjwindow = Toplevel()
                newfileinprjwindow.geometry("390x130")
                newfileinprjwindow.resizable(width=False, height=False)
                newfileinprjwindow.title("New file in project")
                
                enternfipnametxt = Label(newfileinprjwindow, text="Enter file name:")
                enternfipnametxt.pack(side="left")
                
                newfipnamespace = Entry(newfileinprjwindow)
                newfipnamespace.pack(side="left")
                
                createbutt = Button(newfileinprjwindow, text="Create", command=newfileprj)
                createbutt.pack(side="left")
            
            def openfileinprj():
                def openfileip():
                    filename = openfipnamespace.get().strip()
                    if not filename:
                        show_error("Please enter a file name!")
                        return
                    
                    filepath = os.path.expanduser(f'~/PythonProjects/{projectname}/{filename}.py')
                    if not os.path.isfile(filepath):
                        show_error(f"File '{filename}.py' does not exist in project!")
                        return
                    
                    os.system(f'exec kitty nvim ~/PythonProjects/{projectname}/{filename}.py')
                    openfileinprjwindow.destroy()
                
                openfileinprjwindow = Toplevel()
                openfileinprjwindow.geometry("390x130")
                openfileinprjwindow.resizable(width=False, height=False)
                openfileinprjwindow.title("Open file in project")
                
                enterofipnametxt = Label(openfileinprjwindow, text="Enter file name:")
                enterofipnametxt.pack(side="left")
                
                openfipnamespace = Entry(openfileinprjwindow)
                openfipnamespace.pack(side="left")
                
                openfipbutt = Button(openfileinprjwindow, text="Open", command=openfileip)
                openfipbutt.pack(side="left")
            
            prjwindow = Toplevel()
            prjwindow.geometry("410x315")
            prjwindow.resizable(width=False, height=False)
            prjwindow.title(projectname)
            
            openmpyButt = Button(prjwindow, text='Open main.py', command=openmainpy)
            openmpyButt.pack()
            
            newfButt = Button(prjwindow, text='New file', command=newfileinprj)
            newfButt.pack()
            
            openfButt = Button(prjwindow, text='Open file', command=openfileinprj)
            openfButt.pack()
            
            exitButt = Button(prjwindow, text='Exit', command=exitprj)
            exitButt.pack(side='bottom')
    
    openprjwindow = Toplevel()
    openprjwindow.geometry("390x130")
    openprjwindow.resizable(width=False, height=False)
    openprjwindow.title("Open project")
    
    enteropnametxt = Label(openprjwindow, text="Enter project name:")
    enteropnametxt.pack(side="left")
    
    openpnamespace = Entry(openprjwindow)
    openpnamespace.pack(side="left")
    
    openbutt = Button(openprjwindow, text="Open", command=openprj)
    openbutt.pack(side="left")

def newprojectwin():
    def newprj():
        projectname = newpnamespace.get().strip()
        if not projectname:
            show_error("Please enter a project name!")
            return
        
        if check_project_exists(projectname, should_exist=False):
            os.system(f'mkdir -p ~/PythonProjects/{projectname}')
            os.system(f'touch ~/PythonProjects/{projectname}/main.py')
            os.system(f'python -m venv ~/PythonProjects/{projectname}/venv/')
            newprjwindow.destroy()
    
    newprjwindow = Toplevel()
    newprjwindow.geometry("390x130")
    newprjwindow.resizable(width=False, height=False)
    newprjwindow.title("New project")
    
    enternpnametxt = Label(newprjwindow, text="Enter project name:")
    enternpnametxt.pack(side="left")
    
    newpnamespace = Entry(newprjwindow)
    newpnamespace.pack(side="left")
    
    newprjbutt = Button(newprjwindow, text="Create", command=newprj)
    newprjbutt.pack(side="left")

def delprojectwin():
    def confirm_delete():
        projectname = delpnamespace.get().strip()
        if not projectname:
            show_error("Please enter a project name!")
            return
        
        if check_project_exists(projectname, should_exist=True):
            delfilewindow.destroy()
            
            def yespress():
                os.system(f'rm -rf ~/PythonProjects/{projectname}')
                areusurewin.destroy()
            
            def nopress():
                areusurewin.destroy()
            
            areusurewin = Toplevel()
            areusurewin.geometry("230x165")
            areusurewin.resizable(width=False, height=False)
            areusurewin.title("Are you sure?")
            
            quest = Label(areusurewin, text=f'Delete project {projectname}?')
            quest.pack()
            
            yesbutt = Button(areusurewin, text="Yes", command=yespress)
            yesbutt.pack(side='left')
            
            nobutt = Button(areusurewin, text='No', command=nopress)
            nobutt.pack(side='right')
    
    delfilewindow = Toplevel()
    delfilewindow.geometry("390x130")
    delfilewindow.resizable(width=False, height=False)
    delfilewindow.title("Delete project")
    
    enternfnametxt = Label(delfilewindow, text="Enter project name:")
    enternfnametxt.pack(side="left")
    
    delpnamespace = Entry(delfilewindow)
    delpnamespace.pack(side="left")
    
    delbutt = Button(delfilewindow, text="Delete", command=confirm_delete)
    delbutt.pack(side="left")

welcometxt = Label(root, text="Welcome!")
welcometxt.pack()

empty = Label(root, text="")
empty.pack()

filestxt = Label(root, text="----Files----")
filestxt.pack()

openfilebutt = Button(root, text="Open file", command=openfilewin)
openfilebutt.pack()

newfilebutt = Button(root, text="New file", command=newfilewin)
newfilebutt.pack()

launchfilebutt = Button(root, text="Launch file", command=launchfilewin)
launchfilebutt.pack()

renamefilebutt = Button(root, text="Rename file", command=renamewin)
renamefilebutt.pack()

delfilebutt = Button(root, text="Delete file", command=delfilewin)
delfilebutt.pack()

parter = Label(root, text="------------")
parter.pack()

empty2 = Label(root, text="")
empty2.pack()

projectstxt = Label(root, text="----Projects----")
projectstxt.pack()

openprojectbutt = Button(root, text="Open project", command=openprojectwin)
openprojectbutt.pack()

newprojectbutt = Button(root, text="New project", command=newprojectwin)
newprojectbutt.pack()

delprojectbutt = Button(root, text="Delete project", command=delprojectwin)
delprojectbutt.pack()

parter2 = Label(root, text="------------")
parter2.pack()

exitbutt = Button(root, text="Exit", command=exitfromapp)
exitbutt.pack(side="bottom")

root.mainloop()

