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

cursor.execute("CREATE TABLE Student (s_name VARCHAR(255) not null, s_family  VARCHAR(255) not null, s_id INT NOT NULL UNIQUE, age INT not null , city VARCHAR(255) not null , s_field VARCHAR(255) not null, gender VARCHAR(255) NOT NULL, tavg INT DEFAULT 0, PRIMARY KEY(s_id))")
cursor.execute("CREATE TABLE Teacher (t_name VARCHAR(255) not null, t_family  VARCHAR(255) not null, t_id INT NOT NULL UNIQUE, age INT not null , t_field VARCHAR(255) not null, salary INT DEFAULT 0, PRIMARY KEY(t_id))")
cursor.execute("CREATE TABLE Course (c_name VARCHAR(255) not null, dep  VARCHAR(255) not null, c# INT NOT NULL UNIQUE, unit INT not null , c_field VARCHAR(255) not null, PRIMARY KEY(c#))")
cursor.execute("CREATE TABLE Term (s_name VARCHAR(255) not null, s_family  VARCHAR(255) not null, s_id INT NOT NULL UNIQUE, age INT not null , city VARCHAR(255) not null , s_field VARCHAR(255) not null, gender VARCHAR(255) NOT NULL, tavg INT DEFAULT 0, PRIMARY KEY(s_id))")
