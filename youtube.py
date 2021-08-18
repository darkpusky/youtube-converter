from __future__ import unicode_literals
import youtube_dl
import utils
import functions as func
import costants as C

class Song:

    def __init__(song,location,link):
        song.location = location
        song.link = link
        song.options = {
            'format': 'bestaudio[ext=webm]',
            'outtmpl': song.location+'%(title)s.%(ext)s',
            'quiet' : True,
            ### Archivio cronologia ###
            #'download_archive' : 'storico.txt',
        }
        song.yt = youtube_dl.YoutubeDL(song.options)

    def getInfo(song):
        return song.yt.extract_info(song.link,download=False)

    def getRealPath(song):
        return song.yt.prepare_filename(song.getInfo())

    def downloadPlaylist(song):
        playlist = song.getInfo()
        for songs in playlist['entries']:
            song.link = songs['webpage_url']
            song.download()
        
        
    def download(song):
        song.yt.download([song.link])
        utils.debug(C.CONVERT,'Now conversion...')
        song.convert()
        
    def convert(song):
        ### Old path ###
        rtmp = song.getRealPath()
        ### New path ###
        ntmp = func.retrieveNewName(rtmp,song.location)
        command = './ffmpeg -i \"' + rtmp + '\" -vn -ab 192k -y \"' + ntmp + '.mp3\"'
        func.runFFMPEG(command)
        utils.debug(C.CONVERT,'End conversion.')
        utils.debug(C.DELETE,'Deleting file...')
        ### Eliminazione del file precedente ###
        func.deleteDuplicate(rtmp)
        utils.debug(C.DELETE,'End delete.')
        
### MAIN ###          
LOCATION = 'C:/Users/valet/Downloads/YoutubeConverter/'
LINK = "https://www.youtube.com/watch?v=WLnnMOLiFtg"
#LINK = "https://www.youtube.com/playlist?list=PL-jfTyhJyYz7fJ8_dhLYZJzTS8uA7HOnx"
song = Song(LOCATION,LINK)
song.download()
#song.downloadPlaylist()
