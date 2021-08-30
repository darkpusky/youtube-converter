from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import utils as utils
from songframe import FrameSong
from youtube import Song
from PIL import Image, ImageTk
from io import BytesIO
from urllib.request import urlopen
from threading import Thread

### Initialization of the window in center position ###
def centerMainWindow(window,w,h):
    positionRight = int(window.winfo_screenwidth() / 2 - w/2)
    positionDown = int(window.winfo_screenheight() / 2 - h/2)
    return "+{}+{}".format(positionRight, positionDown)

### Handle creation for theme buttons ###
def createDefaultThemeButton(parent,text):
    return Button(parent,text=text,borderwidth=1,cursor="hand2",highlightthickness=0,width=7,height=2)

### Handle commands for theme buttons ###
def handleChangeThemeToDark(light,dark):
    if dark['relief'] == "raised":
        light.configure(relief="raised")
        dark.configure(relief="sunken")
    #TODO implement change of the style

def handleChangeThemeToLight(light,dark):
    if light['relief'] == "raised":
        light.configure(relief="sunken")
        dark.configure(relief="raised")
    #TODO implement change of the style

### Handle creation for lang buttons ###
def createDefaultLangButton(parent,image):
    return Button(parent,borderwidth=0,cursor="hand2",image=image,relief="flat")

### Handle commands for language buttons ###
def handleChangeLangToIT():
    #TODO implement change of the language
    return

def handleChangeLangToUK():
    #TODO implement chenage of the language
    return

### Handle creation for directory button ###
def createDefaultOpendDirButton(parent,image):
    return Button(parent,borderwidth=1,cursor="hand2",image=image,height=18)

### Handle ask directory ###
def getDirectory(entry):
    oldvar = entry.get() #Memorize the old text
    if entry.get() != "":
        entry.delete(0,END) #Delete the old text
    entry.insert(0,filedialog.askdirectory()) #Text from user
    if(entry.get() == ""):
        entry.insert(0,oldvar) #Set old text if user cancel the request

### Handle creation for download button ###
def createDefaultDownloadButton(parent,text):
    return Button(parent,borderwidth=1,cursor="hand2",text=text)

### Validation for directory on click of the download button ###
def validationPathDownload(directory):
    if directory == "": #Empty directory
        messagebox.showinfo(message="La cartella di destinazione non può essere vuota")
        return False
    if not utils.isExistDir(directory): #Path does not exist
        messagebox.showerror(message="La cartella di destinazione non esiste")
        return False
    if not utils.isDir(directory): #Path is not a directory
        messagebox.showerror(message="La cartella di destinazione non è una cartella valida")
        return False
    return True

def isSong(link):
    if "www.youtube.com" not in link:
        return False
    if "watch?v=" not in link:
        return False
    if "&list=" in link:
        return False
    return True

def isPlaylist(link):
    if "www.youtube.com" not in link:
        return False
    if "list=" not in link:
        return False
    return True

### Validation for link on click download button ###
def validationLink(link,song):
    if link == "": #Empty link song,playlist
        messagebox.showinfo(message="Il link non può essere vuoto")
        return False
    #song = True if come from createSong
    #song = False if come from createPlaylist
    if song and not isSong(link):
        messagebox.showerror(message="Il link non sembra valido,deve essere del tipo:\n-\"https://www.youtube.com/watch?v=AAAAAAAAAAA\"")
    elif not song and not isPlaylist(link):
        messagebox.showerror(message="Il link non sembra valido,deve essere del tipo:\n-\"https://www.youtube.com/watch?v=AAAAAAAAAAA&list=AAAA...\"")
    return True
        
### Validation general download ###
def validationDownload(directory,link,song):
    return validationLink(link,song) and validationPathDownload(directory)
    
### Create thumbnail for song ###
def createThumbnail(label,url):
    image_bytes = urlopen(url).read()
    data_stream = BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    pil_image = pil_image.resize((150,74),Image.ANTIALIAS)
    tk_image = ImageTk.PhotoImage(pil_image)
    label.image = tk_image
    label.configure(image=tk_image)

### Create progressbar ###
def createStyleProgressBar(parent,n):
    style = ttk.Style(parent)
    style.theme_use('alt')
    styleBar = n + 'text.Horizontal.TProgressbar'
    style.layout(styleBar, 
                     [('Horizontal.Progressbar.trough',
                       {'children': [('Horizontal.Progressbar.pbar',
                                      {'side': 'left', 'sticky': 'ns'})],
                        'sticky': 'nswe'}), 
                      ('Horizontal.Progressbar.label', {'sticky': ''})])
    style.configure(styleBar,text= "{:.1f}%".format(0),background="red")
    return (style,styleBar)

### Set Progress Bar ###
def setProgress(progress,style,n,label,text):
    style[0].configure(style[1],text= "{:.1f}%".format(n))
    progress.configure(value=n)
    label.configure(text=text)

### Creation of the frame for queue ###
def createSong(parent,directory,entryLink,array):
    if validationDownload(directory,entryLink.get(),True):
        song = Song(directory,entryLink.get())
        FrameSong().createFrameSong(parent,utils.isNotSingle(array),song,str(len(array)+1))
        #TODO exception
        array.append(len(array)+1)

### Download single song,only use for playlist ###
def downloadSong(directory,parent,array,songs):
    singleSong = Song(directory,songs['webpage_url'])
    FrameSong().createFrameSong(parent,utils.isNotSingle(array),singleSong,str(len(array)+1))
    #TODO exception

def iterator(directory,parent,array,playlist):
    for songs in playlist:
        #Thread(target = downloadSong, args=(directory,parent,array,songs)).start()
        downloadSong(directory,parent,array,songs)
        array.append(len(array)+1)

def createPlaylist(parent,directory,entryLink,array):
    if validationDownload(directory,entryLink.get(),False):
        playlist = Song(directory,entryLink.get()).getSongs()
        Thread(target = iterator, args=(directory,parent,array,playlist)).start()

### Handle creation for feedback button ###
def createFeedbackButton(parent,text):
    return Button(parent,borderwidth=1,cursor="hand2",text=text)

### Handle paste link download ###
def pasteLink(entry,window):
    entry.delete(0,END) #Delete the old text
    entry.insert(0,window.clipboard_get())
