import sqlite3

con = sqlite3.connect('Suppliers.db')
c = con.cursor()
delete_table = """
delete
from Suppliers
"""
c.execute(delete_table)
con.commit()

# Query the Suppliers table
con = sqlite3.connect('Suppliers.db')
c = con.cursor()
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows :
    output = []
    for column_index in range(len(row)) :
       output.append(str(row[column_index]))
    print(output)