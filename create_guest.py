import sqlite_utils
import config

def createGuest():
    """Provides an interface to enter attributes to create new user
     and inserts info into the GUESTS table. Returns new guest's new id,
     which will be unique."""

    print("\nCreating New Guest")
    #Gather new guest's attributes.
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number(digits only): ")
    streetAddress = input("Enter street address: ")
    city = input("Enter city: ")
    zipCode = input("Enter zip code: ")
    state = input("Enter state: ")
    idState = input("Enter state ID was issued in: ")
    idNumber = input("Enter ID Number: ")
    licensePlateNo = input("Enter license plate number: ")

    #Get the max id in GUEST and set the new guest's id to be one greater.
    query = "SELECT max(Guest_Id) FROM GUEST"
    reply = config.db.query(query)
    guestId = next(reply)["max(Guest_Id)"] + 1

    #Format attributes as JSON.
    newGuest = {
        "Guest_Id": guestId,
        "First_Name": firstName,
        "Last_Name": lastName,
        "Email": email,
        "Phone": phone,
        "Street_Address": streetAddress,
        "City": city,
        "Zip_Code": zipCode,
        "State": state,
        "Id_State": idState,
        "Id_Number": idNumber,
        "Vehicle_License_Plate": licensePlateNo
    }
    config.db["GUEST"].insert(newGuest)

    return  guestId
