import pandas as pd
import MySQLdb

filename = "Basic_Student_Info.xlsx"

con = MySQLdb.connect(host='localhost', port=3306, db='my_students_2', user='root', passwd='1111', charset='utf8mb4')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Students
                (Student_ID VARCHAR(20), Name VARCHAR(10), Sex VARCHAR(10), Age INT(10), Major VARCHAR(10), 
                 PRIMARY KEY (Student_ID));"""
c.execute(create_table)
con.commit()

stu_data = pd.read_excel(filename)

for row in range(len(stu_data)) :
    data = []
    for col in range(len(stu_data.columns)) :
        data.append(stu_data.loc[row][col])
    print(data)
    c.execute("INSERT INTO Students VALUES ('%s', '%s', '%s', %s, '%s');" %(data.pop(0),data.pop(0),
              data.pop(0), data.pop(0), data.pop(0)))
con.commit()



