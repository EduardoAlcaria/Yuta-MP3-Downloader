from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress
from os import name, system
from sys import exit
from re import compile
# Colors for the terminal, ANSI code pattern
cyan = "\033[1;36m"
pink = "\033[1;95m"
green = "\033[1;32m"
red = "\033[1;31m"
color_reset = "\033[m"

def print_success(message):
    print(f"{green}{message}{color_reset}")
def print_error(message):
    print(f"{red}{message}{color_reset}")
def print_warning(message):
    print(f"{cyan}{message}{color_reset}")
def link_auth(link):
    youTube_valid = compile(r"(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+")

    if not youTube_valid.match(link):
        return "invalid link"
    elif "list=" in link:
        return "playlist"
    elif "v=" in link or "youtu.be/" in link: 
        return "video"
    else:
        return "unknown"
#function to ask the user if he wants to download another music
def download_again():
    again = str(input(f"{cyan}Would you like to download again? [y/n]: {color_reset}")).lower().strip()
    if again == "n":
        exit("Good Bye")
    elif again == "y":
        return
    else:
        print_error("Invalid input, Pleace type 'y' or 'n'.")
        download_again()
#function to clean the terminal
def clean_terminal():
    if name == 'nt': # check if the user uses windowns
        system('cls')
    else:
        system('clear') # check if the user uses linux or macOS
def download_single_music(link): #function to download a single music from youtube
    try:
        yt = YouTube(link, on_progress_callback = on_progress)
        ys = yt.streams.get_audio_only()
        ys.download(mp3=True)
        print(f"{pink}{yt.title}: {color_reset}",end="")
        print_success("\nDownload Successful")
    except Exception as e:
        print_error(f"connection failed {e}")
    download_again()
def download_music_playlist(link): # function to dowload a playlist from youtube
    try:
        downloads = 0
        pl = Playlist(link)
        for video in pl.videos:
            try:
                print(f"{pink}Dowloading: {video.title}{color_reset}")
                yp = video.streams.get_audio_only()
                yp.download(filename=f"{video.title}.mp3")
                downloads += 1
            except Exception as e:
                print_warning(f"Skipped {video.title}: {e}")
                downloads -=1
        print_success(f"{downloads} Downloads successfuls")      
    except Exception as e:
        print_error(f"connection failed: {e}")   
    download_again()
def terminal_interface(): # function to start the termianl inteface
    while True:
        try:
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
                        {pink}An MP3 Downloader
                        by Eduardo Alcaria

                    {red}FOR EDUCATIONAL PURPOSES ONLY.
                NOT RESPONSIBLE FOR COPYRIGHT INFRINGEMENT{color_reset}               
                    """
                print(banner)
                url = str(input(f"{cyan}Enter a YOUTUBE Playlist/Video link>{color_reset} ")).strip()
                val = link_auth(url)


                if val == "video": # single music download
                    print_success("Starting Download....")
                    download_single_music(url)
                elif val == "playlist":# download a playslit
                    print_success("Starting Download....")
                    download_music_playlist(url)
                elif val == "invalid": # exit the problem
                    print_error("\nInvalid link. Please enter the url again")
                else: # invalid command handle
                    print_error("\nUnknown link. Please try again")
        except KeyboardInterrupt:
            print_warning("\nExiting the program, Good bye!")
            break
        except Exception as e:
            print_error("Unexpected error {e}")
clean_terminal()
terminal_interface()
