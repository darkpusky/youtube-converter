from __future__ import unicode_literals
import youtube_dl
import utils as utils
import functions as func
import costants as C
from pathlib import Path
import os

class Song:

    def __init__(song,location,link):
        song.location = location
        song.link = link
        song.options = {
            'format': 'bestaudio[ext=webm]',
            'outtmpl': song.location+'/'+'%(title)s.%(ext)s',
            'quiet' : True,
            'nocheckcertificate' : True,
            'progress_hooks': [],
            ### Archivio cronologia ###
            #'download_archive' : 'storico.txt',
        }
        song.yt = youtube_dl.YoutubeDL(song.options)
        song.downloadPath = str(Path.home() / "Downloads")
        song.info = song.yt.extract_info(song.link,download=False)

    def getRealPath(song):
        return song.yt.prepare_filename(song.info)

    def downloadPlaylist(song):
        playlist = song.info
        for songs in playlist['entries']:
            song.link = songs['webpage_url']
            song.info = song.yt.extract_info(song.link,download=False)
            song.download()
        
        
    def download(song):
        song.yt.download([song.link])
        utils.debug(C.CONVERT,'Now conversion...')
        #song.convert()
        
    def convert(song):
        ### Old path ###
        rtmp = song.getRealPath()
        ### New path ###
        ntmp = func.retrieveNewName(rtmp,song.downloadPath)
        command = './ffmpeg -i \"' + rtmp + '\" -vn -ab 192k -y \"' + ntmp + '.mp3\"'
        func.runFFMPEG(command)
        utils.debug(C.CONVERT,'End conversion.')
        utils.debug(C.CONVERT,'Moving file...')
        #Spostamento del file da Download
        func.moveFile(ntmp,func.retrieveNewName(rtmp,song.location))
        utils.debug(C.CONVERT,'End moving file')            
        utils.debug(C.DELETE,'Deleting file...')
        ### Eliminazione del file precedente ###
        func.deleteDuplicate(rtmp)
        utils.debug(C.DELETE,'End delete.')

    #### Functions for info ###
    def getTitleSong(song):
        return song.info['title']

    def getDurationSong(song):
        return utils.formatDuration(song.info['duration'])

    def getThumb(song):
        return song.info['thumbnails'][0]['url']

    def activeHook(song,hook):
        song.yt._progress_hooks = [hook]

    ### Only for playlist ###
    def getSongs(song):
        return song.info['entries']
        
### MAIN TEST ###          
#LOCATION = 'H:'
#LOCATION ='C:/Users/valet/Desktop/youtube_converter/youtube-converter/YoutubeConverter'   
#LINK = "https://www.youtube.com/watch?v=hmfo73iuUuc"
#LINK = "https://www.youtube.com/playlist?list=PL7KJ8NgcCDuUftHEusHd3VWkl1BKC__Rs"
#LINK = "https://www.youtube.com/watch?v=T_ipuR5eTh0&list=PLWjQPTT1tFBYxEUGIOjxE0liqO0QEmpT3"
#song = Song(LOCATION,LINK)
#song.download()
#song.downloadPlaylist()
