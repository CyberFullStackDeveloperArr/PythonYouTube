from pytube import YouTube
import time
import random
from colorama import init, Fore, Style
import re
import os


init()
init(autoreset=True)

def print_rainbow(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for char in text:
        color = random.choice(colors)
        print(color + char, end='', flush=True)
        time.sleep(0.01)
    print()


os.system('cls' if os.name == 'nt' else 'clear')

print_rainbow("""
╔═╗┬ ┬┌─┐┌─┐┌┬┐  ╔═╗┌─┐┌┬┐┌─┐  ╔╗╔┬┌─┐┬ ┬┌┬┐
║ ╦├─┤│ │└─┐ │   ║  │ │ ││├┤   ║║║││ ┬├─┤ │ 
╚═╝┴ ┴└─┘└─┘ ┴   ╚═╝└─┘─┴┘└─┘  ╝╚╝┴└─┘┴ ┴ ┴                                                                                                                                                                                        
""")

time.sleep(3)

url = input(Fore.GREEN + Style.BRIGHT + "Masukkan Link YouTobe Anda: " + Fore.BLUE)


if not re.search(r"youtu\.be", url):
    print(Fore.RED + "Maaf, Link Anda Tidak Sesuai!")

else: 
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    print (Fore.YELLOW + "Sedang Di Proses.....", end='', flush=True)
    video.download()
    print("\n" + Fore.GREEN + "Video berhasil diunduh!")
