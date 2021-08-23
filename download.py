from tkinter import *
from tkinter import ttk
import guifunctions as gfunc

class Download:

    def start(self,mainframe):
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

        txt_Download_Song = ttk.Entry(frm_Download_Song_Path,exportselection=0,width=40)
        txt_Download_Playlist = ttk.Entry(frm_Download_Playlist_Path,exportselection=0,width=40)
        txt_Download_Song.grid(row=0,column=1)
        txt_Download_Playlist.grid(row=0,column=1)

        btn_Download_Song = gfunc.createDefaultDownloadButton(frm_Download_Song,"Download")
        btn_Download_Song.grid(row=2,column=0)
        btn_Download_Playlist = gfunc.createDefaultDownloadButton(frm_Download_Playlist,"Download")
        btn_Download_Playlist.grid(row=2,column=0)
