import random
import textwrap
import mysql.connector as mysql
# import mysql as my
from datetime import datetime
import smtplib

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "rootSarvin1372",
    db = "datacamp"
)
cursor = db.cursor()
# cursor.execute("CREATE DATABASE datacamp")
cursor.execute("use datacamp")
cursor.execute("DROP TABLE IF EXISTS limited_users")
cursor.execute("DROP TABLE IF EXISTS log_wrongPassword")
cursor.execute("DROP TABLE IF EXISTS log_login")
cursor.execute("DROP TABLE IF EXISTS messages")
cursor.execute("DROP TABLE IF EXISTS request")
cursor.execute("DROP TABLE IF EXISTS blocked")
cursor.execute("DROP TABLE IF EXISTS friends")
cursor.execute("DROP TABLE IF EXISTS users")


# try:
cursor.execute("CREATE TABLE users (uname VARCHAR(255) not null, ulname  VARCHAR(255) not null, userID VARCHAR(255) NOT NULL UNIQUE, phone VARCHAR(255) not null unique, email VARCHAR(255) not null unique, upassword VARCHAR(255) not null, useccheck VARCHAR(255) UNIQUE NOT NULL, timing VARCHAR(255) not null, log_in INT DEFAULT 0, PRIMARY KEY(userID, useccheck))")
cursor.execute("CREATE TABLE friends (u1ID VARCHAR(255), u2ID VARCHAR(255), fID INT AUTO_INCREMENT PRIMARY KEY, FOREIGN KEY(u1ID) REFERENCES users(userID), FOREIGN KEY(u2ID) REFERENCES users(userID))")
cursor.execute("CREATE TABLE blocked (blockerID VARCHAR(255), blockedID VARCHAR(255), bID INT AUTO_INCREMENT PRIMARY KEY, timing VARCHAR(255), FOREIGN KEY(blockerID) REFERENCES users(userID), FOREIGN KEY(blockedID) REFERENCES users(userID))")
cursor.execute("CREATE TABLE request (u1ID VARCHAR(255), u2ID VARCHAR(255), fID INT, bID INT, friendship SMALLINT, message SMALLINT, block SMALLINT, iID INT AUTO_INCREMENT PRIMARY KEY, FOREIGN KEY(u1ID) REFERENCES users(userID), FOREIGN KEY(fID) REFERENCES friends(fID), FOREIGN KEY(bID) REFERENCES blocked(bID), FOREIGN KEY(u2ID) REFERENCES users(userID))")
cursor.execute("CREATE TABLE messages (sID VARCHAR(255), rID VARCHAR(255), timing VARCHAR(255), text VARCHAR(255), seen SMALLINT DEFAULT 0, liked SMALLINT DEFAULT 0, mID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, FOREIGN KEY(sID) REFERENCES users(userID), FOREIGN KEY(rID) REFERENCES users(userID))")
cursor.execute("CREATE TABLE log_login (userID VARCHAR(255), useccheck VARCHAR(255), loginAttempts INT DEFAULT 0, timing VARCHAR(255), newPass VARCHAR(255), FOREIGN KEY(userID) REFERENCES users(userID), FOREIGN KEY(useccheck) REFERENCES users(useccheck))")
cursor.execute("CREATE TABLE log_wrongPassword (userID VARCHAR(255), useccheck VARCHAR(255), timing VARCHAR(255), attempts INT DEFAULT 0, FOREIGN KEY(userID) REFERENCES users(userID), FOREIGN KEY(useccheck) REFERENCES users(useccheck))")
cursor.execute("CREATE TABLE limited_users (userID VARCHAR(255), timing VARCHAR(255), FOREIGN KEY(userID) REFERENCES users(userID))")

# except Exception as e:
#     print(e)

def register(name, lname, ID, phoneNo, gmail, password):
    checking = False
    for i in password:
        if i.isalpha():
            checking = True
            break
    while not checking:
        print("Password should have alphabets, too!\ntry again:\n")
        password = input()
    checking2 = False
    for i in phoneNo:
        if i.isalpha():
            checking2 = True
            break
    while checking2:
        print("phone should not have alphabets!\ntry again:\n")
        phoneNo = input()
    checking3 = False
    for i in name:
        if i.isnumeric():
            checking3 = True
            break
    while checking3:
        print("Name should have alphabets!\ntry again:\n")
        name = input()
    checking4 = False
    for i in lname:
        if i.isnumeric():
            checking4 = True
            break
    while checking4:
        print("Last name should have alphabets!\ntry again:\n")
        lname = input()
    while gmail.isnumeric() or not gmail.endswith("@gmail.com"):
        print("Email should be a valid gmail address!\ntry again:\n")
        gmail = input()
    current_time = datetime.now().strftime("%H:%M:%S")
    temp = 1
    seccheck = input("what is your favorite color?")
    try:
        Q1 ="INSERT INTO users (uname, ulname, userID, phone, email, upassword, useccheck, timing , log_in) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, lname, ID, phoneNo, gmail, password, seccheck, current_time, temp)
        cursor.execute(Q1, values)
        db.commit()
    except Exception as e:
        print(e)
    sendMail(gmail,"succsessfully registered!^-^",f"Hi {name}.\nYou are a member of our family now!<3")
    menu(ID)
    
