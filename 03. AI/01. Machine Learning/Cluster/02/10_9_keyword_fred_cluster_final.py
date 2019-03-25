import time
from scipy import stats
from collections import Counter
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics import silhouette_score

# 빅데이터 Format
# InvoiceNo : 6자리 숫자로 이루어진 거래 고유번호
# StockCode : 5자리 숫자로 이루어진 상품 코드
# Description : 상품명
# Quantity : 한 거래당 판매된 상품수
# InvoiceDate : 거래가 성립된 일시 MM/DD/YY HH:MM
# UnitPrice : 가격
# CustomerID : 사용자 ID
# Country : 사용자의 국가

# 데이터 구조 정의
user_product_dic = {} # 사용자 ID를 키로, 상품 코드의 set을 value로 갖는 딕셔너리
product_user_dic = {} # 상품 코드를 키로, 사용자 ID의 set을 value로 갖는 딕셔너리
product_id_name_dic = {} # 상품 코드를 키로, 상품명을 value로 갖는 딕셔너리
                         # -> 군집화의 내용을 확인하는 단계에서 상품명을 사용

def analyze_clusters_keywords(labels, product_id_name_dic, user_product_dic, id_user_dic) :
    # 각 클러스터의 아이디와, 해당 아이디의 클러스터 들어있는 유저 수를 출력
    print(Counter(labels)) # 리스트의 각각의 값 별로 누적 현황 확인
    cluster_item = {}

    for i in range(len(labels)) :
        cluster_item.setdefault(labels[i], [])
        for x in user_product_dic[id_user_dic[i]] : # 각 사용자의 임시 ID i에 대해 사용자 코드를 찾은 후
            cluster_item[labels[i]].extend([product_id_name_dic[x]]) # 그 사용자 코드와 연결된 구매상품의 ID를 참조한 후
                                                                     # 그 ID를 이용해 상품명을 찾아
                                                                     # 딕셔너리에 클러스터 ID를 키로, 상품명을 value로 추가
    for cluster_id, product_name in cluster_item.items() :
        product_name_keyword = (" ").join(product_name).split() # 각 클러스터안의 상품명을 join명령으로 합쳐 하나의 문자열로
                                                                # 만든 뒤 스페이스 혹은 탭으로 split 하여 키워드로 분해
        print("cluster_id:", cluster_id) # 클러스터 ID 출력
        print(Counter(product_name_keyword).most_common(20)) # 그 아이디를 가지는 클러스터에 속하는 유저들이 구매한 상품들의
                                                             # 상품명안에 가장 자주 나타나는 단어 20개를 역순으로 출력

def analyze_clusters_keywords_bigram(labels, product_id_name_dic,user_product_dic, id_user_dic) :
    # 각 클러스터의 아이디와, 해당 아이디의 클러스터 들어있는 유저 수를 출력
    print(Counter(labels))  # 리스트의 각각의 값 별로 누적 현황 확인
    cluster_item = {}

    for i in range(len(labels)) :
        cluster_item.setdefault(labels[i], [])
        for x in user_product_dic[id_user_dic[i]] : # 각 사용자의 임시 ID i에 대해 사용자 코드를 찾은 후
            cluster_item[labels[i]].extend([product_id_name_dic[x]]) # 그 사용자 코드와 연결된 구매상품의 ID를 참조한 후
                                                                     # 그 ID를 이용해 상품명을 찾아
                                                                     # 딕셔너리에 클러스터 ID를 키로, 상품명을 value로 추가
    for cluster_id, product_name in cluster_item.items() :
        bigram = []
        product_name_keyword = (' ').join(product_name).replace('  OF  ', ' ').split()
            # 각 클러스터 안의 상품명을 join 명령으로 합쳐 하나의 문자열로 만든 뒤 OF를 공백으로 리플레이스하고
        for i in range(0, len(product_name_keyword)-1) :
            bigram.append(' '.join(product_name_keyword[i:i + 2]))
        print('cluster_id:', cluster_id)
        print(Counter(bigram).most_common(20))

def analyze_clusters_product_count(labels, user_product_dic, id_user_dic) :
    product_len_dic = {}

    for i in range(0, len(labels)) :
        product_len_dic.setdefault(labels[i], [])
        product_len_dic[labels[i]].append(len(user_product_dic[id_user_dic[i]]))

    for k, v in product_len_dic.items() :
        print('cluster: ', k)
        print(stats.describe(v))

