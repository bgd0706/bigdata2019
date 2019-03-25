from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

csv = pd.read_csv('train_test.csv', header=None)
csv_label = csv.loc[:,0]
csv_data = csv.loc[:, 1:]
images = []
labels = []

for idx in range(len(csv_label)) :
    if idx % 2 == 0 :
        labels.append(csv_label[idx])

for idx in range(len(csv_data)) :
    if idx % 2 == 0 :
        cols = csv_data.iloc[idx,:]
        vals = list(map(lambda n: int(n) / 256, cols))
        images.append(vals)

train_data, test_data, train_label, test_label = train_test_split(images, labels)

# 데이터 학습시키고 예측하기
clf = svm.SVC(gamma='auto')
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
# 정답률 구하기
ac_score = metrics.accuracy_score(test_label, pre)
cl_report = metrics.classification_report(test_label, pre)
print("전체 데이터 수: %d" %(len(images)))
print("학습 전용 데이터 수: %d" %(len(train_data)))
print("테스트 데이터 수: %d" %(len(test_data)))
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)