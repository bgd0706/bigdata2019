# 목적 : 열의 인덱스 값을 사용하여 특정 열을 선택하기
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

my_columns = [0, 3]

with open(input_file, 'r', newline='') as csv_in_file :
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        for row_list in filereader :
            row_list_output = []
            for index_value in my_columns :
                row_list_output.append(row_list[index_value])
            filewriter.writerow(row_list_output)
        # 첫번째 for문 : 행, 두번째 for문 : 열