# 파일을 읽어 위에 정의한 데이터구조를 채움
for line in open('online_retail_utf.txt') :
    # 데이터를 한 행씩 읽어서 필요한 항목을 저장
    line_items = line.strip().split('\t')
    user_code = line_items[6]
    product_id = line_items[1]
    product_name = line_items[2]

    if len(user_code) == 0 : continue # 사용자 ID가 없을 경우 무시합니다.

    country = line_items[7]
    if country != 'United Kingdom' : continue # 영국에서 구매한 사용자만 고려하므로, 국가가 united kingdom 이 아닌 경우엔 무시

    try : # 연도 읽을 때 에러 처리, 파일 헤더를 무시
        invoice_year = time.strptime(line_items[4], '%m/%d/%y %H:%M').tm_year
    except ValueError :
        continue

    if invoice_year != 2011 : continue # 2011년에 일어난 구매가 아닌 것은 무시

    # 읽은 정보로 데이터 구조를  채움
    # 상품 가짓수를 고려하므로 상품 코드를 set으로 가지도록 할 예정
    user_product_dic.setdefault(user_code, set()) # 딕셔너리 value 구조를 집합으로 -> set()의 결과는 공집합
    user_product_dic[user_code].add(product_id)

    product_user_dic.setdefault(product_id, set())
    product_user_dic[product_id].add(user_code)

    product_id_name_dic[product_id] = product_name

product_per_user_li = [len(x) for x in user_product_dic.values()] # 데이터구조를 다 채웠으므로 각 사용자들이 구매한 상품 가짓수로 리스트를 생성

print("===============================================================================================================")
print("Step1] 빅데이터 로딩 완료")
print('# of users:', len(user_product_dic)) # 최종 사용자 수 출력
print("# of products:", len(product_user_dic)) # 최종 상품 가짓수  출력

print(stats.describe(product_per_user_li)) # 각 사용자들이 구매한 상품 가짓수로 기초 통계량을 출력

min_product_user_li = [k for k,v in user_product_dic.items() if len(v)==1] # 구매한 상품의 가짓수가 1인 사용자의 사용자 ID를 검색
max_product_user_li = [k for k,v in user_product_dic.items() if len(v)>=600] # 구매한 상품의 가짓수가 600개 이상인 사용자의 사용자 ID를 검색
print("# of users purchased one product: %d" %(len(min_product_user_li)))
print("# of users purchased more than 600 product: %d" %(len(max_product_user_li)))

user_product_dic = {k:v for k,v in user_product_dic.items() if len(v)>1 and len(v)<600}
    # 찾아낸 사용자를 군집화에 사용할 user_product_dic에서 제외
print("# of left user: %d" %(len(user_product_dic)))

# 남아 있는 사용자가 구매한 상품에도 0에서 시작하는 고유 ID를 부여
# because 데이터 set에서 제외된 사용자가 구매한 상품은 군집화에서 사용하지 않기 때문에
id_product_dic = {}
for product_set_li in user_product_dic.values() :
    for x in product_set_li :
        if x in id_product_dic :
            product_id = id_product_dic[x]
        else :
            id_product_dic.setdefault(x, len(id_product_dic))
print("# of left items:%d" %(len(id_product_dic)))

id_user_dic = {}
user_product_vec_li = [] # 군집화의 입력으로 사용할 리스트
all_product_count = len(id_product_dic) # 군집화에서 사용할 총 고유 상품 가짓수. 즉, 원-핫 인코딩으로 변환할 피처의 가짓수

for user_code, product_per_user_set in user_product_dic.items() : # 고유 상품 가짓수를 길이로 하는 리스트 생성
    user_product_vec = [0] * all_product_count # user_product_vec을 모두 0으로 초기화
    id_user_dic[len(id_user_dic)] = user_code # id_user_dic의 길이를 이용하여 사용자 ID를 0부터 시작하는 user_id로 변경

    for product_name in product_per_user_set :
        user_product_vec[id_product_dic[product_name]]=1 # 사용자가 구매한 상품 코드를 키로 하여 user_product_vec에서의
                                                         # 해당 상품 코드의 상품 ID를 찾아 value를 1로 셋팅
    # 한 사용자의 처리가 끝났으므로 이 사용자의 user_product_vec을 배열에 추가하는데 배열의 인덱스는 새로 정의한 user_id가 됨

    user_product_vec_li.append(user_product_vec)

print("===============================================================================================================")
print("\n Step2] 사이킷런을 이용하여 실루엣 계수 구하기")
test_data = np.array(user_product_vec_li)

for k in range(2,9) :
    km = KMeans(n_clusters=k).fit(test_data)
    print("score for %d clusters:%.3f" %(k, silhouette_score(test_data,km.labels_)))

print("===============================================================================================================")
print("\n Step3] 상품 키워드 구하기")
km=KMeans(n_clusters=2, n_init=10, max_iter=20) # 전체 구간을 n_init 범위 내에 max_iter만큼 반복하여 최적의 클러스터링을 검색
km.fit(test_data)
analyze_clusters_keywords(km.labels_, product_id_name_dic, user_product_dic, id_user_dic)

print("===============================================================================================================")
print("\n Step4] 의미 있는 키워드로 변환하기")
km=KMeans(n_clusters=2, n_init=10, max_iter=20)
km.fit(user_product_vec_li)
analyze_clusters_keywords_bigram(km.labels_, product_id_name_dic, user_product_dic, id_user_dic)

print("===============================================================================================================")
print("\n Step5] 기초통계량 추가 확인")
analyze_clusters_product_count(km.labels_, user_product_dic, id_user_dic)

print("===============================================================================================================")
print("\n Step6] 분석결과에 대하여 해석하고 발표하기")
