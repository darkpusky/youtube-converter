from tkinter import *
from tkinter import ttk
import guifunctions as gfunc
from it import IT_LANG as IT
from en import EN_LANG as EN

class Lang():

    def changeToIt(self,downloadPath,download,queue,footer):
        downloadPath.changeLang("it")
        download.changeLang("it")
        queue.changeLang("it")
        footer.changeLang("it")
        
    def changeToEn(self,downloadPath,download,queue,footer):
        downloadPath.changeLang("en")
        download.changeLang("en")
        queue.changeLang("en")
        footer.changeLang("en")

def getLabelIt(prop):
    return IT[prop]

def getLabelEn(prop):
    return EN[prop]

