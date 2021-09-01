from tkinter import *
from tkinter import ttk
import guifunctions as gfunc

class Theme():

    def __init__():
        style = ttk.Style()
        style.theme_use('alt')
        window.configure(bg='white') #Window
        general_font = ('Courier New Baltic', 10)
        window.option_add("*Font", general_font) #Font
        style.configure('TFrame',background='white') #Frames
        style.configure('TLabel',background='white') #Labels

    
