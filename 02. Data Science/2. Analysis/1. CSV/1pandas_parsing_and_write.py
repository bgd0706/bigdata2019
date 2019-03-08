# 목적 : pandas로 csv 파일 읽고 쓰기
import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file) # read_csv는 csv 파일 읽기
print(data_frame)
data_frame.to_csv(output_file, index=False) # to_csv는 csv 파일로 저장하기 # index=False는 인덱스가 안나오게 (파일로 내보냈을 때)