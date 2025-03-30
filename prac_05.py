# Description: Write a Python program to extract data from a MySQL database and save it to a CSV file.
# The program should connect to the MySQL database, extract data from the STUDENT table, and save it to a CSV file named dataset.csv.
import csv
import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yuki_8686009",
        database="sekai"
    )
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

cursor = connection.cursor()
query1 = "SELECT * FROM student;"
cursor.execute(query1)
results1 = cursor.fetchall()

query2 = "desc student;"
cursor.execute(query2)
results2 = cursor.fetchall()
header=[]
for row in results2:
    header.append(row[0])

print(header)
file = open("dataset.csv",'w+',newline='')

csv_writer = csv.writer(file)
csv_writer.writerow(header)
csv_writer.writerows(results1)


