# 목적 : 간단한 기술 통계 구하기
import pandas as pd

# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',', header=0) # header = 0 이라는 것은 header가 0행 즉, 레코드가 인덱스 1부터 시작
wine.columns = wine.columns.str.replace(' ', '_')

print("변수별 요약통계 표시")

print("변수별 요약통계 표시")
print(wine.describe()) # count : 전체 레코드 행, mean : 평균, std : 표준편차, 25% : 1사분위값, 50% : 준위값, 75% : 3사분위값

print("\n유일값 찾기") # 데이터 유형이 어떤 것이 있는지 확인
print(sorted(wine.quality.unique()))

print("\n빈도 찾기")
print(wine.quality.value_counts())