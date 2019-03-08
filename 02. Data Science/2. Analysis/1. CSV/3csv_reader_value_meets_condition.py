# 목적 : 파이썬 기본문법으로 특정 행을 필터링 하기
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r', newline='') as csv_in_file :
    with open(output_file, 'w', newline='') as csv_out_file :
        filereader = csv.reader(csv_in_file)
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row_list in filereader:
            supplier = str(row_list[0]).strip() # supplier열이 파일에 1번째에 있어서
            cost = str(row_list[3]).strip('$') #cost열이 파일에 2번째에 있어서
            if supplier == 'Supplier Z' or float(cost) > 600.0 : # 'supplier == 'Supplier Z'는 있으나 마나 한 조건
                filewriter.writerow(row_list)