from tkinter import *
from tkinter import ttk
import guifunctions as gfunc

class DownloadPath:

    def __init__(self):
        self.image = PhotoImage(file = r"C:\Users\valet\Desktop\youtube_converter\youtube-converter\utils\openfile-1.png")
        #TODO get dir from costants
        
    def start(self,mainframe):
        frm_DownloadPath = ttk.Frame(mainframe)
        frm_DownloadPath.grid(row=1,column=0,sticky=(N, W, E, S))
        frm_DownloadPath.columnconfigure(list(range(3)),weight=1)
        frm_DownloadPath.rowconfigure(0,weight=1)
        frm_DownloadPath_Content = ttk.Frame(frm_DownloadPath)
        frm_DownloadPath_Content.grid(row=0,column=1)
        lbl_DownoadPath = ttk.Label(frm_DownloadPath_Content,text="Cartella di destinazione"+":")
        txt_DownloadPath = ttk.Entry(frm_DownloadPath_Content,width=60,exportselection=0)
        btn_DownloadPath = gfunc.createDefaultOpendDirButton(frm_DownloadPath_Content,self.image)
        btn_DownloadPath.configure(command=lambda:gfunc.getDirectory(txt_DownloadPath))
        lbl_DownoadPath.grid(row=0,column=0)
        txt_DownloadPath.grid(row=0,column=1)
        btn_DownloadPath.grid(row=0,column=2,padx=2)
