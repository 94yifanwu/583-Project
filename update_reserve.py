from os import replace
from re import I
import sqlite_utils
import config
import create_guest
from datetime import datetime
from capability6 import cap_6

def updateReserve():
    """Provides an interface to enter attributes to update a reserve to check-in
    and inserts info into the RESERVES table."""

    print("\nUpdate New Reserve")

    Room_Number = input("Enter Room Number: ")
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

    query = (
        "SELECT Room_Number FROM RESERVES WHERE Guest_Id = "
        + str(Guest_Id)
        + " AND Room_Number="
        + str(Room_Number)
    )

    reply = config.db.query(query)
    result = ""
    for row in reply:
        result = row["Room_Number"]

    if result == "":
        print("Room " + Room_Number + " is not reserved with " + First_Name)
        return

    now = datetime.now()

    config.db["RESERVES"].update(
        (Room_Number, Guest_Id), {"Date_Check_In": now.strftime("%Y/%m/%d %H:%M:%S")}
    )

    print("Room " + Room_Number + " check-in")

