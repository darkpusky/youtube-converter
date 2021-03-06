from tkinter import *
from tkinter import ttk
import guifunctions as gfunc
from PIL import Image, ImageTk
from lang import getLabelIt,getLabelEn

class Footer:

    def start(self,mainframe):
        
        frm_Footer = ttk.Frame(mainframe,borderwidth=1)
        frm_Footer.grid(row=23,rowspan=4,column=0,sticky=(N, W, E, S))
        frm_Footer.rowconfigure(list(range(2)),weight=1)
        frm_Footer.columnconfigure(list(range(4)),weight=1)

        lbl_Image = ttk.Label(frm_Footer)
        image = Image.open("./utils/smussato.png")
        image = image.resize((60,60),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        lbl_Image.image = img
        lbl_Image.configure(image=img)
        lbl_Image.grid(row=0,column=0,sticky=(N,W,S),padx=(60,0))

        self.lbl_Desc = ttk.Label(frm_Footer,justify=LEFT)
        self.lbl_Desc.grid(row=0,column=1,columnspan=2,sticky=(N,W,S))

        self.lbl_Copyright = ttk.Label(frm_Footer,anchor=CENTER,text="© 2021 VTP. Tutti i diritti sono riservati.")
        self.lbl_Copyright.grid(row=1,column=0,columnspan=4,sticky=(S,W,E))

        lbl_Version = ttk.Label(frm_Footer,text="v0.7")
        #TODO version da costante
        lbl_Version.grid(row=1,column=0,columnspan=4,sticky=(E,S))
        
        self.btn_feedback = gfunc.createFeedbackButton(frm_Footer,"Feedback")
        self.btn_feedback.grid(row=0,column=3,sticky=(W))

    def changeTheme(self,theme):
        if theme == "dark":
            self.btn_feedback.configure(background="red",activebackground="red",foreground="black",activeforeground="black")
        elif theme == "light":
            self.btn_feedback.configure(background="red",activebackground="red")

    def changeLang(self,lang):
        if lang == "it":
            self.lbl_Desc.configure(text = (getLabelIt("footer_desc") + getLabelIt("footer_lib")))
            self.lbl_Copyright.configure(text = getLabelIt("copyright"))
        elif lang == "en":
            self.lbl_Desc.configure(text = (getLabelEn("footer_desc") + getLabelEn("footer_lib")))
            self.lbl_Copyright.configure(text = getLabelEn("copyright"))
