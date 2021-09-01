from tkinter import *
from tkinter import ttk
import guifunctions as gfunc

class Theme():

    def __init__(self):
        self.style = ttk.Style()

    def changeToLight(self,window,head,downloadPath,download,queue,footer):
        self.style.theme_use('alt')
        general_font = ('Courier New Baltic', 10)
        window.option_add("*Font", general_font) #Font
        window.tk_setPalette(background="white",foreground='black')
        window.configure(bg='white',) #Window
        self.style.configure('TFrame',background='white') #Frames
        self.style.configure('TLabel',background='white') #Labels
        head.changeTheme("light")
        downloadPath.changeTheme("light")
        download.changeTheme("light")
        queue.changeTheme("light")
        footer.changeTheme("light")

    def changeToDark(self,window,head,downloadPath,download,queue,footer):
        self.style.theme_use('alt')
        general_font = ('Courier New Baltic', 10)
        window.option_add("*Font", general_font) #Font
        window.tk_setPalette(background="#171717",foreground='#FAF3F3')
        window.configure(bg='#171717') #Window
        self.style.configure('TFrame',background='#171717') #Frames
        self.style.configure('TLabel',background='#171717') #Labels
        head.changeTheme("dark")
        downloadPath.changeTheme("dark")
        download.changeTheme("dark")
        queue.changeTheme("dark")
        footer.changeTheme("dark")
