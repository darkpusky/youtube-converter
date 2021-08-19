from tkinter import *

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
