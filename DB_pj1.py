import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rootSarvin1372",
  database="sarvinnami"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE ST (STID VARCHAR('s1','s2','s3','s4','s5'), STname VARCHAR('Sn1','Sn2','Sn3','Sn4','Sn5'),STLevel VARCHAR(),STmajor VARCHAR())")
mycursor.execute("CREATE TABLE CO (COID VARCHAR('c1','c2','c3','c4'), COname VARCHAR('Cn1','Cn2','Cn3','Cn4'), COtype VARCHAR('P','P','Q','Q'),Credit VARCHAR(4,3,4,3))")
