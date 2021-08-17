from __future__ import unicode_literals
import youtube_dl
import os

class Song:

    def __init__(song,location):
        song.location = location
        song.options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': song.location+'%(title)s.%(ext)s',
            'download_archive' : 'storico.txt'
        }
        
    def download(song,link):
        with youtube_dl.YoutubeDL(song.options) as ydl:
            ydl.download([link])

LOCATION = 'C:/Users/valet/Downloads/YoutubeConverter/'
song = Song(LOCATION)
song.download("https://www.youtube.com/watch?v=WLnnMOLiFtg")
