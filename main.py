from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress
import os
import sys

cyan = "\033[1;36m"
yellow = "\033[1;33m"
pink = "\033[1;95m"
green = "\033[1;32m"
red = "\033[1;31m"
color_reset = "\033[m"

def clean_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('cls')
def download_single_music(link):
    try:
        yt = YouTube(url, on_progress_callback = on_progress)
        ys = yt.streams.get_audio_only()
        ys.download(mp3=True)
        print(f"{yt.title}: {green}Download Successful{color_reset}")
    except Exception as e:
        print(f"{red}connection failed {e} {color_reset}")


def download_music_playlist(link):
    try:
        pl = Playlist(link)
        for video in pl.videos:
            yp = video.streams.get_audio_only()
            yp.download(mp3=True)
        print(f"{green}Downloads has been successful{color_reset}\n")
    except Exception as e:
        print(f"{red}connection failed {e} {color_reset}\n") 

clean_terminal()
banner = f"""
{pink}         
                 __       
    __  ____  __/ /_____ _
    / / / / / / / __/ __ `/
    / /_/ / /_/ / /_/ /_/ / 
    \__, /\__,_/\__/\__,_/  
    /____/                   
{color_reset}
{pink}A Mp3 Dowloader{color_reset}  {pink}by Eduardo Alcaria{color_reset}                       
    """
print(banner)
choice = str(input(f"What do you want to do:\n{cyan}[1] Single Music{color_reset}\n{yellow}[2] Playlist{color_reset}\n{red}[3] Exit{color_reset}\n> "))
if choice == "1":
    url = str(input('Type an URL: '))
    download_single_music(url)
elif choice == "2":
    url = str(input('Enter the playlist URL: '))
    download_music_playlist(url)
elif choice == "3":
    sys.exit("Exiting Program")
else:
    print(f"{red} invalid choice, Pleace try again{color_reset}")