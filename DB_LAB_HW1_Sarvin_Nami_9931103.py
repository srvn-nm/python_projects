import mysql.connector as mysql


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "rootSarvin1372",
    db = "school"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE school")

cursor.execute("DROP TABLE IF EXISTS Student")
cursor.execute("DROP TABLE IF EXISTS Teacher")
cursor.execute("DROP TABLE IF EXISTS Course")
cursor.execute("DROP TABLE IF EXISTS Term")

cursor.execute("CREATE TABLE Student (s_name VARCHAR(255) not null, s_family  VARCHAR(255) not null, s_id INT NOT NULL UNIQUE, age INT not null , city VARCHAR(255) not null , s_field VARCHAR(255) not null, gender VARCHAR(255) NOT NULL, tavg INT DEFAULT 0, PRIMARY KEY(userID))")
