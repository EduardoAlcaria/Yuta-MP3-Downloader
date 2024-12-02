from yuta_func.yuta_downloader import download_single_music, download_music_playlist
from yuta_func.yuta_tools import link_auth, clean_terminal, print_success, print_error, print_warning

cyan = "\033[1;36m"
pink = "\033[1;95m"
red = "\033[1;31m"
color_reset = "\033[m"

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
                        Version: 0.9.1                
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