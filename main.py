from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress
from os import name, system
from sys import exit
from re import compile
# Colors for the terminal, ANSI code pattern
cyan = "\033[1;36m"
yellow = "\033[1;33m"
pink = "\033[1;95m"
green = "\033[1;32m"
red = "\033[1;31m"
color_reset = "\033[m"

def print_success(massage):
    print(f"{green}{massage}{color_reset}")
def print_error(massage):
    print(f"{red}{massage}{color_reset}")
def print_warning(massage):
    print(f"{yellow}{massage}{color_reset}")
def link_auth(link):
    youTube_valid = compile(r"(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+"
    )

    if not youTube_valid.match(link):
        return "invalid link"
    if "list=" in link:
        return "playlist"
    if "v=" in link or "youtu.be/" in link: 
        return "video"
    return "unknown"
#function to ask the user if he wants to download another music
def download_again():
    again = str(input(f"{yellow}Would you like to download another one? [y/n]: {color_reset}")).lower().strip()
    if again == "y":
        terminal_interface()
    else:
        exit()
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
        print(f"{yt.title}: ",end="")
        print_success("Download Successful")
        download_again()
    except Exception as e:
        print_error(f"connection failed {e}")
        terminal_interface()
def download_music_playlist(link): # function to dowload a playlist from youtube
    try:
        pl = Playlist(link)
        for video in pl.videos:
            print_success(f"Dowloading: {video.title}")
            yp = video.streams.get_audio_only()
            yp.download(filename=f"{video.title}.mp3")
        print_success("Downloads has been successful")
        download_again()      
    except Exception as e:
        print_error(f"connection failed: {e}") 
        terminal_interface()     
def terminal_interface(): # function to start the termianl inteface
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
        {pink}An MP3 Downloader by Eduardo Alcaria{color_reset}    

        {red}FOR EDUCATIONAL PURPOSES ONLY. NOT RESPONSIBLE FOR COPYRIGHT INFRINGEMENT{color_reset}                   
            """
        print(banner)
        url = str(input(f"{cyan}Enter a YOUTUBE link>{color_reset} ")).strip()
        val = link_auth(url)
        if val == "video": # single music download
            print_success("Starting Download....")
            download_single_music(url)
        elif val == "playlist":# download a playslit
            print_success("Starting Download....")
            download_music_playlist(url)
        elif val == "invalid": # exit the problem
            clean_terminal()
            print_error("invalid link, pleace enter the url again")
        else: # invalid command handle
            clean_terminal()
            print_error("{unknown link, Pleace try again{color_reset")
        terminal_interface()
    except:
        print_error("Unexpected input, pleace try again")

clean_terminal()
terminal_interface() # start the program
