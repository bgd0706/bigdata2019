import sqlite3

# Create an in=memory SQLite3 database
# Create a table called sales with four attributes
con = sqlite3.connect(':memory:') # 프로그램이 종료가 되면 휘발성이라 날라가서 조회되지 않는다.

# Query the sales table
cursor = con.execute("SELECT * FROM sales")
rows = cursor.fetchall()

# Count the number of rows in the output
row_counter = 0
for row in rows :
    print(row)
    row_counter += 1
print("Number of rows: {}".format(row_counter))