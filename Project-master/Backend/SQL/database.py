import mysql.connector

print("after import")

cnx = mysql.connector.connect(user='root', password='changeme', host = '172.22.0.1', port = 8080, database='testapp')

cursor = cnx.cursor()

if cnx.is_connected():
	print("connected to sql server")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)

print("connection worked")


cnx.close()