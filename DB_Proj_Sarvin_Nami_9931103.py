import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "rootSarvin1372"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE datacamp")

cursor.execute("CREATE TABLE users (uname VARCHAR(255), ulname  VARCHAR(255), uID VARCHAR(255)), phone VARCHAR(255), email VARCHAR(255), upassword VARCHAR(255), useccheck VARCHAR(255), time VARCHAR(255), limited_login Int, limited_password Int")