def sendMail(TO,SUBJECT,TEXT):
    try:
        message = textwrap.dedent("""\
            From: %s\
            To: %s\
            Subject: %s\
            %s\
            """ % ("snnn99554@gmail.com", ", ".join(TO), SUBJECT, TEXT))
        server = smtplib.SMTP("127.0.0.1")
        server.sendmail("snnn99554@gmail.com", TO, message)
        server.quit()
    except Exception as e:
        print(e)

def passwordRecovery(username):
    questionCount = 0
    seccheck = input("what was your answer to security question? ")
    try:
        cursor.execute("SELECT * from users WHERE userID = %s and useccheck = %s", (username, seccheck))
        checking = cursor.fetchall()
        db.commit()
    except Exception as e:
        print(e)
    while checking == None and questionCount < 5 :
        seccheck = input("what was your answer to security question?")
        print(f"login attempts = {questionCount}")
        questionCount += 1
    randomCode = random.randint(10000,100000)
    code_check = True
    try:
        cursor.execute('SELECT email FROM users WHERE userID = %s',(username))
        reciever = str(cursor.fetchone())
        db.commit()
        cursor.execute("SELECT * from users WHERE userID = %s and useccheck = %s", (username, seccheck))
        checking = cursor.fetchall()
        db.commit()
    except Exception as e:
        print(e)
    while code_check and checking == None and questionCount == 5 :
        sendMail(reciever, "login code", randomCode)
        entered_code = input("type the code we have sended to you here: ")
        if entered_code == randomCode:
            code_check = False
    try:
        user = cursor.fetchone()
        print(user)
        db.commit()
        current_time = datetime.now().strftime("%H:%M:%S")
        Q2 = "INSERT INTO log_login (userID, useccheck, loginAttempts, timing) VALUES(%s, %s, %s, %s)"
        cursor.execute(Q2,(username, seccheck, questionCount, current_time))
        db.commit()
    except Exception as e:
        print(e)
    changePassword(username)
    try:
        cursor.execute('SELECT upassword FROM users WHERE userID = %s',(username))
        new_password = str(cursor.fetchone())
        db.commit()
        update_query2 = " UPDATE log_login SET newPass = %s WHERE userID = %s"
        cursor.execute(update_query2,(new_password, username))
        db.commit()    
    except Exception as e:
        print(e)

def wrongPassword(username):
    try:
        print("invalid inputs for login attempt!")
        cursor.execute('SELECT attempts FROM log_wrongPassword WHERE userID = %s',(username))
        number = cursor.fetchone()
        db.commit()
        if int(number) + 1 < 3 :
            temp = int(number) + 1
            update_query = " UPDATE log_wrongPassword SET attempts = %s WHERE userID = %s"
            cursor.execute(update_query,(temp, username))
            db.commit()
        else: 
            current_time = datetime.now().strftime("%H:%M:%S")
            Q4 = "INSERT INTO limited_users (userID, timing) VALUES(%s, %s)"
            cursor.execute(Q4,(username, current_time))
            db.commit()
    except Exception as e:
        print(e)
        
def login():
    try:
        username = input("type your username here: ")
        limited_query = f"SELECT userID From limited_users WHERE userID = {username}"
        limited_username = cursor.execute(limited_query)
        db.commit()
        login_query =f"SELECT userID FROM users WHERE log_in = '1' and userID = {username}"
        loggedin_username = cursor.execute(login_query)
        db.commit()
        if (not (username == limited_username)) and (not(username == loggedin_username)):
            password = input("type your password here or if you don't remember it just type 0:  ")
            if password == 0:
                passwordRecovery(username)
            else:
                cursor.execute('SELECT upassword FROM users WHERE userID = username')
                oldpass = cursor.fetchone()
                db.commit()
                if str(oldpass) == password:
                    cursor.execute("SELECT * from users WHERE userID = %s and upassword = %s", (username, password))
                    user = cursor.fetchone()
                    print("Hello!\nWelcome Back!\n" + user)
                    db.commit()
                    print("Congratulations!\nYou successfully logged in!\n" + user)
                    update_query = f" UPDATE users SET log_in = '1' WHERE userID = {username}"
                    cursor.execute(update_query)
                    db.commit()
                    menu(username)
                else:
                    wrongPassword(username)
        else:
            print("Sorry!\nYou can't login.>-<\n")
    except Exception as e:
        print(e)

