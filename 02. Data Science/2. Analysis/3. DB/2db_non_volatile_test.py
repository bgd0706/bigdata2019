import csv
import sqlite3
import sys

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows :
    output = []
    for column_index in range(len(row)) :
        output.append(str(row[column_index]))
    print(output)
