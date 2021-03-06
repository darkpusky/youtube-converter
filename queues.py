from tkinter import *
from tkinter import ttk
import guifunctions as gfunc
from lang import getLabelIt,getLabelEn

class Queues:

    def start(self,mainframe):
        self.frm_Queue_Container = Frame(mainframe,highlightbackground="red",highlightcolor="red",highlightthickness=2,borderwidth=0)
        self.frm_Queue_Container.grid(row=7,column=0,sticky=(N, W, E, S),rowspan=16)
        #TODO style container
        
        self.canvas_Queue = Canvas(self.frm_Queue_Container,height=20)
        self.canvas_Queue.pack(side=LEFT,fill=BOTH,expand=True)
        self.frm_Queue = Frame(self.canvas_Queue)
        frm_Inner_Canvas = self.canvas_Queue.create_window((0,0), window=self.frm_Queue,anchor=NW)

        self.lbl_None = Label(self.frm_Queue)
        self.lbl_None.pack(fill=X,padx=(0,4))
        
        scrl_Queue = Scrollbar(self.frm_Queue_Container,orient=VERTICAL,command=self.canvas_Queue.yview)
        scrl_Queue.pack(side=RIGHT,fill=Y)
        self.canvas_Queue.config(yscrollcommand=scrl_Queue.set)

        def FrameWidth(event):
            #Ridimensiona il frame interno ogni volta he viene creato
            #un nuovo widget
            canvas_width = event.width
            self.canvas_Queue.itemconfig(frm_Inner_Canvas, width = canvas_width)

        def OnFrameConfigure(event):
            #Ridimensiona il canvas ogni volta he viene creato
            #un nuovo widget
            self.canvas_Queue.configure(scrollregion=self.canvas_Queue.bbox("all"))
            
        def ScrollWheel(event):
            #Evento della rotellina del mouse sul canvas
            if event.delta < 0 and scrl_Queue.get()[1] < 1.0: #Se verso sopra e scroll attivo
                self.canvas_Queue.yview_scroll(-1*(event.delta//120),"units")
            elif event.delta > 0 and scrl_Queue.get()[0] > 0.0: #Se verso basso e scroll attivo
                self.canvas_Queue.yview_scroll(-1*(event.delta//120),"units")
               
        self.frm_Queue.bind("<Configure>",OnFrameConfigure)
        self.canvas_Queue.bind("<Configure>",FrameWidth)
        self.canvas_Queue.bind_all("<MouseWheel>",ScrollWheel)
        
    def changeTheme(self,theme):
        if theme == "dark":
            self.canvas_Queue.configure(background="#171717")
            self.lbl_None.configure(foreground="#FAF3F3")
            for elem in self.frm_Queue.winfo_children():
                try:
                    elem.configure(background="#171717")
                except:
                    pass
        elif theme == "light":
            self.canvas_Queue.configure(background="white")
            self.lbl_None.configure(background="white")
            for elem in self.frm_Queue.winfo_children():
                try:
                    elem.configure(background="white")
                except:
                    pass
        
    def changeLang(self,lang):
        if lang == "it":
            self.lbl_None.configure(text = getLabelIt("none"))
        elif lang == "en":
            self.lbl_None.configure(text = getLabelEn("none"))
            