def changePassword(username):
    try:
        questionCount = 0
        seccheck = input("what was your answer to security question? ")
        cursor.execute("SELECT * from users WHERE userID = %s and useccheck = %s", (username, seccheck))
        checking = cursor.fetchone()
        db.commit()
        while checking == None and questionCount < 5 :
            seccheck = input("what was your answer to security question?")
            print(f"login attempts = {questionCount}")
            questionCount += 1
        randomCode = random.randint(10000,100000)
        code_check = True
        cursor.execute('SELECT email FROM users WHERE userID = username')
        checking_email = cursor.fetchone()
        reciever = str(checking_email)
        db.commit()
        cursor.execute("SELECT * from users WHERE userID = %s and useccheck = %s", (username, seccheck))
        checking2 = cursor.fetchone()
        db.commit()
        while code_check and checking2 == None and questionCount == 5 :
            sendMail(reciever, "login code", randomCode)
            entered_code = input("type the code we have sended to you here: ")
            if entered_code == randomCode:
                code_check = False
        new_password = input("Enter your new password here: ")
        while not new_password.isalpha():
            print("Password should have alphabets, too!\ntry again:\n")
            new_password = input()
        update_query = f" UPDATE users SET upassword = {new_password} WHERE userID = {username}"
        cursor.execute(update_query)
        db.commit()
    except Exception as e:
        print(e)

def firstMenu():
    print("Hello.Welcome here.Please enter the number of one of the choices below: ")
    choice = input("1)register for a new account\n2)login to an existing account")
    if choice == "1":
        name = input("Enter your name here: ")
        lname = input("Enter your lname here: ")
        ID = input("Enter your ID here: ")
        phoneNo = input("Enter your phone number here: ")
        gmail = input("Enter your gmail here: ")
        password = input("Enter your password here: ")
        register(name, lname, ID, phoneNo, gmail, password)
    if choice == "2":
        login()

def serachMenu(ids,username):
    try:
        choice = input("Please select one of the options below:\n1)friendship\n2)unfriend\n3)block\n4)unblock\n5)send messsages\n6)exit\n")
        if choice == "1":
            no = 1
            for id in ids:
                print(no + ") " + id)
                no += 1
            i = int(input("Enter the number of one person")) - 1
            cursor.execute(f'SELECT blockerID, blockedID, u1ID, u2ID FROM friends OUTER JOIN blocked WHERE (blockerID == {ids[i]} and blockedID == {username}) or (u1ID == {ids[i]}and u2ID == {username}) or (u2ID == {ids[i]}and u1ID == {username})')
            checking = cursor.fetchall()
            db.commit()
            if checking == None:
                Q6 = f"INSERT INTO friends (u1ID, u2ID) VALUES ({username}, {ids[i]})"
                cursor.execute(Q6)
                db.commit()
                Q7 = f"DELETE FROM blocked WHERE blockerID = {username} and blockedID = {ids[i]}"
                cursor.execute(Q7)
                db.commit()
            choice = input("Please select one of the options below:\n1)friendship\n2)unfriend\n3)block\n4)unblock\n5)send messsages\n6)exit\n")
        elif choice == "2":
            no = 1
            for id in ids:
                print(no + ") " + id)
                no += 1
            i = int(input("Enter the number of one person")) - 1
            Q6 = f"DELETE FROM friends WHERE (u1ID == {ids[i]}and u2ID == {username}) or (u2ID == {ids[i]}and u1ID == {username})"
            cursor.execute(Q6)
            db.commit()
            choice = input("Please select one of the options below:\n1)friendship\n2)unfriend\n3)block\n4)unblock\n5)send messsages\n6)exit\n")
        elif choice == "3":
            no = 1
            for id in ids:
                print(no + ") " + id)
                no += 1
            i = int(input("Enter the number of one person")) - 1
            current_time = datetime.now().strftime("%H:%M:%S")
            cursor.execute(f'INSERT INTO blocked (blockerID, blockedID, timing) VALUES ({username}, {ids[i]}, {current_time})')
            cursor.execute(f'SELECT fID FROM friends WHERE (u1ID == {ids[i]}and u2ID == {username}) or (u2ID == {ids[i]}and u1ID == {username})')
            checking = list(cursor.fetchall())
            db.commit()
            if not checking == None:
                Q6 = f"DELETE FROM friends WHERE fID = {checking[0]}"
                cursor.execute(Q6)
                Q7 = f"DELETE FROM friends WHERE fID = {checking[1]}"
                cursor.execute(Q7)
                db.commit()
            choice = input("Please select one of the options below:\n1)friendship\n2)unfriend\n3)block\n4)unblock\n5)send messsages\n6)exit\n")
        elif choice == "4":
            no = 1
            for id in ids:
                print(no + ") " + id)
                no += 1
            i = int(input("Enter the number of one person")) - 1
            current_time = datetime.now().strftime("%H:%M:%S")
            cursor.execute(f'DELETE FROM blocked WHERE blockerID = {username} and blockedID= {ids[i]} and timing = {current_time}')
            db.commit()
            choice = input("Please select one of the options below:\n1)friendship\n2)unfriend\n3)block\n4)unblock\n5)send messsages\n6)exit\n")
        elif choice == "5":
            no = 1
            for id in ids:
                print(no + ") " + id)
                no += 1
            i = int(input("Enter the number of one person")) - 1
            sendmessage(username , id[i])
        elif choice == "6":
            menu(username)
    except Exception as e:
        print(e)

