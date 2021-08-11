from pytube import YouTube

class Song:
    def __init__(song, link):
        song.yt = YouTube(link,on_progress_callback=progress_func,
                          on_complete_callback=complete_func,
                          proxies=my_proxies)

    def getTitle(song):
        print(song.yt.title)

    def getThumb(song):
        print(song.yt.thumbnail_url)

song = Song('https://www.youtube.com/watch?v=WLnnMOLiFtg')
song.getTitle()
