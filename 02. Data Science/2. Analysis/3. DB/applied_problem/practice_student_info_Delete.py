import pandas as pd
import MySQLdb

filename = "Student_Info_DB_Scheme.xlsx"

con = MySQLdb.connect(host='localhost', port=3306, db='my_students', user='root', passwd='1111', charset='utf8mb4')
c = con.cursor()

c.execute("DELETE FROM Students WHERE Student_ID='ITT002'")
con.commit()