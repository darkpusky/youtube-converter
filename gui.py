from youtube import Song 
from tkinter import *
from tkinter import ttk
import guifunctions as gfunc

### OPTIONS ###
MWW = 500 #Main window width
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
mainframe = ttk.Frame(window)
mainframe.grid(column=0,row=0,sticky=(N, W, E, S),padx=5,pady=5)
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(list(range(5)),weight=1)
#TODO style


############ SECTIONS ############

### Theme & Language ###
frm_Head = ttk.Frame(mainframe,borderwidth=1)#Row Frame Theme
frm_Head.grid(row=0,column=0,sticky=(N, W, E, S))#Positioning Row Frame Theme
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
italy = PhotoImage(file = r"C:\Users\valet\Desktop\youtube_converter\youtube-converter\utils\italy2.png")
uk = PhotoImage(file = r"C:\Users\valet\Desktop\youtube_converter\youtube-converter\utils\uk2.png")
btn_Head_Lang_It = gfunc.createDefaultLangButton(frm_Head_Langs,italy)
btn_Head_Lang_En = gfunc.createDefaultLangButton(frm_Head_Langs,uk)
btn_Head_Lang_It.configure(command=lambda:gfunc.handleChangeLangToIT())
btn_Head_Lang_En.configure(command=lambda:gfunc.handleChangeLangToUK())
btn_Head_Lang_It.grid(row=0,column=0,sticky=(N,E),padx=2)
btn_Head_Lang_En.grid(row=0,column=1,sticky=(N,E))

### Frames ###
frm_DownloadPath = ttk.Frame(master=mainframe,borderwidth=1)
frm_Download = ttk.Frame(master=mainframe,borderwidth=1)
frm_Queue = ttk.Frame(master=mainframe,borderwidth=1)
frm_Footer = ttk.Frame(master=mainframe,borderwidth=1)

### Labels ###

lbl_DownoadPath = ttk.Label(master=frm_DownloadPath,text="DownloadPath")
lbl_Download = ttk.Label(master=frm_Download,text="Download")
lbl_Queue = ttk.Label(master=frm_Queue,text="Queue")
lbl_Footer = ttk.Label(master=frm_Footer,text="Footer")

### Grid frames ###

frm_DownloadPath.grid(row=1,column=0,sticky=(N, W, E, S))
lbl_DownoadPath.pack()
frm_Download.grid(row=2,column=0,sticky=(N, W, E, S))
lbl_Download.pack()
frm_Queue.grid(row=3,column=0,sticky=(N, W, E, S))
lbl_Queue.pack()
frm_Footer.grid(row=4,column=0,sticky=(N, W, E, S))
lbl_Footer.pack()

window.mainloop()

