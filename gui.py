from tkinter import *
from tkinter import ttk
import guifunctions as gfunc
from downloadpath import DownloadPath
from head import Head
from download import Download
from queues import Queues
from footer import Footer
from theme import Theme

class Main():

    def __init__(self):
        
        ### OPTIONS ###
        MWW = 800 #Main window width
        MWH = 650 #Main window height
        THEME = "light"

        ### Create Main Window ###
        self.window = Tk()
        #window.withdraw()
        self.window.title("Youtube Converter")
        self.window.minsize(MWW,MWH)
        self.window.maxsize(1920,1080)
        self.window.geometry('800x650' + gfunc.centerMainWindow(self.window,MWW,MWH))
        self.window.columnconfigure(0,weight=1)
        self.window.rowconfigure(0,weight=1)

        ### Main frame ###
        mainframe = ttk.Frame(self.window)
        mainframe.grid(column=0,row=0,sticky=(N, W, E, S),padx=5,pady=5)
        mainframe.columnconfigure(0,weight=1)
        mainframe.rowconfigure(list(range(25)),weight=1)

        self.theme = Theme()
        
            
        ############ SECTIONS ############
        ####### Theme & Language #######
        self.head = Head(self.callbackThemeLight,self.callbackThemeDark)
        self.head.start(mainframe)

        ####### Download path #######
        self.downloadPath = DownloadPath()
        self.downloadPath.start(mainframe)

        ####### Download #######
        self.download = Download(self.downloadPath.txt_DownloadPath)

        ####### Queue #######
        self.queue = Queues()
        self.queue.start(mainframe)

        #Download viene fatto partire dopo perchè serve il frame di Queue
        self.download.start(mainframe,self.queue.frm_Queue,self.window)

        ####### Footer #######
        self.footer = Footer()
        self.footer.start(mainframe)

        self.changeTheme(THEME)
        self.callbackThemeLight()
        self.window.mainloop()

    def changeTheme(self,color):
        if color == "light":
            self.theme.changeToLight(self.window,self.head,self.downloadPath,self.download,self.queue,self.footer)
        elif color == "dark":
            self.theme.changeToDark(self.window,self.head,self.downloadPath,self.download,self.queue,self.footer)

    def callbackThemeLight(self):
        self.changeTheme("light")

    def callbackThemeDark(self):
        self.changeTheme("dark")
        
if __name__ == "__main__":
    Main()
