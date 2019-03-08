# 목적 : 기본 파이썬 csv 모듈을 활용하여 csv 파일 읽고 쓰기
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open (input_file, 'r', newline='') as csv_in_file :
    with open (output_file, 'w', newline='') as csv_out_file :
        filereader = csv.reader(csv_in_file, delimiter=',') # delimiter는 어떤 기호로 기준으로 삼아 읽겠다는 것이다.
        filewriter = csv.writer(csv_out_file, delimiter=',') # default값이 ','이므로 ,라면 굳이 안해도 된다.
        for row_list in filereader :
            filewriter.writerow(row_list)