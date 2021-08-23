from youtube import Song
from tkinter import *
from tkinter import ttk
import guifunctions as gfunc
from downloadpath import DownloadPath
from head import Head
from download import Download

### OPTIONS ###
MWW = 800 #Main window width
MWH = 600 #Main window height

### Create Main Window ###
window = Tk()
window.title("Youtube Converter")
window.minsize(MWW,MWH)
window.maxsize(1920,1080)
window.geometry('500x600' + gfunc.centerMainWindow(window,MWW,MWH))
window.columnconfigure(0,weight=1)
window.rowconfigure(0,weight=1)

### Main frame ###
mainframe = ttk.Frame(window,borderwidth=2)
mainframe.grid(column=0,row=0,sticky=(N, W, E, S),padx=5,pady=5)
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(list(range(25)),weight=1)
#TODO style


############ SECTIONS ############

####### Theme & Language #######
head = Head()
head.start(mainframe)

####### Download path #######
downloadPath = DownloadPath()
downloadPath.start(mainframe)

####### Download #######
download = Download()
download.start(mainframe)

####### Queue #######
frm_Queue = Frame(mainframe,borderwidth=1,highlightbackground="red",highlightcolor="red",highlightthickness=2)
frm_Queue.grid(row=8,column=0,sticky=(N, W, E, S),rowspan=14)
lbl_Queue = ttk.Label(frm_Queue,text="Queue")
lbl_Queue.pack()

### Frames ###


frm_Footer = ttk.Frame(master=mainframe,borderwidth=1)

### Labels ###



lbl_Footer = ttk.Label(master=frm_Footer,text="Footer")


### Grid frames ###





frm_Footer.grid(row=22,column=0,sticky=(N, W, E, S))
lbl_Footer.pack()

window.mainloop()

