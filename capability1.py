import sqlite_utils
import config

from capability6 import cap_6

def cap_1():
    """Shows ALL rooms and current status"""

    while True:
        print('\nRooms\n')
        rooms = config.db["ROOM"].rows_where(select='Room_Number,Type,Status')
        displayRooms(rooms)

        room_num = input(
            "\nPlease enter a room number or 'quit' to return to main menu: "
        )
        if room_num == "quit":
            return
        else:
            # Get Room Number selection
            room = config.db["ROOM"].get(room_num)

            # is Room available? -> call cap_6 to enter guest information
            #    - Set room to occupied after check in of guest.
            if room["Status"] == "Available":
                # Guest_Id will be passed as 0
                return cap_6('0', room_num, False)

            # is Room occupied? -> call cap_6 to modify
            #    - if guest checks out -> change room to unavailable/dirty
            elif room["Status"] == "Unavailable/Occupied":
                stays = config.db["STAYS_IN"].rows_where("Room_Number = :roomNo", {"roomNo": room_num})
                guest_id = next(stays)["Guest_Id"]
                return cap_6(guest_id, room_num, False)

            # is Room dirty? -> Warn user "room is dirty", ask if user
            #    - wants to change room to available? if 'no' no action
            elif room["Status"] == "Unavailable/Dirty":
                selection = input(
                    f"\nWARNING: Room {room_num} is dirty."
                    "\nDo you want to update status to Available?(y/n): "
                )
                if selection == "y":
                    config.db["ROOM"].update(room_num, {"Status": "Available"})
                    config.db["ROOM"].update(room_num, {"Bathroom": True})
                    config.db["ROOM"].update(room_num, {"Towels": True})
                    config.db["ROOM"].update(room_num, {"Bed_Sheets": True})
                    config.db["ROOM"].update(room_num, {"Dusting": True})
                    config.db["ROOM"].update(room_num, {"Vacuum": True})
                    config.db["ROOM"].update(room_num, {"Electronics": True})

            # is Room in maintenance? -> ask user if they want to change to
            #    - available? if 'no' no action
            elif room["Status"] == "Unavailable/Maintenance":
                selection = input(
                    f"\nWARNING: Room {room_num} is currently in maintenance."
                    "\nDo you want to update status to Available?(y/n): "
                )
                if selection == "y":
                    config.db["ROOM"].update(room_num, {"Status": "Available"})
                    config.db["ROOM"].update(room_num, {"Bathroom": True})
                    config.db["ROOM"].update(room_num, {"Towels": True})
                    config.db["ROOM"].update(room_num, {"Bed_Sheets": True})
                    config.db["ROOM"].update(room_num, {"Dusting": True})
                    config.db["ROOM"].update(room_num, {"Vacuum": True})
                    config.db["ROOM"].update(room_num, {"Electronics": True})

def displayRooms(rooms):
    print("Room Number\tType\tStatus")
    for row in rooms:
        roomNo = row["Room_Number"]
        type = row["Type"]
        status = row["Status"]
        print(f"{roomNo}\t\t{type}\t{status}")
