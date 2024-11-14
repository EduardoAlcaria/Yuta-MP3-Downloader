from pytubefix import Playlist, YouTube
from pytubefix.cli import on_progress
from time import sleep
import os, sys
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

#function to ask the user if he wants to download another music
def download_again():
    again = str(input(f"{yellow}Would you like to download another one? [y/n]: {color_reset}")).lower().strip()
    if again == "y":
        terminal_interface()
    else:
        sys.exit()
#function to clean the terminal
def clean_terminal():
    if os.name == 'nt': # check if the user uses windowns
        os.system('cls')
    else:
        os.system('clear') # check if the user uses linux or macOS
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
            yp = video.streams.get_audio_only()
            yp.download(filename=f"{video.title}.mp3")
        print_success("Downloads has been successful")
        download_again()      
    except Exception as e:
        print_error(f"connection failed: {e}") 
        terminal_interface()     
def terminal_interface(): # function to start the termianl inteface
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
    choice = str(input(f"What do you want to do:\n{cyan}[1] Single Music{color_reset}\n{yellow}[2] Playlist{color_reset}\n{red}[3] Exit{color_reset}\n> ")).lower().strip()
    if choice == "1": # single music download
        url = str(input(f"{yellow}Type an URL: {color_reset}")).strip()
        download_single_music(url)
    elif choice == "2":# download a playslit
        url = str(input(f"{yellow}Enter the playlist URL: {color_reset}")).strip()
        download_music_playlist(url)
    elif choice == "3": # exit the problem
        sys.exit(f"{yellow}Exiting Program{color_reset}")
    else: # invalid command handle
        print(f"{red} invalid choice, Pleace try again{color_reset}")
    terminal_interface()

terminal_interface() # start the program