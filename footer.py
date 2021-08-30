from tkinter import *
from tkinter import ttk
import guifunctions as gfunc
from PIL import Image, ImageTk

class Footer:

    def start(self,mainframe):
        
        frm_Footer = ttk.Frame(mainframe,borderwidth=1)
        frm_Footer.grid(row=23,rowspan=4,column=0,sticky=(N, W, E, S))
        frm_Footer.rowconfigure(list(range(2)),weight=1)
        frm_Footer.columnconfigure(list(range(4)),weight=1)

        lbl_Image = Label(frm_Footer)
        image = Image.open("C:/Users/valet/Desktop/youtube_converter/youtube-converter/utils/smussato.png")
        image = image.resize((60,60),Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        lbl_Image.image = img
        lbl_Image.configure(image=img)
        lbl_Image.grid(row=0,column=0,sticky=(N,W,S),padx=(60,0))

        lbl_Desc = Label(frm_Footer,justify=LEFT,text="Il programma è stato scritto totalmente in python, con le seguenti librerie:\nyoutube_dl, pillow e tkinter.")
        lbl_Desc.grid(row=0,column=1,columnspan=2,sticky=(N,W,S))

        lbl_Copyright = Label(frm_Footer,text="© 2021 VTP. Tutti i diritti sono riservati.")
        lbl_Copyright.grid(row=1,column=0,columnspan=4,sticky=(S,W,E))

        btn_feedback = gfunc.createFeedbackButton(frm_Footer,"Feedback")
        btn_feedback.grid(row=0,column=3,sticky=(W))
