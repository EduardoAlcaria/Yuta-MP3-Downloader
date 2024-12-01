from yuta_func.yuta_tools import print_error, print_success, print_warning, download_again
from pytubefix import YouTube, Playlist
from rich.progress import track

def download_single_music(link): #function to download a single music from youtube
    yt = YouTube(link)
    try:
        print_success(f"{yt.title}: ")
        for i in track(range(1), description="[bright_magenta]Downloading..."):
            ys = yt.streams.get_audio_only()
            ys.download(mp3=True)
        print_success("Download Successful")
    except Exception as e:
        print_error(f"connection failed {e}")
    download_again()

def download_music_playlist(link): # function to dowload a playlist from youtube
    try:
        pl = Playlist(link)
        total_videos = len(pl.videos)
        downloads = 0
        for video in track(pl.videos, description="[bright_magenta]Downloading videos...", total=total_videos):
            try:
                print(f"{"\033[1;95m"}Dowloading: {video.title}{"\033[m"}")
                yp = video.streams.get_audio_only()
                yp.download(filename=f"{video.title}.mp3")
                downloads += 1
            except Exception as e:
                downloads -= 1
                print_warning(f"Skipped {video.title}: {e}")
        print_success("All downloads successfuls")      
    except Exception as e:
        print_error(f"connection failed: {e}")   
    download_again()