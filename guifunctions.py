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
from lang import getLabelIt,getLabelEn

### Initialization of the window in center position ###
def centerMainWindow(window,w,h):
    positionRight = int(window.winfo_screenwidth() / 2 - w/2)
    positionDown = int(window.winfo_screenheight() / 2 - h/2)
    return "+{}+{}".format(positionRight, positionDown)

### Handle creation for theme buttons ###
def createDefaultThemeButton(parent,text):
    return Button(parent,text=text,borderwidth=1,cursor="hand2",highlightthickness=0,width=7,height=2)

### Handle commands for theme buttons ###
def handleChangeThemeToDark(light,dark,callback):
    if dark['relief'] == "raised":
        light.configure(relief="raised")
        dark.configure(relief="sunken")
        callback()
    #TODO implement change of the style

def handleChangeThemeToLight(light,dark,callback):
    if light['relief'] == "raised":
        light.configure(relief="sunken")
        dark.configure(relief="raised")
        callback()
    #TODO implement change of the style

### Handle creation for lang buttons ###
def createDefaultLangButton(parent,image):
    return Button(parent,borderwidth=0,cursor="hand2",image=image,relief="flat")

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
def validationPathDownload(directory,lang):
    if directory == "": #Empty directory
        if lang == "it":    
            messagebox.showinfo(message= getLabelIt("empty_dir"))
        elif lang == "en":
            messagebox.showinfo(message= getLabelEn("empty_dir"))
        return False
    if not utils.isExistDir(directory): #Path does not exist
        if lang == "it":
            messagebox.showerror(message= getLabelIt("exist_dir"))
        elif lang == "en":
            messagebox.showerror(message= getLabelEn("exist_dir"))
        return False
    if not utils.isDir(directory): #Path is not a directory
        if lang == "it":
            messagebox.showerror(message= getLabelIt("valid_dir"))
        elif lang == "en":
            messagebox.showerror(message= getLabelEn("valid_dir"))
        return False
    return True

def isSong(link):
    if "youtube.com" not in link:
        return False
    if "watch?v=" not in link:
        return False
    if "&list=" in link:
        return False
    return True

def isPlaylist(link):
    if "youtube.com" not in link:
        return False
    if "list=" not in link:
        return False
    return True

### Validation for link on click download button ###
def validationLink(link,song,lang):
    if link == "": #Empty link song,playlist
        if lang == "it":
            messagebox.showinfo(message= getLabeIt("empty_link"))
        elif lang == "en":
            messagebox.showinfo(message= getLabeEn("empty_link"))
        return False
    #song = True if come from createSong
    #song = False if come from createPlaylist
    if song and not isSong(link):
        if lang == "it":
            messagebox.showerror(message= getLabelIt("valid_song"))
        elif lang == "en":
            messagebox.showerror(message= getLabelEn("valid_song"))
        return False
    elif not song and not isPlaylist(link):
        if lang == "it":
            messagebox.showerror(message= getLabelIt("valid_playlist"))
        elif lang == "en":
            messagebox.showerror(message= getLabelEn("valid_playlist"))
        return False
    return True
        
### Validation general download ###
def validationDownload(directory,link,song,lang):
    return validationLink(link,song,lang) and validationPathDownload(directory,lang)
    
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
def createSong(parent,directory,entryLink,array,lang):
    if validationDownload(directory,entryLink.get(),True,lang):
        try:   
            song = Song(directory,entryLink.get())
            frame = FrameSong()
            frame.createFrameSong(parent,utils.isNotSingle(array),song,str(len(array)+1),lang)
            array.append(frame)
        except:
            messagebox.showerror(message= getLabelIt("error_download") if lang == "it" else getLabelEn("error_download"))

### Download single song,only use for playlist ###
def downloadSong(directory,parent,array,songs,lang):
    singleSong = Song(directory,songs['webpage_url'])
    frame = FrameSong()
    frame.createFrameSong(parent,utils.isNotSingle(array),singleSong,str(len(array)+1),lang)
    array.append(frame)

def iterator(directory,parent,array,playlist,lang):
    for songs in playlist:
        #try:
        downloadSong(directory,parent,array,songs,lang)
        #except:
         #   continue

def createPlaylist(parent,directory,entryLink,array,lang):
    if validationDownload(directory,entryLink.get(),False,lang):
        playlist = Song(directory,entryLink.get()).getSongs()
        Thread(target = iterator, args=(directory,parent,array,playlist,lang)).start()
        #handleLoadPlaylist(lang)

### Handle window load playlist ###
def handleLoadPlaylist(lang):
    print("qui")
    top = Toplevel()
    top.resizable(FALSE,FALSE)

### Handle creation for feedback button ###
def createFeedbackButton(parent,text):
    return Button(parent,cursor="hand2",text=text)

### Handle paste link download ###
def pasteLink(entry,window):
    entry.delete(0,END) #Delete the old text
    entry.insert(0,window.clipboard_get())

### Handle missing ffmpeg ###
def missingFFmpeg(lang):
    root = Tk()
    root.withdraw()
    messagebox.showerror(message= getLabelIt("exist_ffmpeg") if lang == "it" else getLabelEn("exist_ffmpeg")) 
