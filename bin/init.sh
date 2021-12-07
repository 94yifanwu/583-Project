# Remove previously initialized database file
rm ./dbFiles/hotel.db

# Create schema
sqlite3 < ./bin/dbInit.sql

# Add rows
sqlite-utils insert ./dbFiles/hotel.db HOUSEKEEP --csv ./csvFiles/housekeep.csv
sqlite-utils insert ./dbFiles/hotel.db ROOM --csv ./csvFiles/room.csv
sqlite-utils insert ./dbFiles/hotel.db GUEST --csv ./csvFiles/guest.csv
sqlite-utils insert ./dbFiles/hotel.db CLEANS --csv ./csvFiles/cleans.csv
sqlite-utils insert ./dbFiles/hotel.db RESERVES --csv ./csvFiles/reserves.csv
sqlite-utils insert ./dbFiles/hotel.db STAYS_IN --csv ./csvFiles/stays_in.csv
