from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import utils as utils
from tkinter import messagebox

### Initialization of the window in center position ###
def centerMainWindow(window,w,h):
    positionRight = int(window.winfo_screenwidth() / 2 - w/2)
    positionDown = int(window.winfo_screenheight() / 2 - h/2)
    return "+{}+{}".format(positionRight, positionDown)

### Handle creation for theme buttons ###
def createDefaultThemeButton(parent,text):
    return Button(parent,text=text,borderwidth=1,cursor="hand2",highlightthickness=0,width=7,height=2)

### Handle commands for theme buttons ###
def handleChangeThemeToDark(light,dark):
    if dark['relief'] == "raised":
        light.configure(relief="raised")
        dark.configure(relief="sunken")
    #TODO implement change of the style

def handleChangeThemeToLight(light,dark):
    if light['relief'] == "raised":
        light.configure(relief="sunken")
        dark.configure(relief="raised")
    #TODO implement change of the style

### Handle creation for lang buttons ###
def createDefaultLangButton(parent,image):
    return Button(parent,borderwidth=0,cursor="hand2",text=image,relief="flat")

### Handle commands for language buttons ###
def handleChangeLangToIT():
    #TODO implement chenage of the language
    return

def handleChangeLangToUK():
    #TODO implement chenage of the language
    return

### Handle creation for directory button ###
def createDefaultOpendDirButton(parent,image):
    return Button(parent,borderwidth=1,cursor="hand2",text="dir",height=2) #Height=18

### Handle ask directory ###
def getDirectory(entry):
    oldvar = entry.get() #Memorize the old text
    if entry.get() != "":
        entry.delete(0,END) #Delete the old text
    entry.insert(0,filedialog.askdirectory()) #Text from user
    if(entry.get() == ""):
        entry.insert(0,oldvar) #Set old text if user cancel the request

### Handle creation for download button ###
def createDefaultDownloadButton(parent,text):
    return Button(parent,borderwidth=1,cursor="hand2",text=text)

### Validation for directory on click of the download button ###
def validationDownload(directory):
    if directory == "": #Empty directory
        messagebox.showinfo(message="La cartella di destinazione non può essere vuota")
        return False
    if not utils.isExistDir(directory): #Path does not exist
        messagebox.showerror(message="La cartella di destinazione non esiste")
        return False
    if not utils.isDir(directory): #Path is not a directory
        messagebox.showerror(message="La cartella di destinazione non è una cartella valida")
        return False
    return True

### Creation of the frame for queue ###
def createSong(parent,directory):
    if validationDownload(directory):
        frm_Object = ttk.Frame(parent,borderwidth=1,highlightbackground="red",highlightcolor="red",highlightthickness=2)
        frm_Object.rowconfigure(0,weight=1)
        frm_Object.columnconfigure(list(range(7)),weight=1)
        lbl_Image = ttk.Label(frm_Object,text="Image")
        lbl_Name = ttk.Label(frm_Object,text="Name")
        lbl_Duration = ttk.Label(frm_Object,text="Duration")

        lbl_Progress = ttk.Label(frm_Object,text="ProgressBar")
        lbl_Operation = ttk.Label(frm_Object,text="Operation...")
        
        lbl_Image.grid(row=0,column=0)
        lbl_Name.grid(row=0,column=1)
        lbl_Duration.grid(row=0,column=2,columnspan=3)
        lbl_Progress.grid(row=0,column=5)
        lbl_Operation.grid(row=0,column=6)
        frm_Object.grid(row=0,column=0)
        
