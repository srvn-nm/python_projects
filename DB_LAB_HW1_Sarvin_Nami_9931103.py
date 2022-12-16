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

cursor.execute("DROP TABLE IF EXISTS Term")
cursor.execute("DROP TABLE IF EXISTS Student")
cursor.execute("DROP TABLE IF EXISTS Teacher")
cursor.execute("DROP TABLE IF EXISTS Course")

cursor.execute("CREATE TABLE Student (s_name VARCHAR(255) not NULL, s_family  VARCHAR(255) not NULL, s_id INT NOT NULL UNIQUE, age INT not NULL, city VARCHAR(255) not NULL , s_field VARCHAR(255) not NULL, gender VARCHAR(255) NOT NULL, tavg INT DEFAULT 0, PRIMARY KEY(s_id))")
cursor.execute("CREATE TABLE Teacher (t_name VARCHAR(255) not NULL, t_family  VARCHAR(255) not NULL, t_id INT NOT NULL UNIQUE, t_field VARCHAR(255) not NULL, salary INT DEFAULT 0, PRIMARY KEY(t_id))")
cursor.execute("CREATE TABLE Course (c_name VARCHAR(255) not NULL, dep  VARCHAR(255) not NULL, c_id INT NOT NULL UNIQUE, unit INT not NULL, c_field VARCHAR(255) not NULL, PRIMARY KEY(c_id))")
cursor.execute("CREATE TABLE Term (id INT UNIQUE not NULL, s_id INT NOT NULL, t_id INT NOT NULL, c_id INT NOT NULL, grade INT NOT NULL, term_no INT, PRIMARY KEY(id), FOREIGN KEY(s_id) REFERENCES Student(s_id), FOREIGN KEY(t_id) REFERENCES Teacher(t_id), FOREIGN KEY(c_id) REFERENCES Course(c_id))")

def student_add(s_name, s_family, s_id, age, city, s_field, gender, tavg):
    try:
        Q1 ="INSERT INTO Student (s_name, s_family, s_id, age, city, s_field, gender, tavg) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (s_name, s_family, s_id, age, city, s_field, gender, tavg)
        cursor.execute(Q1, values)
        db.commit()
    except Exception as e:
        print(e)
        
        
def teacher_add(t_name, t_family, t_id, t_field, salary):
    try:
        Q1 ="INSERT INTO Teacher (t_name, t_family, t_id, t_field, salary) VALUES(%s, %s, %s, %s, %s, %s)"
        values = (t_name, t_family, t_id, t_field, salary)
        cursor.execute(Q1, values)
        db.commit()
    except Exception as e:
        print(e)        
        

def course_add(c_name, dep, c_id, unit, c_field):
    try:
        Q1 ="INSERT INTO Course (c_name, dep, c_id, unit, c_field) VALUES(%s, %s, %s, %s, %s)"
        values = (c_name, dep, c_id, unit, c_field)
        cursor.execute(Q1, values)
        db.commit()
    except Exception as e:
        print(e)


def Term_add(id, s_id, t_id, c_id, grade, term_no):
    try:
        Q1 ="INSERT INTO Term (id, s_id, t_id, c_id, grade, term_no) VALUES(%s, %s, %s, %s, %s, %s)"
        values = (id, s_id, t_id, c_id, grade, term_no)
        cursor.execute(Q1, values)
        db.commit()
    except Exception as e:
        print(e) 


student_add("danial", "jahed", 1, 23, "mashhad", "software", "m", 18.26)
student_add("ahmad", "ghadirzadeh", 2, 23, "mashhad", "software", "m", 17.36)
student_add("mahsa", "ghanad", 3, 20, "shiraz", "hardware", "f", 15.13)
student_add("hasan", "attari", 4, 22, "esfahan", "electricity", "m", 12.43)
student_add("elham", "sadeghi", 5, 18, "rasht", "industry", "f", 16.25)
student_add("fatemeh", "khosravi", 6, 19, "zanjan", "it", "f", 18.46)
student_add("saeed", "yazdanian", 7, 26, "tahran", "software", "m", 19.16)
student_add("sajjad", "aemmi", 8, 23, "mashhad", "software", "m", 16.89)
student_add("alireza", "shahidi", 9, 21, "tehran", "it", "m", 9.75)
student_add("negar", "kamali", 10, 20, "mashhad", "software", "f", 15.25)
student_add("ali", "gandomi", 11, 23, "tehran", "hardware", "m", 17.16)
student_add("nafiseh", "hoseini", 12, 19, "esfahan", "construction", "f", 15.65)
student_add("mahdi", "alizadeh", 13, 24, "bushehr", "industry", "m", 11.16)
student_add("mahmood", "mohammadiyan", 14, 23, "tabas", "software", "m", 16.36)
student_add("mehrnaz", "mohammadzadeh", 15, 24, "tehran", "construction", "f", 11.36)


teacher_add("javad", "hamidzadeh", 1, "computer", 3300000)
teacher_add("khalil", "mafi", 2, "electricity", 5000000)
teacher_add("javad", "yazdanjo", 3, "computer", 1000000)
teacher_add("aminfarid", "aminian", 4, "computer", 2500000)
teacher_add("hashem", "etemadzadeh", 5, "math", 2300000)
teacher_add("saeed", "yazdanian", 6, "computer", 1500000)
teacher_add("amir", "bavafa", 7, "computer", 2500000)
teacher_add("ali", "haerian", 8, "industry", 6000000)
teacher_add("amirmasoud", "aminian", 9, "electricity", 2500000)
teacher_add("abas", "golmakani", 10, "electricity", 2300000)