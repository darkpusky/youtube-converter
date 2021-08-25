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
download = Download(downloadPath.txt_DownloadPath)

####### Queue #######
frm_Queue_Container = Frame(mainframe,borderwidth=1,highlightbackground="red",highlightcolor="red",highlightthickness=2)
frm_Queue_Container.grid(row=10,column=0,sticky=(N, W, E, S),rowspan=10)
frm_Queue_Container.columnconfigure(list(range(11)),weight=1)
frm_Queue_Container.rowconfigure(0,weight=1)
canvas_Queue = Canvas(frm_Queue_Container)

scrl_Queue = ttk.Scrollbar(frm_Queue_Container,orient=VERTICAL,command=canvas_Queue.yview)
frm_Queue = ttk.Frame(canvas_Queue,width=200)
lbl_Image = ttk.Label(frm_Queue,text="Image")
lbl_Image.pack()

##canvas_Queue.bind("<MouseWheel>",lambda e:
##                 canvas_Queue.yview_scroll(int(-1*(e.delta/120)),"units")
##                )
canvas_Queue.create_window((0,0),window=frm_Queue,anchor="nw")
canvas_Queue.configure(yscrollcommand=scrl_Queue.set)
canvas_Queue.grid(row=0,column=0,columnspan=10,sticky=(N,W,S,E))
scrl_Queue.grid(row=0,column=10,sticky=(N,E,S),padx=(10,0))

def configure(event):
    canvas_Queue.configure(scrollregion = canvas_Queue.bbox("all"))
    frm_Queue.configure(width=200)
    frm_Object.configure(width=canvas_Queue.winfo_width())
    print(" & " + str(frm_Object.winfo_width()))
    

###TEST####
frm_Object = Frame(frm_Queue,borderwidth=1,highlightbackground="red",highlightcolor="red",highlightthickness=2)
frm_Object.rowconfigure(0,weight=1)
frm_Object.columnconfigure(list(range(7)),weight=1)


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

canvas_Queue.bind("<Configure>",configure)
###########

#Download viene fatto partire dopo perchè serve il frame di Queue
download.start(mainframe,mainframe)

### Frames ###
frm_Footer = ttk.Frame(master=mainframe,borderwidth=1)

### Labels ###
lbl_Footer = ttk.Label(master=frm_Footer,text="Footer")

### Grid frames ###
frm_Footer.grid(row=22,column=0,sticky=(N, W, E, S))
lbl_Footer.pack()

window.mainloop()

