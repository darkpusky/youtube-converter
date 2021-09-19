from tkinter import *
from tkinter import ttk
import guifunctions as gfunc
from threading import Thread
from lang import getLabelIt,getLabelEn

class FrameSong:

    def createFrameSong(self,parent,isSingle,song,nsong,lang):

        self.lang = lang
        frm_Object = Frame(parent,borderwidth=1,height=75)
        frm_Object.rowconfigure(0,weight=1)
        frm_Object.columnconfigure(list(range(20)),weight=1)

        frm_Image = Frame(frm_Object,width=150,height=75,highlightbackground = "red", highlightcolor= "red",highlightthickness=2)
        label = Label(frm_Image,width=144,height=70)
        gfunc.createThumbnail(label,song.getThumb())
        label.pack(fill=BOTH)
        #label.configure(width=frm_Object.width/20*2)
        frm_Image.grid(row=0,column=0,columnspan=3,sticky=(N,W),padx=(5,5))
        
        frm_Id = Frame(frm_Object,height=75)
        frm_Id.rowconfigure(list(range(2)),weight=1)
        frm_Id.columnconfigure(list(range(80)),weight=1)
        
        self.lbl_Name = Label(frm_Id)
        self.lbl_Duration = Label(frm_Id)
        if self.lang == "it":
            self.lbl_Name.configure(text = getLabelIt("titolo"))
            self.lbl_Duration.configure(text = getLabelIt("durata"))
        elif self.lang == "en":
            self.lbl_Name.configure(text = getLabelEn("titolo"))
            self.lbl_Duration.configure(text = getLabelEn("durata"))
        self.lbl_Name.grid(row=0,column=0,sticky=(N,E))
        self.lbl_Duration.grid(row=1,column=0,sticky=(N,E))
    
        msg_Name = Label(frm_Id,justify=LEFT,text=song.getTitleSong())
        msg_Name.grid(row=0,column=1,columnspan=79,sticky=(N,W))
        msg_Name.configure(wraplength=frm_Id.winfo_width()/80*70)

        msg_Duration = Label(frm_Id,justify=LEFT,text=song.getDurationSong())
        msg_Duration.grid(row=1,column=1,columnspan=79,sticky=(N,W))
        
        frm_Id.grid(row=0,column=3,columnspan=5,sticky=(W,N,S))
        frm_Id.grid_propagate(0)
        
        sep_Id = ttk.Separator(frm_Object,orient=VERTICAL)
        sep_Id.grid(row=0,column=16,sticky=(N,S,E))

        frm_Progress = Frame(frm_Object)
        frm_Progress.rowconfigure(list(range(10)),weight=1)
        frm_Progress.columnconfigure(0,weight=1)

        style_ProgressBar = gfunc.createStyleProgressBar(frm_Object,nsong)
         
        progress_bar = ttk.Progressbar(frm_Progress,style=style_ProgressBar[1])
        progress_bar.grid(row=0,rowspan=8,column=0,sticky=(W,E),padx=(5,7))
        
        self.lbl_Operation = Label(frm_Progress)
        self.lbl_Operation.grid(row=9,column=0,sticky=(W,N,E))
        
        frm_Progress.grid(row=0,column=17,columnspan=3,sticky=(N,W,E,S))
        
        #Do this only if the element is not single
        if isSingle:
            sep_Frame = ttk.Separator(parent,orient=HORIZONTAL)
            sep_Frame.pack(fill=BOTH,side=BOTTOM,padx=10,pady=5)

        #Delete none label from frame
        if int(nsong) <= 1: #Sta per essere creata una sola canzone
            parent.winfo_children()[0].pack_forget()
        
        frm_Object.pack(fill=X,side=BOTTOM,expand=TRUE,pady=5,padx=(0,4))
        frm_Object.grid_propagate(0)

        #Calcola il momento del wrap al cambio della dimensione del frame ID
        def WrapLabel(event):
            msg_Name.configure(wraplength=event.width/80*70) #Calcolo della griglia

        def WidthId(event):
            frm_Id.configure(width=event.width/20*11)
        
        def WidthImage(event):
            label.configure(width=event.width/20*2) #Calcolo della griglia
            
        frm_Id.bind("<Configure>",WrapLabel)
        #frm_Object.bind("<Configure>",WidthImage)
        frm_Object.bind("<Configure>",WidthId)
        
        def my_hook(d):
            if d['status'] == 'downloading':
                percentual = float(d['_percent_str'][:-1]) * 90 / 100
                label = getLabelIt("scarico") if self.lang == 'it' else getLabelEn("scarico")
                gfunc.setProgress(progress_bar,style_ProgressBar,percentual,self.lbl_Operation,label)
            elif d['status'] == 'finished':
                percentual = 90.0
                label = getLabelIt("converto") if self.lang == 'it' else getLabelEn("converto")
                gfunc.setProgress(progress_bar,style_ProgressBar,percentual,self.lbl_Operation,label)
                song.convert()
                percentual = 100.0
                label = getLabelIt("finito") if self.lang == 'it' else getLabelEn("finito")
                gfunc.setProgress(progress_bar,style_ProgressBar,percentual,self.lbl_Operation,label)
            elif d['status'] == 'error':
                percentual = 0.0
                label = getLabelIt("error") if self.lang == 'it' else getLabelEn("error")
                gfunc.setProgress(progress_bar,style_ProgressBar,percentual,self.lbl_Operation,label)
            #TODO exception hook
        song.activeHook(my_hook)

        #Async download
        Thread(target=song.download).start()

    def changeLang(self,lang):
        if lang == "it":
            self.lang = "it"
            self.lbl_Name.configure(text = getLabelIt("titolo"))
            self.lbl_Duration.configure(text = getLabelIt("durata"))
            if self.lbl_Operation["text"] == getLabelEn("scarico"):
                self.lbl_Operation.configure(text=getLabelIt("scarico"))
            elif self.lbl_Operation["text"] == getLabelEn("converto"):
                self.lbl_Operation.configure(text=getLabelIt("converto"))
            elif self.lbl_Operation["text"] == getLabelEn("finito"):
                self.lbl_Operation.configure(text=getLabelIt("finito"))
            elif self.lbl_Operation["text"] == getLabelEn("error"):
                self.lbl_Operation.configure(text=getLabelIt("error"))
                
                
        elif lang == "en":
            self.lang = "en"
            self.lbl_Name.configure(text = getLabelEn("titolo"))
            self.lbl_Duration.configure(text = getLabelEn("durata"))
            if self.lbl_Operation["text"] == getLabelIt("scarico"):
                self.lbl_Operation.configure(text=getLabelEn("scarico"))
            elif self.lbl_Operation["text"] == getLabelIt("converto"):
                self.lbl_Operation.configure(text=getLabelEn("converto"))
            elif self.lbl_Operation["text"] == getLabelIt("finito"):
                self.lbl_Operation.configure(text=getLabelEn("finito"))
            elif self.lbl_Operation["text"] == getLabelIt("error"):
                self.lbl_Operation.configure(text=getLabelEn("error"))
