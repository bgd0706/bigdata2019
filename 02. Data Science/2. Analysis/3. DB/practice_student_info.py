import sys
import pandas as pd
import sqlite3

filename = "Student_Info_DB_Scheme.xlsx"

read_excel = pd.read_excel(filename, index_col=None)

con = sqlite3.connect('Students.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Students
                (Student_ID VARCHAR(20), Name VARCHAR(20), Age INT(20), Major  VARCHAR(20), Practicable_computer_languages VARCHAR(20), 
                High_level VARCHAR(20), Middle_level VARCHAR(20));"""
c.execute(create_table)
con.commit()





