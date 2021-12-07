# Main menu HotelX

import sqlite_utils
import config
import capability1
import capability2
import capability3
import capability4
import capability5
import capability6
import capability7
import capability8
import capability9

def mainMenu():
    print(
    "\n\nWelcome to Hotelx Management Software!\n"
    + "\n"
    + " \/    \/   ||||   ||||||  \/\/\    \/    \/     // \n"
    + " ||    ||   ////     ||    \/       ||     \/   // \n"
    + " ||====||   |  |     ||    /////    ||      \/ // \n"
    + " ||    ||   \/\/     ||    \/       ||      // \/ \n"
    + " ||    ||   ||||     ||    \/\/\    \/\/\  //   \/ \n"
    + " ___________________________________________________"
    )
    begin = input("\nPress Enter to begin.....\n")
    if begin == "":
        while True:
            print("\nMain Menu")
            selection = input(
                "\nEnter the number of your selection to continue\n"
                + "1. Show status of all rooms\n"
                + "2. Show 7 day status of specific rooms\n"
                + "3. Show all current reservations\n"
                + "4. Housekeeping management\n"
                + "5. Show guest profile\n"
                + "6. Stay information for specific guest\n"
                + "7. Search guests\n"
                + "8. Generate daily report\n"
                + "9. Customer reservation screen\n"
                + "Enter \"quit\"  at any time to exit program.\n"
            )
            if selection == "1":
                capability1.cap_1()
            elif selection == "2":
                capability2.cap_2()
            elif selection == "3":
                capability3.cap_3(0)
            elif selection == "4":
                capability4.cap_4()
            elif selection == "5":
                guestId = input("\nEnter the guest's id number: ")
                capability5.cap_5(guestId)
            elif selection == "6":
                guestId = input("\nEnter the guest's id: ")
                roomNo = input("\nEnter the room number: ")
                capability6.cap_6(guestId, roomNo, False)
            elif selection == "7":
                capability7.cap_7()
            elif selection == "8":
                capability8.cap_8()
            elif selection == "9":
                capability9.cap_9()
            elif selection == "quit":
                quit()
            else:
                print(
                    "\nThat is not a valid selection."
                )
