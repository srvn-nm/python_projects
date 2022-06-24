import mysql.connector as mysql
from datetime import datetime

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "rootSarvin1372"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE datacamp")

cursor.execute("CREATE TABLE users (uname VARCHAR(255) not null, ulname  VARCHAR(255) not null, uID Int NOT NULL unique PRIMARY KEY, phone VARCHAR(255) not null unique, email VARCHAR(255) not null unique, upassword VARCHAR(255) not null, useccheck VARCHAR(255) not null unique, time VARCHAR(255) not null, limited_login Int default='0', limited_password Int default='0'")
cursor.execute("CREATE TABLE friends (u1ID Int, u2ID Int, fID Int NOT NULL AUTO_INCREMENT PRIMARY KEY, FOREIGN KEY(u1ID, u2ID) REFERENCES Users(uID, uID)")
cursor.execute("CREATE TABLE blocked (blockerID Int, blockedID Int, bID Int NOT NULL AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), FOREIGN KEY(blockerID, blockedID) REFERENCES Users(uID, uID)")
cursor.execute("CREATE TABLE request (u1ID Int, u2ID Int, fID Int, bID Int, friendship smallint, message smallint, block smallint, iID Int NOT NULL AUTO_INCREMENT PRIMARY KEY, FOREIGN KEY(u1ID, u2ID) REFERENCES Users(uID, uID), FOREIGN KEY(fID) REFERENCES friends(fID), FOREIGN KEY(bID) REFERENCES blocked(bID)")
cursor.execute("CREATE TABLE messages (sID Int, rID Int, time VARCHAR(255), text VARCHAR(255), seen smallint, like smallint, mID Int NOT NULL AUTO_INCREMENT PRIMARY KEY, FOREIGN KEY(sID, rID) REFERENCES Users(uID, uID)")
cursor.execute("CREATE TABLE log_login (uID Int, useccheck VARCHAR(255), loginAttempts Int, time VARCHAR(255), FOREIGN KEY(uID, useccheck) REFERENCES Users(uID, useccheck)")
cursor.execute("CREATE TABLE log_passwordChange (uID Int, useccheck VARCHAR(255), time VARCHAR(255), newPass VARCHAR(255), FOREIGN KEY(uID, useccheck) REFERENCES Users(uID, useccheck)")

def register(name, lname, ID, phoneNo, gmail, password):
    while not password.isalpha():
        print("Password should have alphabets, too!\ntry again:\n")
        password = input()
    while phoneNo.isalpha():
        print("phone should not have alphabets!\ntry again:\n")
        phoneNo = input()
    while name.isnumeric():
        print("Name should have alphabets!\ntry again:\n")
        name = input()
    while lname.isnumeric():
        print("Last name should have alphabets!\ntry again:\n")
        lname = input()
    while gmail.isnumeric() or not gmail.endwith("@gmail.com"):
        print("Email should be a valid gmail address!\ntry again:\n")
        gmail = input()
    current_time = datetime.now().strftime("%H:%M:%S")
    seccheck = input("what is your favorite color?")
    Q1 ="""
    INSERT INTO users (uname, ulname, uID, phone, email, upassword, useccheck, time)
    VALUES(name, lname, ID, phoneNo, email, password, seccheck, current_time)
    """
    with db.cursor() as cursor:
    cursor.execute(Q1)
    db.commit()
    menu()
    
def Login():
    username = input("type your username here:")
    password = input("type your password here or if you don't remember it just type 0:")
    if password == 0:
        seccheck = input("what was youe answer to security question?")
    menu()