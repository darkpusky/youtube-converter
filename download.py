from tkinter import *
from tkinter import ttk
import guifunctions as gfunc

class Download:

    def __init__(self,directoryEntry):
        self.entry = directoryEntry
        self.song_list = []
        self.image = PhotoImage(file = r".\utils\clipboard.png")
    
    def start(self,mainframe,queue_frame,window):
        frm_Download = ttk.Frame(mainframe,borderwidth=1)
        frm_Download.grid(row=4,column=0,sticky=(N, W, E, S))
        frm_Download.columnconfigure(list(range(7)),weight=1)
        frm_Download.rowconfigure(0,weight=1)
        frm_Download_Song = ttk.Frame(frm_Download)
        frm_Download_Playlist = ttk.Frame(frm_Download)
        frm_Download_Song.grid(row=0,column=1)
        frm_Download_Playlist.grid(row=0,column=5)

        lbl_Download_Song = ttk.Label(frm_Download_Song,text="Scarica Canzone")
        lbl_Download_Playlist = ttk.Label(frm_Download_Playlist,text="Scarica Playlist")
        lbl_Download_Song.grid(row=0,column=0)
        lbl_Download_Playlist.grid(row=0,column=0)

        frm_Download_Song_Path = ttk.Frame(frm_Download_Song)
        frm_Download_Song_Path.grid(row=1,column=0,pady=7)
        frm_Download_Playlist_Path = ttk.Frame(frm_Download_Playlist)
        frm_Download_Playlist_Path.grid(row=1,column=0,pady=7)

        lbl_Download_Song_Link = ttk.Label(frm_Download_Song_Path,text="Link:")
        lbl_Download_Song_Link.grid(row=0,column=0)
        lbl_Download_Playlist_Link = ttk.Label(frm_Download_Playlist_Path,text="Link:")
        lbl_Download_Playlist_Link.grid(row=0,column=0)

        self.txt_Download_Song = Entry(frm_Download_Song_Path,exportselection=0,width=40,highlightthickness=2,highlightbackground="red",highlightcolor= "red",insertbackground="red")
        ### MOCK ###
        self.txt_Download_Song.insert(0,"https://www.youtube.com/watch?v=WLnnMOLiFtg")
        ### MOCK ###
        self.txt_Download_Playlist = Entry(frm_Download_Playlist_Path,exportselection=0,width=40,highlightthickness=2,highlightbackground="red",highlightcolor= "red",insertbackground="red")
        self.txt_Download_Song.grid(row=0,column=1)
        self.txt_Download_Playlist.grid(row=0,column=1)

        self.btn_Paste_Download_Song = gfunc.createDefaultOpendDirButton(frm_Download_Song_Path,self.image)
        self.btn_Paste_Download_Song.grid(row=0,column=2,padx=2)
        self.btn_Paste_Download_Playlist = gfunc.createDefaultOpendDirButton(frm_Download_Playlist_Path,self.image)
        self.btn_Paste_Download_Playlist.grid(row=0,column=2,padx=2)
        self.btn_Paste_Download_Song.configure(command=lambda:gfunc.pasteLink(self.txt_Download_Song,window))
        self.btn_Paste_Download_Playlist.configure(command=lambda:gfunc.pasteLink(self.txt_Download_Playlist,window))
  
        self.btn_Download_Song = gfunc.createDefaultDownloadButton(frm_Download_Song,"Download")
        self.btn_Download_Song.grid(row=2,column=0)
        self.btn_Download_Playlist = gfunc.createDefaultDownloadButton(frm_Download_Playlist,"Download")
        self.btn_Download_Playlist.grid(row=2,column=0)
        self.btn_Download_Song.configure(command=lambda:gfunc.createSong(queue_frame,self.entry.get(),self.txt_Download_Song,self.song_list))
        self.btn_Download_Playlist.configure(command=lambda:gfunc.createPlaylist(queue_frame,self.entry.get(),self.txt_Download_Playlist,self.song_list))

        #Start command on enter key
        self.txt_Download_Song.bind('<Return>',lambda e:gfunc.createSong(queue_frame,self.entry.get(),self.txt_Download_Song,self.song_list))
        self.txt_Download_Playlist.bind('<Return>',lambda e:gfunc.createPlaylist(queue_frame,self.entry.get(),self.txt_Download_Playlist,self.song_list))

    def changeTheme(self,theme):
        if theme == "dark":
            self.btn_Paste_Download_Song.configure(background="#C8C6C6",activebackground="#C8C6C6")
            self.btn_Paste_Download_Playlist.configure(background="#C8C6C6",activebackground="#C8C6C6")
            
            self.btn_Download_Song.configure(background="#C8C6C6",activebackground="#C8C6C6",foreground="black")
            self.btn_Download_Playlist.configure(background="#C8C6C6",activebackground="#C8C6C6",foreground="black")
        elif theme == "light":
            self.btn_Paste_Download_Song.configure(background="#FAF3F3",activebackground="#FAF3F3")
            self.btn_Paste_Download_Playlist.configure(background="#FAF3F3",activebackground="#FAF3F3")
            
            self.btn_Download_Song.configure(background="#FAF3F3",activebackground="#FAF3F3")
            self.btn_Download_Playlist.configure(background="#FAF3F3",activebackground="#FAF3F3")