def sendmessage(sender,reciever):
    try:
        msg = input("Please type your message here: ")
        current_time = datetime.now().strftime("%H:%M:%S")
        cursor.execute(f'INSERT INTO messages (sID, rID, timing, text) VALUES ({sender}, {reciever}, {current_time}, {msg})')
        db.commit()
    except Exception as e:
        print(e)
   
def menu(username):
    try:
        choice = input("Hi.Type the number of the action you want to perform here:\n1)change password\n2)log out\n3)delete account\n4)search\n5)messages\n6)friends\n7)shutdown")
        if choice == "1":
            changePassword(username)
            menu(username)
        elif choice == "2":
            update_query = f" UPDATE users SET log_in = '0' WHERE userID = {username}"
            cursor.execute(update_query)
            db.commit()
            firstMenu()
        elif choice == "3":
            update_query = f" UPDATE users SET upassword = None SET uname = None and SET ulname = None and SET phone = None and SET email = None and SET useccheck = None and SET timing = None and SET log_in = '0' WHERE userID = {username}"
            cursor.execute(update_query)
            db.commit()
        elif choice == "4":
            searched_username = input("Please enter the username you want to search for: ")
            searching_number = int(len(searched_username)*0.5)
            searching_name = searched_username[0:searching_number]
            search_query = f"SELECT userID FROM users WHERE userID like {searching_name}%"
            cursor.execute(search_query)
            searched_IDs = []
            for row in cursor:
                searched_IDs.append(row)
            db.commit()
            no = 1
            for id in searched_IDs:
                print(no + ") " + id)
                no += 1
            serachMenu(searched_IDs,username)  
        elif choice == "5":
            search_query = f"SELECT * FROM messages WHERE rID = {username}"
            cursor.execute(search_query)
            messages = cursor.fetchall()
            db.commit()
            no = 1
            for msg in messages:
                print(no + ") " + msg)
                no += 1
            cursor.execute(f"UPDATE messages SET seen = '1' WHERE seen = '0'")
            db.commit()
            choice2 = input("If you want to like a message type its number or type 0")
            if choice2 == "0": 
                menu(username)
            else:
                cursor.execut(f"UPDATE messages SET liked = '1' WHERE mID = {messages[int(choice2)-1][6]}")
                db.commit()
                menu(username)
        elif choice == "6":
            search_query = f"SELECT * FROM friends WHERE u1ID = {username} or u2ID = {username}"
            cursor.execute(search_query)
            friends = cursor.fetchall()
            db.commit()
            no = 1
            for fr in friends:
                print(no + ") " + fr)
                no += 1
            choice2 = input("If you want to unfriend a friend type their number or type 0")
            if choice2 == "0": 
                menu(username)
            else:
                i = int(choice2) - 1
                Q6 = f"DELETE FROM friends WHERE (u1ID == {friends[i]}and u2ID == {username}) or (u2ID == {friends[i]}and u1ID == {username})"
                cursor.execute(Q6)
                db.commit()
                menu(username)
        elif choice == "7":
            print(f"Goodbye {username}!\nHope to see you again soon.^-^\n")
    except Exception as e:
        print(e)
firstMenu()
db.close()