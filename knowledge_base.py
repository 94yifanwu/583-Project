import config
import sqlite_utils
import sqlite3

def kb(your_age,your_genres,your_language):
    print("\nrecommending movie: ...")

    if(your_age == "18"):
        print("recommending movie: Toy Story")
    elif(your_age == "19"):
        print("recommending movie: Grumpier Old Men")
    elif(your_age == "20"):
        print("recommending movie: Waiting to Exhale")
    elif(your_age == "21"):
        print("recommending movie: Father of the Bride Part II")
