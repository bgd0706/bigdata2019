import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv('iris.csv') # iris의 csv 데이터를 읽어들인다.

csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]] # 독립변수 추출
csv_label = csv["Name"] # 종속변수 추출

# 학습 전용 데이터와 테스트 전용 데이터로 나누기
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)

clf = svm.SVC() # svm 객체 생성
clf.fit(train_data, train_label) # 데이터 학습
pre = clf.predict(test_data) # 데이터 예측

ac_score = metrics.accuracy_score(test_label, pre) # 정답률 구하기
print("전체 데이터 수: %d" %(len(csv_data)))
print("학습 전용 데이터 수: %d" %(len(train_data)))
print("테스트 데이터 수: %d" %(len(test_data)))
print("정답률 =", ac_score)