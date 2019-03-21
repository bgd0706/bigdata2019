from sklearn import svm, metrics
import glob, os.path, re, json
# 목적 : 어느 나라 말인지 예측하는 것

# 텍스트를 읽어 들이고 출현 빈도 조사하기
def check_freq(fname) :
    name = os.path.basename(fname)
    lang = re.match(r'^[a-z]{2,}', name).group()
    with open(fname, "r", encoding='utf-8') as f :
        text = f.read()
    text = text.lower() # 소문자 변환
    # 숫자 세기 변수 (cnt) 초기화하기
    cnt = [0 for n in range(0, 26)] # 0이 26개로 초기화된 list -> [0,0,0, .... ,0,0]
    code_a = ord("a")
    code_z = ord("z")
    # 알파벳 출현 횟수 구하기
    for ch in text :
        n = ord(ch)
        if code_a <= n <= code_z: # a~z 사이에 있을 때
            cnt[n - code_a] += 1
    # 정규화하기
    total = sum(cnt)
    freq = list(map(lambda n : n/ total, cnt)) # 각각의 언어별 빈도비율
    return (freq, lang) # freq는 고정 변수, lang은 종속 변수

# 각 파일 처리하기
def load_files(path) :
    freqs = []
    labels = []
    file_list = glob.glob(path)
    for fname in file_list :
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels} # 딕셔너리 형태로 반환
data = load_files("./lang/train/*.txt")
test = load_files("./lang/test/*.txt")
# 이후를 대비해서 JSON으로 결과 저장하기
with open("./lang/freq.json", "w", encoding="utf-8") as fp :
    json.dump([data, test], fp)
# 학습하기
clf = svm.SVC(gamma='auto')
clf.fit(data["freqs"], data["labels"])
# 예측하기
predict = clf.predict(test["freqs"])
# 결과 테스트하기
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)
