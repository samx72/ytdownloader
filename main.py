from pytube import YouTube
import os
import time
import ctypes
from termcolor import colored
os.system("cls")

print(colored("for more (shits) programs -> https://github.com/samx72", "green"))
time.sleep(2.3)
os.system("cls")

ctypes.windll.kernel32.SetConsoleTitleW("yt downloader")

work = True

while(work == True):
    os.system("cls")
    print(colored("""

    ██╗░░░██╗████████╗  ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
    ╚██╗░██╔╝╚══██╔══╝  ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ░╚████╔╝░░░░██║░░░  ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝
    ░░╚██╔╝░░░░░██║░░░  ██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗
    ░░░██║░░░░░░██║░░░  ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║
    ░░░╚═╝░░░░░░╚═╝░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
    """, "cyan"))

    #work = True

    #while(work == True):
        

    link = input("url: ")
    path = input("path where video download: ")
    try:
        yt = YouTube(
        link,
        use_oauth=False,
        allow_oauth_cache=True
        )

        os.system("cls")
        print(f"i found this video: {yt.title}")
        print("Number of views: ",yt.views)
        print("Length of video: ",yt.length, "seconds")
        ys = yt.streams.get_highest_resolution()
        input("click enter to download")

        print(colored("Downloading...", "green"))

        ys.download(path)
        os.system("cls")
        print(colored("video is downloaded", "blue"))

        end = input("""
do you want continue in this program?(y/n): """)

        if(end == "y"):
            continue

        else:
            work = False
            print("program ended")
            exit()
    except:
        os.system("cls")
        print(colored("""

        ██╗░░░██╗████████╗  ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
        ╚██╗░██╔╝╚══██╔══╝  ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
        ░╚████╔╝░░░░██║░░░  ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝
        ░░╚██╔╝░░░░░██║░░░  ██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗
        ░░░██║░░░░░░██║░░░  ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║
        ░░░╚═╝░░░░░░╚═╝░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
        """, "red")) 
        
        print(colored("ERROR, click enter to restart program", "red"))
    
        

        input()
        continue     