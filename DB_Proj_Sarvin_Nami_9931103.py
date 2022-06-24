import random
import textwrap
import mysql.connector as mysql
from datetime import datetime
import smtplib

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "rootSarvin1372"
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE datacamp")

cursor.execute("CREATE TABLE users (uname VARCHAR(255) not null, ulname  VARCHAR(255) not null, uID Int NOT NULL unique PRIMARY KEY, phone VARCHAR(255) not null unique, email VARCHAR(255) not null unique, upassword VARCHAR(255) not null, useccheck VARCHAR(255) not null unique, time VARCHAR(255) not null, log_in int default='0'")
cursor.execute("CREATE TABLE friends (u1ID Int, u2ID Int, fID Int NOT NULL AUTO_INCREMENT PRIMARY KEY, FOREIGN KEY(u1ID, u2ID) REFERENCES Users(uID, uID)")
cursor.execute("CREATE TABLE blocked (blockerID Int, blockedID Int, bID Int NOT NULL AUTO_INCREMENT PRIMARY KEY, time VARCHAR(255), FOREIGN KEY(blockerID, blockedID) REFERENCES Users(uID, uID)")
cursor.execute("CREATE TABLE request (u1ID Int, u2ID Int, fID Int, bID Int, friendship smallint, message smallint, block smallint, iID Int NOT NULL AUTO_INCREMENT PRIMARY KEY, FOREIGN KEY(u1ID, u2ID) REFERENCES Users(uID, uID), FOREIGN KEY(fID) REFERENCES friends(fID), FOREIGN KEY(bID) REFERENCES blocked(bID)")
cursor.execute("CREATE TABLE messages (sID Int, rID Int, time VARCHAR(255), text VARCHAR(255), seen smallint, like smallint, mID Int NOT NULL AUTO_INCREMENT PRIMARY KEY, FOREIGN KEY(sID, rID) REFERENCES Users(uID, uID)")
cursor.execute("CREATE TABLE log_login (uID Int, useccheck VARCHAR(255), loginAttempts Int default='0', time VARCHAR(255), newPass VARCHAR(255), FOREIGN KEY(uID, useccheck) REFERENCES Users(uID, useccheck)")
cursor.execute("CREATE TABLE log_wrongPassword (uID Int, useccheck VARCHAR(255), time VARCHAR(255), attempts Int default='0', FOREIGN KEY(uID, useccheck) REFERENCES Users(uID, useccheck)")
cursor.execute("CREATE TABLE limited_users (uID Int, time VARCHAR(255), FOREIGN KEY(uID) REFERENCES Users(uID)")

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
    Q1 =f"INSERT INTO users (uname, ulname, uID, phone, email, upassword, useccheck, time , log_in) VALUES({name}, {lname}, {ID}, {phoneNo}, {gmail}, {password}, {seccheck}, {current_time}, '1')"
    cursor.execute(Q1)
    db.commit()
    sendMail(gmail,"succsessfully registered!^-^",f"Hi {name}.\nYou are a member of our family now!<3")
    menu(ID)
    
