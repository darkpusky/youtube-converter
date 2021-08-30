from tkinter import *
from tkinter import ttk
import guifunctions as gfunc
from downloadpath import DownloadPath
from head import Head
from download import Download
from queues import Queues
from footer import Footer


### OPTIONS ###
MWW = 800 #Main window width
MWH = 650 #Main window height

### Create Main Window ###
window = Tk()
#window.withdraw()
window.title("Youtube Converter")
window.minsize(MWW,MWH)
window.maxsize(1920,1080)
window.geometry('800x650' + gfunc.centerMainWindow(window,MWW,MWH))
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
download = Download(downloadPath.txt_DownloadPath)

####### Queue #######
queue = Queues()
queue.start(mainframe)

#Download viene fatto partire dopo perchè serve il frame di Queue
download.start(mainframe,queue.frm_Queue,window)

####### Footer #######
footer = Footer()
footer.start(mainframe)

window.mainloop()

