import csv, MySQLdb, sys

# Path to and name of a CSV output file
input_file = sys.argv[1]

# Connect to a MySQL database
con = MySQLdb.connect(host='Localhost', port=3306, db='my_suppliers', user='open_source', passwd='1111')
c = con.cursor()

# Read a file writer object and write the header row
file_reader = csv.reader(open(input_file, 'r', newline=''), delimiter=',')
header = next(file_reader, None)
for row in file_reader :
    data = []
    for column_index in range(len(header)) :
        data.append(str(row[column_index]).strip())
    print(data)
    c.execute("""UPDATE Suppliers SET Cost=%s, Purchase_Date=%s WHERE Supplier_Name=%s""", data)
con.commit()

# Query the Suppliers table and write the output to a CSV file
c.execute("SELECT * FROM Suppliers")

rows = c.fetchall()
for row in rows :
    output = []
    for column_index in range(len(row)) :
        output.append(str(row[column_index]))
    print(output)