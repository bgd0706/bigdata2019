import pandas as pd
import MySQLdb

filename = "Student_Language.xlsx"

con = MySQLdb.connect(host='localhost', port=3306, db='my_students_2', user='root', passwd='1111', charset='utf8mb4')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Languages
                (Student_ID VARCHAR(20), Name VARCHAR(10), Level VARCHAR(10), Period VARCHAR(10), 
                 FOREIGN KEY(Student_ID) REFERENCES Students(Student_ID));"""
c.execute(create_table)
con.commit()

stu_data = pd.read_excel(filename)
print(len(stu_data))
for row in range(len(stu_data)) :
    data = []
    for col in range(len(stu_data.columns)) :
        data.append(stu_data.loc[row][col])
    print(data)
    c.execute("INSERT INTO Languages VALUES ('%s', '%s', '%s', '%s');" %(data.pop(0),data.pop(0),data.pop(0), data.pop(0)))
con.commit()



