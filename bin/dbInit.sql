--Create and open db file
.open dbFiles/hotel.db

--Create tables
CREATE TABLE HOUSEKEEP(
  Housekeep_Id INT,
  First_Name VARCHAR,
  Last_Name VARCHAR,
  PRIMARY KEY (Housekeep_Id)
);

CREATE TABLE ROOM(
  Room_Number INT,
  Type TEXT CHECK( Type IN ('K', 'DQ', 'DBK', 'S')),
  Status TEXT CHECK( Status IN ('Available', 'Unavailable/Occupied',
    'Unavailable/Dirty', 'Unavailable/Maintenance')),
  Bathroom BOOLEAN,
  Towels BOOLEAN,
  Bed_Sheets BOOLEAN,
  Dusting BOOLEAN,
  Vacuum BOOLEAN,
  Electronics BOOLEAN,
  PRIMARY KEY (Room_Number)
);

CREATE TABLE GUEST(
  Guest_Id INT,
  First_Name VARCHAR,
  Last_Name VARCHAR,
  Phone CHAR(10),
  Vehicle_License_Plate CHAR(7),
  Email VARCHAR,
  Id_State CHAR(2),
  Id_Number VARCHAR,
  Street_Address VARCHAR,
  City VARCHAR,
  Zip_Code CHAR(5),
  State CHAR(2),
  PRIMARY KEY (Guest_Id)
);

CREATE TABLE CLEANS(
  Room_Number INT,
  Housekeep_Id INT,
  PRIMARY KEY (Room_Number, Housekeep_Id),
  FOREIGN KEY (Room_Number) REFERENCES ROOM(Room_Number),
  FOREIGN KEY (Housekeep_Id) REFERENCES HOUSEKEEP(Housekeep_Id)
);

CREATE TABLE RESERVES(
  Room_Number INT,
  Guest_Id INT,
  Date_Made DATE,
  Date_Check_In DATE,
  Date_Check_Out DATE,
  Website_Reservation_Made BOOLEAN,
  --Room_Type TEXT AS (SELECT Type FROM ROOM
                  --WHERE RESERVES.Room_Number = ROOM.Room_Number),
  Daily_Rate FLOAT(5, 2), --AS
    --IIF( (Room_Type = 'K'), 95.0,
      --IFF( (Room_Type = 'DQ'), 120.0,
        --IIF( (Room_Type = 'DBK'), 160.0, 200.0))),
  Total_Charge FLOAT(9, 2) AS ((JULIANDAY(Date_Check_Out) - JULIANDAY(Date_Check_In))
                                * Daily_Rate),
  PRIMARY KEY (Room_Number, Guest_Id),
  FOREIGN KEY (Room_Number) REFERENCES ROOM(Room_Number),
  FOREIGN KEY (Guest_Id) REFERENCES GUEST(Guest_Id)
);

CREATE TABLE STAYS_IN(
  Room_Number INT,
  Guest_Id INT,
  Check_In TIMESTAMP,
  Expected_Check_Out TIMESTAMP,
  Daily_Rate FLOAT(7, 2),
  Total_Charge FLOAT(9, 2) AS ((JULIANDAY(Expected_Check_Out)
    - JULIANDAY(Check_In)) * Daily_Rate),
  Payments_Made FLOAT(9, 2),
  Balance FLOAT(9, 2) AS (Total_Charge - Payments_Made),
  PRIMARY KEY (Room_Number, Guest_Id),
  FOREIGN KEY (Room_Number) REFERENCES ROOM(Room_Number),
  FOREIGN KEY (Guest_Id) REFERENCES GUEST(Guest_Id)
);
