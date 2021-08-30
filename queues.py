from tkinter import *
from tkinter import ttk
import guifunctions as gfunc

class Queues:

    def start(self,mainframe):
        frm_Queue_Container = Frame(mainframe,highlightbackground="red",highlightcolor="red",highlightthickness=2)
        frm_Queue_Container.grid(row=7,column=0,sticky=(N, W, E, S),rowspan=16)
        #TODO style container
        
        canvas_Queue = Canvas(frm_Queue_Container,height=20)
        canvas_Queue.pack(side=LEFT,fill=BOTH,expand=True)
        self.frm_Queue = Frame(canvas_Queue)
        frm_Inner_Canvas = canvas_Queue.create_window((0,0), window=self.frm_Queue,anchor=NW)

        scrl_Queue = Scrollbar(frm_Queue_Container,orient=VERTICAL,command=canvas_Queue.yview)
        scrl_Queue.pack(side=RIGHT,fill=Y)
        canvas_Queue.config(yscrollcommand=scrl_Queue.set)

        def FrameWidth(event):
            #Ridimensiona il frame interno ogni volta he viene creato
            #un nuovo widget
            canvas_width = event.width
            canvas_Queue.itemconfig(frm_Inner_Canvas, width = canvas_width)

        def OnFrameConfigure(event):
            #Ridimensiona il canvas ogni volta he viene creato
            #un nuovo widget
            canvas_Queue.configure(scrollregion=canvas_Queue.bbox("all"))
            
        def ScrollWheel(event):
            #Evento della rotellina del mouse sul canvas
            if event.delta < 0 and scrl_Queue.get()[1] < 1.0: #Se verso sopra e scroll attivo
                canvas_Queue.yview_scroll(-1*(event.delta//120),"units")
            elif event.delta > 0 and scrl_Queue.get()[0] > 0.0: #Se verso basso e scroll attivo
                canvas_Queue.yview_scroll(-1*(event.delta//120),"units")
               
        self.frm_Queue.bind("<Configure>",OnFrameConfigure)
        canvas_Queue.bind("<Configure>",FrameWidth)
        canvas_Queue.bind_all("<MouseWheel>",ScrollWheel)
