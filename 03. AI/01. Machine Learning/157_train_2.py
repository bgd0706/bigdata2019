import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
# 붓꽃의 csv 데이터 읽어 들이기
csv = pd.read_csv('iris.csv')
# 필요한 열 추출하기
csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
csv_label = csv["Name"]
# 학습 전용 데이터와 테스트 전용 데이터로 나누기
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)
# 데이터 학습시키고 예측하기
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
# 정답률 구하기
ac_score = metrics.accuracy_score(test_label, pre)
print("전체 데이터 수: %d" %(len(csv_data)))
print("학습 전용 데이터 수: %d" %(len(train_data)))
print("테스트 데이터 수: %d" %(len(test_data)))
print("정답률 =", ac_score)