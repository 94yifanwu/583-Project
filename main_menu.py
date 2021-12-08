# Main menu Movie Recommend

import sqlite_utils
import config
import capability1

def mainMenu():
    # from here https://manytools.org/hacker-tools/ascii-banner/
    print(
    """
███╗   ███╗ ██████╗ ██╗   ██╗██╗███████╗    ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ███╗███╗   ███╗███████╗███╗   ██╗██████╗ 
████╗ ████║██╔═══██╗██║   ██║██║██╔════╝    ██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗ ████║████╗ ████║██╔════╝████╗  ██║██╔══██╗
██╔████╔██║██║   ██║██║   ██║██║█████╗      ██████╔╝█████╗  ██║     ██║   ██║██╔████╔██║██╔████╔██║█████╗  ██╔██╗ ██║██║  ██║
██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██║██╔══╝      ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║  ██║
██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ██║███████╗    ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║ ╚████║██████╔╝
╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ 
    """
    )
    while True:
        print("\n-------------Main Menu-------------\n")
        print("Please enter the information: ")
        your_age = input("Enter your age: ")
        your_genres = input("Enter your genres: ")
        your_language = input("Enter your language: ")
        capability1.cap_1(your_age,your_genres,your_language)
        
