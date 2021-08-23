from tkinter import *
from tkinter import ttk
from tkinter import filedialog

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
    return Button(parent,borderwidth=0,cursor="hand2",image=image,relief="flat")

### Handle commands for language buttons ###
def handleChangeLangToIT():
    #TODO implement chenage of the language
    return

def handleChangeLangToUK():
    #TODO implement chenage of the language
    return

### Handle creation for directory button ###
def createDefaultOpendDirButton(parent,image):
    return Button(parent,borderwidth=1,cursor="hand2",image=image,height=18)

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
    #TODO
    return
