import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="rootSarvin1372",
  database="sarvinnami"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE ST (STID VARCHAR(255), STname VARCHAR(255),STLevel VARCHAR(255),STmajor VARCHAR(255))")
# mycursor.execute("CREATE TABLE CO (COID VARCHAR(255), COname VARCHAR(255), COtype VARCHAR(255),Credit VARCHAR(255))")
# mycursor.execute("CREATE TABLE STCO (STID VARCHAR(255),COID VARCHAR(255), YR VARCHAR(255), TR VARCHAR(255),Grade VARCHAR(255))")
# #  inserting into table st
sql = "INSERT INTO ST (STID, STname) VALUES (%s, %s)"
val = [
  ('S1', 'Sn1'),
  ('S2', 'Sn2'),
  ('S3', 'Sn3'),
  ('S4', 'Sn4'),
  ('S5', 'Sn5')
]

mycursor.executemany(sql, val)

mydb.commit()

sql2 = "INSERT INTO CO (COID,COname, COtype,Credit) VALUES (%s, %s, %s, %d)"
val2 = [
  ('C1', 'Cn1', 'P', 4),
  ('C2', 'Cn2', 'P', 3),
  ('C3', 'Cn3', 'Q', 4),
  ('C4', 'Cn4', 'Q', 3)
]

mycursor.executemany(sql2, val2)

mydb.commit()

sql3 = "INSERT INTO STCO (STID, COID, YR, TR, Grade) VALUES (%s, %s, %s, %d, %d)"
val3 = [
  ('S1', 'C1', '94-95', 2, 19),
  ('S1', 'C3', '94-95', 2, 20),
  ('S2', 'C2', '94-95', 2, 18),
  ('S3', 'C2', '94-95', 1, 17),
  ('S4', 'C3', '94-95', 2, 16)
]

mycursor.executemany(sql3, val3)

mydb.commit()

sql4 = "SELECT *\
  FROM STCO \
  INNER JOIN CO ON STCO.COID = CO.COID"

mycursor.execute(sql4)

myresult = mycursor.fetchall()

# mycursor.execute("SELECT STNAME FROM myresult WHERE")

# myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# mycursor.execute("SELECT * FROM CO")

# myresult2 = mycursor.fetchall()

# for x in myresult2:
#   print(x)