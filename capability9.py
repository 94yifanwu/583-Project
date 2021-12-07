import config
import sqlite_utils
import sqlite3
import datetime
import capability3
import create_reserve

# Once the available rooms are displayed to the User,
# the User shall be able to select a room and enter
# in their information to make a reservation.
# The User shall then be able to submit the reservation request.
# When the information is submitted, the information shall be
# transferred to Capability 3 and a reservation is made.


def cap_9():
    """Shows ALL available rooms"""
    print("\nPrinting all available rooms...\n")

    rooms = config.db["ROOM"].rows_where("Status='Available'")
    for row in rooms:
        print("Room_Number: " + str(row["Room_Number"]))
        print("Type: " + str(row["Type"]))
        print("Status: " + str(row["Status"]) + "\n")

    selection = input(
        "Enter the number of your selection to continue\n"
        + "1. Add Reservation\n"
        + 'Enter "quit"  at any time to exit program.\n'
    )
    if selection == "quit":
        return
    else:
        if selection == "1":
            #create_reserve.createReserve()
            capability3.createReservation(0)
