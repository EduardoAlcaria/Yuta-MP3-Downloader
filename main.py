from pytubefix import Playlist
from pytubefix import YouTube
from pytubefix.cli import on_progress
        


def downloadSM(link):
    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        print(yt.title)
        ys = yt.streams.get_audio_only()
        ys.download(mp3=True)
        print('\nDownload Successful')
    except:
        print('connection failed')


def downloadMP(link):
    try:
        pl = Playlist(link)
        for video in pl.videos:
            yp = video.streams.get_audio_only()
            yp.download(mp3=True)
        print('Downloads has been successful\n')
    except:
        print('connection failed\n') 


banner = """
        
                __       
   __  ____  __/ /_____ _
  / / / / / / / __/ __ `/
 / /_/ / /_/ / /_/ /_/ / 
 \__, /\__,_/\__/\__,_/  
/____/                   

                           
"""
print(banner)
op = str(input("""What do you want to do: 
Single Music [1] Playlist [2]  Exit[3]
"""))
if op == '1':
    url = str(input('Type an URL: '))
    downloadSM(url)
if op == '2':
    url = str(input('Enter the playlist URL: '))
    downloadMP(url)
