import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "rootSarvin1372"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE datacamp")

cursor.execute("CREATE TABLE users (uname VARCHAR(255), ulname  VARCHAR(255), uID Int, phone VARCHAR(255), email VARCHAR(255), upassword VARCHAR(255), useccheck VARCHAR(255), time VARCHAR(255), limited_login Int, limited_password Int")
cursor.execute("CREATE TABLE friends (u1ID Int, u2ID Int, fID Int")
cursor.execute("CREATE TABLE blocked (blockerID Int, blockedID Int, bID Int, time VARCHAR(255)")
cursor.execute("CREATE TABLE request (u1ID Int, u2ID Int, fID Int, bID Int, friendship smallint, message smallint, block smallint")
cursor.execute("CREATE TABLE messages (sID Int, rID Int, time VARCHAR(255), text VARCHAR(255), seen smallint, like smallint")
cursor.execute("CREATE TABLE log_login (uID Int, useccheck VARCHAR(255), loginAttempts Int, time VARCHAR(255)")
cursor.execute("CREATE TABLE log_passwordChange (uID Int, useccheck VARCHAR(255), time VARCHAR(255), newPass VARCHAR(255)")