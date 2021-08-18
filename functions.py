import subprocess
import os

def runFFMPEG(command):
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    subprocess.call(command,startupinfo=si)

def deleteDuplicate(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")
        #TODO Exception

def retrieveNewName(path,location):
    name = os.path.splitext(os.path.basename(path))[0]
    return location + name
