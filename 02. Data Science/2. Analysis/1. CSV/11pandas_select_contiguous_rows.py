# 목적 : 판다스를 이용하여 유효 데이터 선택하기
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, header=None)

data_frame = data_frame.drop([0,1,2,16,17,18])
data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3)) # index 3부터 해야되므로

data_frame.to_csv(output_file, index=False)