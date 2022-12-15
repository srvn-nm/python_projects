import mysql.connector as mysql


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "rootSarvin1372",
    db = "school"
)
cursor = db.cursor()
# cursor.execute("CREATE DATABASE school")
cursor.execute("use school")

cursor.execute("DROP TABLE IF EXISTS Student")
cursor.execute("DROP TABLE IF EXISTS Teacher")
cursor.execute("DROP TABLE IF EXISTS Course")
cursor.execute("DROP TABLE IF EXISTS Term")

cursor.execute("CREATE TABLE Student (s_name VARCHAR(255) not NULL, s_family  VARCHAR(255) not NULL, s_id INT NOT NULL UNIQUE, age INT not NULL, city VARCHAR(255) not NULL , s_field VARCHAR(255) not NULL, gender VARCHAR(255) NOT NULL, tavg INT DEFAULT 0, PRIMARY KEY(s_id))")
cursor.execute("CREATE TABLE Teacher (t_name VARCHAR(255) not NULL, t_family  VARCHAR(255) not NULL, t_id INT NOT NULL UNIQUE, age INT not NULL, t_field VARCHAR(255) not NULL, salary INT DEFAULT 0, PRIMARY KEY(t_id))")
cursor.execute("CREATE TABLE Course (c_name VARCHAR(255) not NULL, dep  VARCHAR(255) not NULL, c_id INT NOT NULL UNIQUE, unit INT not NULL, c_field VARCHAR(255) not NULL, PRIMARY KEY(c_id))")
cursor.execute("CREATE TABLE Term (id INT UNIQUE not NULL, s_id INT NOT NULL, t_id INT NOT NULL, c_id INT NOT NULL, grade INT NOT NULL, term_no INT, PRIMARY KEY(id), FOREIGN KEY(s_id) REFERENCES Student(s_id), FOREIGN KEY(t_id) REFERENCES Teacher(t_id), FOREIGN KEY(c_id) REFERENCES Course(c_id))")
