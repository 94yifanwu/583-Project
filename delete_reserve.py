from os import replace
from re import I
import sqlite_utils
import config


def deleteReserve():
    """Provides an interface to enter attributes to delete a reserve"""

    print("\nDelete Room Reserve")

    Room_Number = input("Enter Room Number: ")
    query = "SELECT Room_Number FROM RESERVES WHERE Room_Number = '" + Room_Number + "'"

    reply = config.db.query(query)
    Room_Number = ""

    for row in reply:
        Room_Number = row["Room_Number"]

    if Room_Number == "":
        print("Room_Number not found")
        return

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
        print("Guest not found")
        return

    config.db["RESERVES"].delete((Room_Number, Guest_Id))
    config.db["ROOM"].update(Room_Number, {"Status": "Available"})

    print("Room_Number " + str(Room_Number) + " deleted")

    return ""