def sendMail(TO,SUBJECT,TEXT):
    message = textwrap.dedent("""\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % ("snnn99554@gmail.com", ", ".join(TO), SUBJECT, TEXT))
    server = smtplib.SMTP('localhost')
    server.sendmail("snnn99554@gmail.com", TO, message)
    server.quit()

def passwordRecovery(username):
    questionCount = 0
    seccheck = input("what was your answer to security question? ")
    while cursor.execute("SELECT * from users WHERE uId = %s and useccheck = %s", (username, seccheck)) == None and questionCount < 5 :
        seccheck = input("what was your answer to security question?")
        print(f"login attempts = {questionCount}")
        questionCount += 1
    randomCode = random.randint(10000,100000)
    code_check = True
    reciever = str(cursor.execute('SELECT email FROM users WHERE uId = username'))
    while code_check and cursor.execute("SELECT * FROM users WHERE uId = %s and useccheck = %s", (username, seccheck)) == None and questionCount == 5 :
        sendMail(reciever, "login code", randomCode)
        entered_code = input("type the code we have sended to you here: ")
        if entered_code == randomCode:
            code_check = False
    user = cursor.fetchone()
    print(user)
    current_time = datetime.now().strftime("%H:%M:%S")
    Q2 = f"INSERT INTO log_login (uID, useccheck, loginAttempts, time) VALUES({username}, {seccheck}, {questionCount}, {current_time})"
    cursor.execute(Q2)
    db.commit()
    changePassword(username)
    new_password = str(cursor.execute('SELECT upassword FROM users WHERE uId = username'))
    update_query2 = f" UPDATE log_login SET newPass = {new_password} WHERE uId = {username}"
    cursor.execute(update_query2)
    db.commit()    

def wrongPassword(username):
    print("invalid inputs for login attempt!")
    if int(cursor.execute('SELECT attempts FROM log_wrongPassword WHERE uId = username')) + 1 < 3 :
        temp = int(cursor.execute('SELECT attempts FROM log_wrongPassword WHERE uId = username')) + 1
        update_query = f" UPDATE log_wrongPassword SET attempts = {temp} WHERE uId = {username}"
        cursor.execute(update_query)
        db.commit()
    else: 
        current_time = datetime.now().strftime("%H:%M:%S")
        Q4 = f"INSERT INTO limited_users (uID, time) VALUES({username}, {current_time})"
        cursor.execute(Q4)
        db.commit()
        
def login():
    username = input("type your username here: ")
    limited_query = f"SELECT uID From limited_users WHERE uID = {username}"
    limited_username = cursor.execute(limited_query)
    db.commit()
    login_query =f"SELECT uID FROM users WHERE log_in = '1' and uID = {username}"
    loggedin_username = cursor.execute(login_query)
    db.commit()
    if (not (username == limited_username)) and (not(username == loggedin_username)):
        password = input("type your password here or if you don't remember it just type 0:  ")
        if password == 0:
            passwordRecovery(username,)
        else:
            if str(cursor.execute('SELECT upassword FROM users WHERE uId = username')) == password:
                cursor.execute("SELECT * from users WHERE uId = %s and upassword = %s", (username, password))
                user = cursor.fetchone()
                print("Hello!\nWelcome Back!\n" + user)
                db.commit()
                print("Congratulations!\nYou successfully logged in!\n" + user)
                update_query = f" UPDATE users SET log_in = '1' WHERE uId = {username}"
                cursor.execute(update_query)
                db.commit()
                menu(username)
            else:
                wrongPassword(username)
    else:
        print("Sorry!\nYou can't login.>-<\n")

def changePassword(username):
    questionCount = 0
    seccheck = input("what was your answer to security question? ")
    while cursor.execute("SELECT * from users WHERE uId = %s and useccheck = %s", (username, seccheck)) == None and questionCount < 5 :
        seccheck = input("what was your answer to security question?")
        print(f"login attempts = {questionCount}")
        questionCount += 1
    randomCode = random.randint(10000,100000)
    code_check = True
    reciever = str(cursor.execute('SELECT email FROM users WHERE uId = username'))
    while code_check and cursor.execute("SELECT * FROM users WHERE uId = %s and useccheck = %s", (username, seccheck)) == None and questionCount == 5 :
        sendMail(reciever, "login code", randomCode)
        entered_code = input("type the code we have sended to you here: ")
        if entered_code == randomCode:
            code_check = False
    new_password = input("Enter your new password here: ")
    while not new_password.isalpha():
        print("Password should have alphabets, too!\ntry again:\n")
        new_password = input()
    update_query = f" UPDATE users SET upassword = {new_password} WHERE uId = {username}"
    cursor.execute(update_query)
    db.commit()

def firstMenu():
    print("Hello.Welcome here.Please enter the number of one of the choices below: ")
    choice = input("1)register for a new account\n2)login to an existing account")
    if choice == "1":
        register()
    if choice == "2":
        login()
        
def menu(username):
    choice = input("Hi.Type the number of the action you want to perform here:\n1)change password\n2)log out\n3)delete account\n4)")
    if choice == "1":
        changePassword(username)
    elif choice == "2":
        update_query = f" UPDATE users SET log_in = '0' WHERE uId = {username}"
        cursor.execute(update_query)
        db.commit()
        firstMenu()
    elif choice == "3":
        update_query = f" UPDATE users SET upassword = None SET uname = None and SET ulname = None and SET phone = None and SET email = None and SET useccheck = None and SET time = None and SET log_in = '0' WHERE uId = {username}"
        cursor.execute(update_query)
        db.commit()