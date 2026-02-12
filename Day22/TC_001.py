import mysql.connector
from twisted.names.client import query

host = "localhost"
user = "root"
password = "Abhay@2026"
database = "feb_2026"

conn=mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()
print("connected to database successfully")

query="SELECT * FROM feb_2026.emp_table"
cursor.execute(query)

results = cursor.fetchall()
for row in results:
    print(row)