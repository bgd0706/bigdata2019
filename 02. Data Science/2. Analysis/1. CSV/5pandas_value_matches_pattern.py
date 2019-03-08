# 목적 : pandas에서 패턴 활용
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.ix[data_frame['Invoice Number'].str.startswith('001-'), :]
# 간단한 정규식은 해당 패턴에 매칭이 되는 함수를 사용하는 것이 유리
# 복잡한 정규식은 함수보다 정규식을 활용하는 것이 유리

data_frame_value_matches_pattern.to_csv(output_file, index=False)