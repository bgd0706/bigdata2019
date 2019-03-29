import pandas as pd
from sklearn import svm, metrics, model_selection

csv = pd.read_csv('iris.csv') # iris의 csv 데이터를 읽어들인다.

data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]] # 독립변수 추출
label = csv["Name"] # 종속변수 추출

clf = svm.SVC() # svm 객체 생성

# 크로스밸리데이션
# 특정 데이터를 훈련 전용 데이터와 테스트 전용 데이터로 분할한 뒤
# 훈련 데이터를 활용해 학습하여 테스트 데이터로 데스트해서 학습의 타당성을 검증하는 방법
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("각각의 정답률 =", scores)
print("평균 정답률 =", scores.mean())