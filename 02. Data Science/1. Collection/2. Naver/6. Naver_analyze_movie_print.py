import json
import re
from collections import Counter
list_org_link = {}

def search_org_link (stu_json) :
    not_org_link = 0
    for index in range(len(stu_json)) :
        try :
            each_title = stu_json[index]["title"]
            each_rating = stu_json[index]["userRating"]
            list_org_link[each_title] = each_rating
        except :
            not_org_link += 1
    print(len(list_org_link))
    return not_org_link

def main () :
    print("="*10+"빅데이터 분석기"+"="*10)
    search_input = input("분석 키워드를 입력하세요: ")

    with open("%s_naver_movie.json" % search_input, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        stu_json = json.loads(json_string)

    not_to_org = search_org_link(stu_json)
    print("데이터 분석을 시작합니다..")

    print("\n<네이버 검색 빅데이터 분석>")
    print("검색어: %s" %search_input)
    print("전체 추천수: %s" %len(list_org_link))
    print("전체 건수: %s" % (len(stu_json)-not_to_org))
    print("부정확한 데이터수: %s" %not_to_org)

    resulted = sorted(Counter(list_org_link).items(), key=lambda t: t[1], reverse=True)

    print("\n- 제목 별 블로그 분석")
    for index in resulted :
        print(" >> %s: %s점" %(index[0], index[1]))

main()