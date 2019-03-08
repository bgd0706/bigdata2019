# 목적 : csv 파일 읽고 쓰기
import sys
input_file = sys.argv[1] # supplier_data.csv
output_file = sys.argv[2] # output_files/1output.csv

with open(input_file, 'r', newline='') as filereader :
    with open(output_file, 'w', newline='') as filewriter :
        header = filereader.readline() # 헤더행 한 줄 읽기
        header = header.strip() # 공백 제거
        header_list = header.split(',') # ',' 기준으로 split하여 리스트로 만들어짐
        print(header_list)
        filewriter.write(','.join(map(str,header_list))+'\n') # 리스트 -> 문자열로
        for row in filereader : # 다음 줄 부터 시작 
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str,row_list))+'\n')