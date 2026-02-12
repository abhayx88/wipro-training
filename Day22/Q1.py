import mysql.connector
from pymongo import MongoClient

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhay@2026",
    database="company_db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM employees WHERE salary > 50000")
for emp in cursor.fetchall():
    print(emp)

cursor.execute(
    "INSERT INTO employees (name, department, salary) VALUES (%s,%s,%s)",
    ("Riya", "IT", 58000)
)
conn.commit()

cursor.execute(
    "UPDATE employees SET salary = salary * 1.10 WHERE id = 1"
)
conn.commit()

cursor.close()
conn.close()

client = MongoClient("mongodb://localhost:27017/")
collection = client.company_db.employees

collection.insert_one({
    "name": "Amit",
    "department": "IT",
    "salary": 60000
})

for emp in collection.find({"department": "IT"}):
    print(emp)

collection.update_one(
    {"name": "Amit"},
    {"$set": {"salary": 65000}}
)

client.close()
