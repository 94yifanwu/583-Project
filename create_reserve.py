from os import replace
from re import I
import sqlite_utils
import config
import create_guest
from datetime import datetime


def createReserve():
    """Provides an interface to enter attributes to create new reserve
    and inserts info into the RESERVES table."""

    print("\nCreating New Reserve")

    First_Name = input("Enter First Name: ")
    Last_Name = input("Enter Last Name: ")

    query = (
        "SELECT Guest_Id FROM GUEST WHERE First_Name = '"
        + First_Name
        + "' AND Last_Name = '"
        + Last_Name
        + "'"
    )

    reply = config.db.query(query)
    Guest_Id = ""

    for row in reply:
        Guest_Id = row["Guest_Id"]

    if Guest_Id == "":
        create_guest.createGuest()

    Room_Number = input("Enter Room Number: ")
    ROOM_Type = input("Enter Room Type: ")
    Daily_Rate = input("Enter Daily Rate: ")
    Website_Reservation_Made = input("Enter Website Reservation Made: ")

    now = datetime.now()

    # Format attributes as JSON.
    newReserve = {
        "Room_Number": Room_Number,
        "Guest_Id": Guest_Id,
        "Date_Made": now.strftime("%Y/%m/%d %H:%M:%S"),
        "Website_Reservation_Made": Website_Reservation_Made,
        "Daily_Rate": Daily_Rate,
    }

    config.db["RESERVES"].insert(newReserve)
    config.db["ROOM"].update(Room_Number, {"Status": "Unavailable/Occupied"})
    print("Room_Number reserved")

    return
