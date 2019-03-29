import urllib.request, datetime
import xml.etree.ElementTree as ET

access_key = "XtvjsQxlsgO41hz7VcZ3PmLekszkSNs2bpmvNTR%2Fn3VJ9uy6sI3jd%2B8RmLgU3vI5%2FpTae%2BoYpWSP4MKtixEHAw%3D%3D"

def get_Request_URL (url) : # (1) 통합대기환경 정보(대기오염정보 조회 서비스)
    req = urllib.request.Request(url)
    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 :
           # print("[%s] Url Request Success" %datetime.datetime.now())
           return response.read().decode("UTF-8")
    except Exception as e :
        print(e)
        # print(" [%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def get_Dust_URL () : # 대기오염 정보 (대기오염정보 조회 서비스) request 보내기 전, url 만드는 함수
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?serviceKey=" + access_key
    parameters += "&numOfRows=160"
    parameters += "&pageNo=1"
    parameters += "&sidoName=" + urllib.parse.quote_plus("대구")
    parameters += "&ver=1.3"

    url = end_point + parameters

    retData = get_Request_URL(url)
    if (retData == None) :
        return None
    else :
        return retData

def Make_Dust_Xml() : # (1) 대기오염정보 (대기오염정보 조회 서비스) xml 파일 생성하는 함수
    xmlData = get_Dust_URL()
    tree = ET.ElementTree(ET.fromstring(xmlData)) # str으로 가져오기 때문에 Tree형태로 만들어줘야함
    root = tree.getroot()
    for i in root.getiterator("body") :
        for j in i.getiterator("items") :
           dust_list = j.findall("item")
           for i in range(len(dust_list)) :
               if dust_list[i].findtext("stationName") == "신암동" :
                   return dust_list[i].findtext("khaiGrade")

if __name__ == "__main__" :
    Make_Dust_Xml()