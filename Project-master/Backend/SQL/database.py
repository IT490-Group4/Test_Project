import mysql.connector

print("after import")

# host can be 'mysql' because docker-compose automagically (TM) does name
# resolution for us. Also, mysql runs on port 3306, not 8080.
cnx = mysql.connector.connect(user='root', password='changeme', host = 'mysql', port = 3306, database='testapp')

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
