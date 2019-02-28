# [참고 사항]
# - API 호출수 25,000회/일로 제한
# - 한번 호출에 최대 100개 검색
# - 한번 실행에 최대 1000개까지 기사 검색
import urllib.request
import datetime
import json

app_id = "ck3_G6VCspzuucVvBCAU"
app_pw = "73Y_5NA4Jc"

def get_request_url (url) :
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id",app_id)
    req.add_header("X-Naver-Client-Secret",app_pw)

    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
            print("[%s] Url:%s => Request Success" %(datetime.datetime.now(), url))
            return response.read().decode('UTF-8')
    except Exception as e :
        print(e)
        print("[%s] Error for URL: %s" %(datetime.datetime.now(),url))
        return None

def getNaversearchResult (sNode,search_text,page_start,display) :
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" %sNode
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(search_text),page_start,display)
    url = base+node+parameters
    retData = get_request_url(url)

    if(retData == None) :
        return None
    else :
        return json.loads(retData)

def getPostData(post, jsonResult) :
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    link = post['link']

    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y  %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'title' :title, 'description':description, 'org_link' :org_link, 'pDate':pDate})
    return

def main() :
    print("=" * 10 + "빅데이터 수집기" + "=" * 10)
    search_input = input("검색어를 입력하세요: ")
    print("외부 빅데이터를 수집합니다.")

    jsonResult=[]

    sNode = 'news'
    search_text = search_input
    display_count = 100

    jsonSearch = getNaversearchResult(sNode, search_text,1,display_count)

    index = 1 # 1번 루프를 돌 때마다 100건이 조회되기 때문에 1000번을 넘기지 않게 하기 위한 인덱스임
    while((jsonSearch!=None) and (jsonSearch['display']!=0) and index < 10) :
        for post in jsonSearch['items'] :
            getPostData(post,jsonResult)

        nStart = jsonSearch['start']+jsonSearch['display']
        jsonSearch = getNaversearchResult(sNode,search_text,nStart,display_count)
        index = index+1

    with open('%s_naver_%s.json' %(search_text,sNode), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,indent=4, sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

    print("'%s_naver_%s.json' 이름으로 분석데이터를 저장합니다." %(search_text,sNode))
    print("추후 분석은 검색기를 통하여 분석하세요.")

if __name__ == '__main__' :
    main()