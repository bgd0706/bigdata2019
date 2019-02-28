import json
import re
from collections import Counter

list_org_link = []

def search_org_link (stu_json) :
    not_org_link = 0
    for index in range(len(stu_json)) :
        try :
            each_org_link = stu_json[index]["bloggerlink"]
            p = re.compile("//.+/(.+)")
            m = p.search(each_org_link)
            list_org_link.append(m.group(1))
        except :
            print("'org_link'가 없는 기사를 발견했습니다.")
            not_org_link += 1
    return not_org_link

def main () :
    print("="*10+"빅데이터 분석기"+"="*10)
    search_input = input("분석 키워드를 입력하세요: ")

    with open("%s_naver_blog.json" % search_input, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        stu_json = json.loads(json_string)

    print("데이터 분석을 시작합니다..")

    not_org_link = search_org_link (stu_json)

    print("\n<네이버 검색 빅데이터 분석>")
    print("검색어: %s" %search_input)
    print("전체 이름수: %s" %len(set(list_org_link)))
    print("전체 건수: %s" % (len(stu_json)-not_org_link))
    print("부정확한 데이터수: %s" %not_org_link)

    resulted = sorted(Counter(list_org_link).items(), key=lambda t: t[1], reverse=True)

    print("\n- 제목 별 블로그 분석")
    for index in resulted :
        print(" >> %s: %s건" %(index[0], index[1]))

main()