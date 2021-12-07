import sqlite_utils

# Initializes global variables
def init():
    dbfile = "./dbFiles/hotel.db"
    global db
    db = sqlite_utils.Database(dbfile)
