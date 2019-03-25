import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

data = pd.read_csv('./mnist/train.csv', header=None)
test = pd.read_csv('./mnist/t10k.csv', header=None)

all_csv = []
all_csv.append(data)
all_csv.append(test)

all_csv_concat = pd.concat(all_csv)
all_csv_concat.to_csv("./mnist/merge.csv", index=False,header=0)

def load_csv(fname) :
    labels = []
    images = []
    with open(fname, "r") as f :
        for line in f :
            cols = line.split(",")
            if len(cols) < 2 : continue
            labels.append(int(cols.pop(0)))
            vals = list(map(lambda n: int(n) / 256, cols))
            images.append(vals)
    return {"labels":labels, "images":images}

file_read = load_csv('./mnist/merge.csv')
images = file_read["images"]
labels = file_read["labels"]

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