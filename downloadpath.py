from tkinter import *
from tkinter import ttk
import guifunctions as gfunc
from lang import getLabelIt,getLabelEn

class DownloadPath:

    def __init__(self):
        self.image = PhotoImage(file = r".\utils\openfile-1.png")
        #TODO get dir from costants
        
    def start(self,mainframe):
        frm_DownloadPath = ttk.Frame(mainframe)
        frm_DownloadPath.grid(row=1,column=0,sticky=(N, W, E, S))
        frm_DownloadPath.columnconfigure(list(range(3)),weight=1)
        frm_DownloadPath.rowconfigure(0,weight=1)
        frm_DownloadPath_Content = ttk.Frame(frm_DownloadPath)
        frm_DownloadPath_Content.grid(row=0,column=1)
        self.lbl_DownoadPath = ttk.Label(frm_DownloadPath_Content)
        self.txt_DownloadPath = Entry(frm_DownloadPath_Content,width=60,exportselection=0,highlightthickness=2,highlightbackground="red",highlightcolor= "red",insertbackground="red")
        ##MOCK##
        self.txt_DownloadPath.insert(0,"C:/Users/valet/Downloads/Youtube")
        ##MOCK##
        self.btn_DownloadPath = gfunc.createDefaultOpendDirButton(frm_DownloadPath_Content,self.image)
        self.btn_DownloadPath.configure(command=lambda:gfunc.getDirectory(self.txt_DownloadPath))
        self.lbl_DownoadPath.grid(row=0,column=0)
        self.txt_DownloadPath.grid(row=0,column=1)
        self.btn_DownloadPath.grid(row=0,column=2,padx=2)

    def changeTheme(self,theme):
        if theme == "dark":
            self.btn_DownloadPath.configure(background="#C8C6C6",activebackground="#C8C6C6")
        elif theme == "light":
            self.btn_DownloadPath.configure(background="#FAF3F3",activebackground="#FAF3F3")

    def changeLang(self,lang):
        if lang == "it":
            self.lbl_DownoadPath.configure(text= getLabelIt("dest"))
        elif lang == "en":
            self.lbl_DownoadPath.configure(text= getLabelEn("dest"))
