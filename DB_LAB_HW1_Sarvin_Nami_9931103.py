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

cursor.execute("CREATE TABLE Student (s_name VARCHAR(255) not NULL, s_family  VARCHAR(255) not NULL, s_id INT NOT NULL UNIQUE, age INT not NULL, city VARCHAR(255) not NULL , s_field VARCHAR(255) not NULL, gender VARCHAR(255) NOT NULL, tavg DOUBLE, PRIMARY KEY(s_id))")
cursor.execute("CREATE TABLE Teacher (t_name VARCHAR(255) not NULL, t_family  VARCHAR(255) not NULL, t_id INT NOT NULL UNIQUE, t_field VARCHAR(255) not NULL, salary INT DEFAULT 0, PRIMARY KEY(t_id))")
cursor.execute("CREATE TABLE Course (c_name VARCHAR(255) not NULL, dep  VARCHAR(255) not NULL, c_id INT NOT NULL UNIQUE, unit INT not NULL, c_field VARCHAR(255) not NULL, PRIMARY KEY(c_id))")
cursor.execute("CREATE TABLE Term (id INT UNIQUE not NULL, s_id INT NOT NULL, t_id INT NOT NULL, c_id INT NOT NULL, grade DOUBLE NOT NULL, term_no INT, PRIMARY KEY(id), FOREIGN KEY(s_id) REFERENCES Student(s_id), FOREIGN KEY(t_id) REFERENCES Teacher(t_id), FOREIGN KEY(c_id) REFERENCES Course(c_id))")

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
        Q1 ="INSERT INTO Teacher (t_name, t_family, t_id, t_field, salary) VALUES(%s, %s, %s, %s, %s)"
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


def term_add(id, s_id, t_id, c_id, grade, term_no):
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


course_add("mathematical", "computer", 1, 3, "electricity")
course_add("electrical circuits", "computer", 2, 3, "electricity")
course_add("logic circuits", "computer", 3, 3, "computer")
course_add("data structure", "computer", 4, 3, "computer")
course_add("android programming", "computer", 5, 3, "computer")
course_add("computer architecture", "computer", 6, 3, "computer")
course_add("electronic", "electricity", 7, 3, "electricity")
course_add("soil", "construction", 8, 3, "construction")
course_add("lab database", "computer", 9, 1, "computer")
course_add("enghelab", "elahiat", 10, 2, "elahiat")
course_add("mathematical", "computer", 11, 3, "electricity")


term_add(1, 2, 1, 1, 20, 8)
term_add(2, 8, 7, 7, 18, 4)
term_add(3, 14, 3, 6, 18, 6)
term_add(4, 8, 5, 2, 1.5, 3)
term_add(5, 4, 2, 3, 15, 6)
term_add(6, 11, 6, 4, 19, 5)
term_add(7, 15, 10, 9, 9, 3)
term_add(8, 10, 5, 11, 1, 4)
term_add(9, 3, 3, 6, 20, 5)
term_add(10, 2, 4, 10, 20, 4)
term_add(11, 10, 6, 2, 8, 3)
term_add(12, 5, 8, 4, 9.25, 6)
term_add(13, 8, 5, 6, 8.75, 6)
term_add(14, 15, 2, 2, 16, 4)
term_add(15, 14, 3, 7, 15, 7)


print("-----------------------------------------------------------------------")
Q1 = "SELECT s_id, s_name FROM Student WHERE ((s_name LIKE 'a%' or s_name LIKE '%a') and (tavg >= 17))"
cursor.execute(Q1)
records = cursor.fetchall()
print("Total number of rows in table of query 1: ", cursor.rowcount)
print("\nPrinting each row")
for row in records:
    print("Id = ", row[0], )
    print("Name = ", row[1], "\n\n****\n")
    
    
print("-----------------------------------------------------------------------")
Q2 = "SELECT t_id, t_name FROM Teacher WHERE (t_name LIKE 'j%')ORDER BY t_id DESC" 
cursor.execute(Q2)
records = cursor.fetchall()
print("Total number of rows in table of query 2: ", cursor.rowcount)
print("\nPrinting each row")
for row in records:
    print("Id = ", row[0], )
    print("Name = ", row[1], "\n\n****\n")
    
    
print("-----------------------------------------------------------------------")
Q3 = "UPDATE Student SET tavg = tavg + 1 WHERE ((city LIKE 'z%') and (city LIKE '%n'))"
cursor.execute(Q3)
db.commit()
cursor.execute("SELECT s_id, s_name, city, tavg FROM Student WHERE ((city LIKE 'z%') and (city LIKE '%n'))")
records = cursor.fetchall()
print("Total number of rows in table of query 3: ", cursor.rowcount)
print("\nPrinting each row")
for row in records:
    print("Id = ", row[0], )
    print("Name = ", row[1])
    print("City = ", row[2])
    print("Average = ", row[3], "\n\n****\n")
    
    
print("-----------------------------------------------------------------------")
cursor.execute("SELECT COUNT(*) FROM Student WHERE (age > 20) ORDER BY age")
count = cursor.fetchone()
Q4 = "SELECT * FROM Student WHERE (age > 20) ORDER BY age LIMIT %s"
cursor.execute(Q4,(int(count[0]/5),))
records = cursor.fetchall()
print("Total number of rows in table of query 4: ", cursor.rowcount)
db.commit()
print("\nPrinting each row")
for row in records:
    print("Id = ", row[0], )
    print("Name = ", row[1])
    print("City = ", row[2])
    print("Average = ", row[3], "\n\n****\n")
    
    
print("-----------------------------------------------------------------------")
Q5 = "UPDATE Teacher SET t_field = 'electricity' WHERE (t_name = 'javad' and t_family = 'hamidzadeh')"
cursor.execute(Q5)
cursor.execute("SELECT * FROM Teacher WHERE t_name = 'javad' and t_family = 'hamidzadeh'")
records = cursor.fetchall()
print("Total number of rows in table of query 5: ", cursor.rowcount)
db.commit()
print("\nPrinting each row")
for row in records:
    print(row, "\n\n****\n")
    
    
print("-----------------------------------------------------------------------")
Q6 = "SELECT Student.s_name AS name, Student.s_family AS family FROM Student INNER JOIN term ON (Term.term_no = 3 and Student.age > 20 and Term.s_id = Student.s_id)"
cursor.execute(Q6)
records = cursor.fetchall()
print("Total number of rows in table of query 6: ", cursor.rowcount)
db.commit()
print("\nPrinting each row")
for row in records:
    print("Name = ", row[0], )
    print("Family = ", row[1], "\n\n****\n")
    
print("-----------------------------------------------------------------------")
Q7 = "SELECT Student.s_name AS name FROM Student INNER JOIN term ON (Term.term_no <= 3 and Term.term_no >= 1 and Student.gender = 'm' and Term.s_id = Student.s_id and Student.tavg >= 18)"
cursor.execute(Q7)
records = cursor.fetchall()
print("Total number of rows in table of query 7: ", cursor.rowcount)
db.commit()
print("\nPrinting each row")
for row in records:
    print("Name = ", row[0], "\n\n****\n")
    
    
print("-----------------------------------------------------------------------")
Q8 = "SELECT * FROM Teacher WHERE (salary >= 5000000 or t_field != 'computer')ORDER BY t_id DESC"
cursor.execute(Q8)
records = cursor.fetchall()
print("Total number of rows in table of query 8: ", cursor.rowcount)
db.commit()
print("\nPrinting each row")
for row in records:
    print(row, "\n\n****\n")