# Main menu Movie Recommend

import sqlite_utils
import config
import capability1

def mainMenu():
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
    begin = ""
    if begin == "":
        while True:
            print("\nMain Menu")
            selection = input(
                "\nEnter the number of your selection to continue\n"
                + "1. xxxxxx\n"
                + "2. xxxxxx\n"
                + "3. xxxxxx\n"
                + "Enter \"quit\"  at any time to exit program.\n"
            )
            if selection == "1":
                capability1.cap_1()
            elif selection == "quit":
                quit()
            else:
                print(
                    "\nThat is not a valid selection."
                )
