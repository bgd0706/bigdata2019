# 목적 : pandas 문법으로 특정 행을 필터링 하기
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)

data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

data_frame_value_meets_condition = data_frame.loc[(data_frame['Supplier Name'].str.contains('Z')) | (data_frame['Cost'] > 600.0), : ]

data_frame_value_meets_condition.to_csv(output_file, index=False)

# loc [행조건 : 열조건] -> 문자열 기준
# iloc [행조건 : 열조건] -> 숫자를 기준
# ix [행조건 : 열조건] -> 문자열, 숫자 모두 가능