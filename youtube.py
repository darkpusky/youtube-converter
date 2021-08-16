from __future__ import unicode_literals
import youtube_dl
import os

class Song:

    def __init__(song):
        song.save_path = '/'.join(os.getcwd().split('/')[:3]) + '\Downloads'
        song.save_download = 'C:\\Users\\Exolab\\Downloads'
        song.options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': song.save_download,
        }
        
    def download(song,link):
        with youtube_dl.YoutubeDL(song.options) as ydl:
            ydl.download([link])

song = Song()
song.download("https://www.youtube.com/watch?v=WLnnMOLiFtg")
