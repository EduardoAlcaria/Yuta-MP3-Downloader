from os import name, system
from re import compile

def print_success(message):
    print(f"{"\033[1;95m"}{message}{"\033[m"}")
def print_error(message):
    print(f"{"\033[1;31m"}{message}{"\033[m"}")
def print_warning(message):
    print(f"{"\033[1;36m"}{message}{"\033[m"}")

def clean_terminal():
    if name == 'nt': # check if the user uses windowns
        system('cls')
    else:
        system('clear') # check if the user uses linux or macOS

def download_again(msg):
    again = str(input(f"{"\033[1;36m"}{msg}{"\033[m"}")).lower().strip()
    if again == "n":
        exit("Good Bye")
    elif again == "y":
        return
    else:
        print_error("Invalid input, Pleace type 'y' or 'n'.", end="")
        download_again(">")

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