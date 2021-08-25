from tkinter import *
from tkinter import ttk
import guifunctions as gfunc

class Head:
    #def __init__(self):
        #self.italy = PhotoImage(file = r"C:\Users\valet\Desktop\youtube_converter\youtube-converter\utils\italy2.png")
        #self.uk = PhotoImage(file = r"C:\Users\valet\Desktop\youtube_converter\youtube-converter\utils\uk2.png")
        #TODO get dir from costants
        
    def start(self,mainframe):
        frm_Head = ttk.Frame(mainframe,borderwidth=1)#Row Frame Theme
        frm_Head.grid(row=0,column=0,sticky=(N, W, E, S))#Positioning Row
        frm_Head.columnconfigure(list(range(3)),weight=1)
        frm_Head.rowconfigure(0,weight=1)
        
        #Theme & Language ha una griglia di 1X3
        #1X1 ha i temi da scegliere, due bottoni
        #1x2 cella di passaggio
        #1x3 ha le lingue da scegliere, due bottoni separati
        
        ### Griglia ###
        frm_Head_Themes = ttk.Frame(frm_Head)
        frm_Head_Langs = ttk.Frame(frm_Head)
        frm_Head_Themes.grid(row=0,column=0,sticky=(N,W))
        frm_Head_Langs.grid(row=0,column=2,sticky=(N,E))

        ### Theme buttons ###
        btn_Head_Theme_Light = gfunc.createDefaultThemeButton(frm_Head_Themes,"Light")
        btn_Head_Theme_Dark = gfunc.createDefaultThemeButton(frm_Head_Themes,"Dark")
        btn_Head_Theme_Light.configure(relief="sunken",command=lambda:gfunc.handleChangeThemeToLight(btn_Head_Theme_Light,btn_Head_Theme_Dark))
        btn_Head_Theme_Dark.configure(command=lambda:gfunc.handleChangeThemeToDark(btn_Head_Theme_Light,btn_Head_Theme_Dark))
        btn_Head_Theme_Light.grid(row=0,column=0,sticky=(N,W))
        btn_Head_Theme_Dark.grid(row=0,column=1,sticky=(N,W))
        #TODO style of the buttons

        ### Language buttons ###
        btn_Head_Lang_It = gfunc.createDefaultLangButton(frm_Head_Langs,"")
        btn_Head_Lang_En = gfunc.createDefaultLangButton(frm_Head_Langs,"")
        btn_Head_Lang_It.configure(command=lambda:gfunc.handleChangeLangToIT())
        btn_Head_Lang_En.configure(command=lambda:gfunc.handleChangeLangToUK())
        btn_Head_Lang_It.grid(row=0,column=0,sticky=(N,E),padx=2)
        btn_Head_Lang_En.grid(row=0,column=1,sticky=(N,E))
