from sklearn import svm
# XOR의 계산 결과 데이터 --- (※1)
xor_data = [
    # P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

and_data = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]

or_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

nor_data = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 0]
]

nand_data = [
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 학습을 위해 데이터와 레이블 분리하기
data =[]
label = []
for row in nand_data :
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p,q])
    label.append(r)
# 데이터 학습시키기
clf = svm.SVC(gamma='auto')
clf.fit(data, label)
# 데이터 예측하기
pre = clf.predict(data)
print("예측결과 :", pre)
# 결과 확인하기
ok = 0 ; total = 0
for idx, answer in enumerate(label) :
    p = pre[idx]
    if p == answer: ok+=1
    total += 1
print("정답률:", ok, "/", total, "=", ok/total *100,'%')