import pandas as pd
import MySQLdb

filename = "Student_Info_DB_Scheme.xlsx"

con = MySQLdb.connect(host='localhost', port=3306, db='my_students', user='root', passwd='1111', charset='utf8mb4')
c = con.cursor()

c.execute("UPDATE Students SET name ='박영호' WHERE Student_ID='ITT001'")
con.commit()