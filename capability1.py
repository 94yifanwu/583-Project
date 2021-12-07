import config
import sqlite_utils
import sqlite3
import datetime

def cap_1():
    print("\nPrinting xxxxxxx ...\n")

    # rooms = config.db["TABLE"].rows_where("Status='Available'")
    # for row in rooms:
    #     print("Room_Number: " + str(row["Room_Number"]))
    #     print("Type: " + str(row["Type"]))
    #     print("Status: " + str(row["Status"]) + "\n")

    selection = input(
        "Enter the number of your selection to continue\n"
        + "1. xxxxxxxx\n"
        + 'Enter "quit"  at any time to exit program.\n'
    )
    if selection == "quit":
        return
    else:
        if selection == "1":
            #create_reserve.createReserve()
            print("1")