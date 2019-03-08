# 목적 : 워크북의 기본정보 확인
# xlrd 모듈 설치

import sys
from xlrd import open_workbook

input_file = sys.argv[1]

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets) # nsheets는 workbook의 멤버변수
for worksheet in workbook.sheets() :
    print("Worksheet name:", worksheet.name, "\tRows:", worksheet.nrows, "\tColumns:", worksheet.ncols)