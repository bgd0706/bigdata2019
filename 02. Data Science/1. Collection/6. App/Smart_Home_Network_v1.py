from Step5_Weather_realtime_info_for_student import get_Realtime_Weather_Info
from selenium import webdriver
from collections import Counter
import time, json, random, csv

g_Radiator = False # 난방기
g_Gas_Valve = False # 가스밸브
g_Balcony_Windows = False # 베란다
g_Door = False # 출입문 상태
g_lamp = False # 조명
g_curtain = False # 커튼
g_speaker = False # 스피커
g_pad = False # 패드
g_ref = False # 냉장고

# 주광색 : 일반 사무실에서 많이 사용되는 색으로 선명하고 차가운 느낌의 백색을 가진 색 (5,701K ~ 7,100K)
# 주백색 : 거실에서 많이 사용하는 색상으로 청색광이 빠져 백색이면서도 차가운 느낌이 없다. (4,501K ~ 5,700K)
# 온백색 : 고급스러우면서 은은한 색상으로 눈이 가장 편하게 느끼는 색상 (3,001K ~ 4,500K)
# 전구색 : 백열전구의 느낌이 나는 색상으로 따뜻하면서 분위기와 편안함을 느낄 수 있습니다. (2,700K ~ 3,000K)

g_AI_Mode = False

presentYear = time.strftime('%Y', time.localtime(time.time()))
presentMonth = time.strftime('%m', time.localtime(time.time()))
presentDay = time.strftime('%d', time.localtime(time.time()))
presentHour = time.strftime('%H', time.localtime(time.time()))
presentMinute = time.strftime('%M', time.localtime(time.time()))
presentSecond = time.strftime('%S', time.localtime(time.time()))

def read_ref() :
    with open('ref_sub.csv', 'r', encoding='utf-8') as f_ref:
        while True :
            line = f_ref.readline().replace("\n","")
            if not line : break
            print("%s (이/가) %s 있습니다." %(line.split(',')[0], line.split(',')[1][:len(line.split(',')[1])]))

def make_food_ref () :
    with open('ref_sub.csv', 'r', encoding='utf-8') as f_ref:
        while True :
            line = f_ref.readline().replace("\n","")
            if not line : break
            print("%s (이/가) %s 있습니다." %(line.split(' ')[0], line.split(' ')[1]))
    search_url = "http://home.ebs.co.kr/cook/board/4/500514/list?bbsId=500514&boardType=2&iframeOn=false&searchCondition=pstCntnSrch&" \
                 "searchKeyword=%s&searchKeywordCondition=1" % line.split(' ')[0]
    driver = webdriver.Chrome('C:\chromedriver')
    driver.implicitly_wait(3)
    driver.get(search_url)

def use_and_update_ref() :
    line = []
    with open('ref_sub.csv', 'r', encoding='utf-8', newline='') as f_ref:
        while True:
            lines = f_ref.readline().replace("\n", "")
            if not lines: break
            line.append(lines)
        while True:
            ingred_to_use = input("어떤 재료를 쓰겠습니까? (안하면 n) ")
            if ingred_to_use == 'n': break
            for i in range(len(line)):
                subject_name = line[i].split(',')[0]
                subject_num = line[i].split(',')[1]
                if ingred_to_use == subject_name[:len(subject_name)]:
                    num_to_now = int(subject_num[:len(subject_num) - 2])  # 현재 냉장고에 있는 재료 수
                    num_to_want = int(input("몇 %s 쓰겠습니까? " % subject_num[len(subject_num) - 2]))  # 쓰고 싶은 재료 수
                    if num_to_want > num_to_now:
                        print("현재 냉장고에 있는 수 보다 많습니다. 다시 선택해주세요.")
                        break
                    num_to_left = num_to_now - num_to_want  # 남는 재료 수
                    with open('ref_sub.csv', 'r', encoding='utf-8', newline='') as f_ref_2:
                        while True:
                            lines = f_ref_2.readline().replace("\n", "")
                            if not lines: break
                            if lines.split(',')[0] == subject_name:
                                lines.replace(lines.split(',')[1][:len(lines.split(',')[1]) - 2], str(num_to_left))
                                print(lines)
                                break
def add_ref () :
    while True :
       add_input = input("추가 하시겠습니까? 재고 수정하시겠습니까? 1. 재고 추가 2. 재고 수정 ")
       if add_input == 1 :
           with open('ref_sub.csv', 'a', encoding='utf-8', newline='') as f_ref:
                add_name = input("품명을 적으세요. (n 하면 종료) ")
                add_num = input("개수를 적으세요 (ex) 3개) ")
                f_ref_writer = csv.writer(f_ref)
                f_ref_writer.writerow([add_name, add_num])
       elif add_input == 2 :
           with open('ref_sub.csv', 'r', encoding='utf-8', newline='') as f_ref:
               add_name = input("재고 수정할 품명을 적어주세요. ")
               add_num = input("개수를 적으세요 (ex) 3개) ")
               while True:
                   lines = f_ref.readline().replace("\n", "")
                   if not lines: break
                   if lines.split(',')[0] == add_name:
                       lines.replace(lines.split(',')[1][:len(lines.split(',')[1])], add_num)

def search_want_music (object_music) :
    search_url = "https://www.melon.com/search/total/index.htm?q=%s&section=&linkOrText=T&ipath=srch_form" %object_music
    driver = webdriver.Chrome('C:\chromedriver')
    driver.implicitly_wait(3)
    driver.get(search_url)

def cal_subway (fm, sub_input) :
    list_minute = []
    lines = csv.reader(f)
    for line in lines:
        if line[0] == presentHour and line[1] > presentMinute:  # 예를 들어 현재 시간이 14시이고, 15시 사이에 2번 이상 도착하는 경우
            list_minute.append(int(line[1]))  # 분을 리스트에 넣는다.
            if len(list_minute) == 2: break  # 리스트의 개수가 2개가 되면 for문 종료
        if line[0] == str(int(presentHour) + 1) and len(list_minute) == 1:  # 현재 시간이 14시인데, 15시 사이에 1번 있는 경우
            if len(list_minute) == 2:
                break
            else:  # 리스트 길이가 0, 1일 때
                if line[0] == str(int(presentHour) + 1):
                    list_minute.append(int(line[1]) + 60)  # 다음 시간의 분을 더해준다.
        if line[0] == str(int(presentHour) + 1) and len(list_minute) == 0:  # 현재 시간이 14시인데, 15시 사이에 열차가 없는 경우
            list_minute.append(int(line[1]) + 60)

    while len(list_minute) != 0:
        if sub_input == 1 :
            print("설화명곡행 열차가 %s분 남았습니다." % str(int(list_minute.pop(0)) - int(presentMinute)))
        elif sub_input == 2 :
            print("안심행 열차가 %s분 남았습니다." % str(int(list_minute.pop(0)) - int(presentMinute)))

def read_weather_info() :
    with open("동구_신암동_초단기예보조회.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        f_json = json.loads(json_string)
    return f_json

def print_main_menu() :
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 행위선택")
    print("5. 프로그램 종료")

def print_device_status(device_name, device_status) :
    print("%s 상태: " %device_name, end="")
    if device_status == True : print("작동")
    else : print("정지")

def check_device_status() :
    print_device_status('난방기', g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문', g_Door)
    print_device_status('조명', g_lamp)
    print_device_status('커튼', g_curtain)
    print_device_status('스피커', g_speaker)
    print_device_status('패드', g_pad)
    print_device_status('냉장고', g_ref)

def print_device_menu() :
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")
    print("5. 조명")
    print("6. 커튼")
    print("7. 스피커")
    print("8. 패드")
    print("9. 냉장고")

def control_device() :
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door, g_lamp, g_curtain, g_speaker, g_ref

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1 : g_Radiator = not g_Radiator
    if menu_num == 2 : g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3 : g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4 : g_Door = not g_Door
    if menu_num == 5 : g_lamp = not g_lamp
    if menu_num == 6 : g_curtain = not g_curtain
    if menu_num == 7 : g_speaker = not g_speaker
    if menu_num == 8 : g_ref = not g_ref

    check_device_status()

def print_weather_info(f_json) :
    print("\n현재 시각은 %s년 %s월 %s일 %s시 %s분 %s초 입니다." % (
        presentYear, presentMonth, presentDay, presentHour, presentMinute, presentSecond))

    len_f = len(f_json)
    presentHour_int = int(presentHour)

    for i in range(len_f):
        if str(f_json[i]["fcstTime"])[0:2] == str(presentHour_int + 1):
            if f_json[i]["category"] == "T1H": # 기온
                print("%s시 기온은 %s℃ 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
            if f_json[i]["category"] == "RN1": # 1시간 강수량
                print("%s시 1시간 강수량은 %smm 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
            if f_json[i]["category"] == "SKY": # 하늘상태
                cloud = f_json[i]["fcstValue"]
                if 0 <= cloud <= 2 : exp_cloud = "맑음"
                elif 3 <= cloud <= 5 : exp_cloud = "구름조금"
                elif 6 <= cloud <= 8 : exp_cloud = "구름많음"
                elif 9 <= cloud <= 10 : exp_cloud ="흐림"
                print("%s시 하늘상태는 %s 일 것으로 예상됩니다." % (presentHour_int + 1, exp_cloud))
            if f_json[i]["category"] == "REH": # 습도
                print("%s시 습도는 %s%% 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
            if f_json[i]["category"] == "PTY": # 강수형태
                precipitation = f_json[i]["fcstValue"]
                if precipitation == 0 : pre_form = "강수없음"
                elif precipitation == 1 : pre_form = "비"
                elif precipitation == 2 : pre_form = "비와 눈"
                elif precipitation == 3 : pre_form = "눈"
                print("%s시 강수형태는 %s 일 것으로 예상됩니다." % (presentHour_int + 1, pre_form))

def ai_person_info() :
    global g_Gas_Valve, g_Door, g_lamp, g_speaker, g_ref, g_curtain

    if behavior == 1 : # 기상
        if g_lamp == True :
            lamp_input = input("조명이 켜져 있습니다. 조명을 끄겠습니까? (y or n) ")
            if lamp_input == 'y' :
                g_lamp = not g_lamp
        elif g_lamp == False :
            lamp_input = input("조명을 켜겠습니까? (y or n) ")
            if lamp_input == 'y' :
                print("조명이 켜졌습니다.")
                g_lamp = not g_lamp
        if g_speaker == False :
            speaker_input_false = input("스피커를 키겠습니까? (y or n) ")
            if speaker_input_false == 'y' :
                print("스피커가 켜졌습니다.")
                g_speaker = not g_speaker
                music_input = input("아침에 듣기 좋은 음악을 트시겠습니까? (y or n) ")
                if music_input == 'y':
                    search_want_music("아침에 듣기 좋은 음악")
                else:
                    music_input = input("다른 음악을 트시겠습니까? (y or n) ")
                    if music_input == 'y':
                        music_input_input = input("듣고싶은 음악을 적어주세요.(실제로는 불러주세요) ")
                        search_want_music(music_input_input)
        elif g_speaker == True :
            speaker_input_true = input("스피커가 켜져 있습니다. 스피커를 끄겠습니까? (y or n) ")
            if speaker_input_true == 'y' :
                print("스피커를 끄겠습니다.")
                g_speaker = not g_speaker
            else :
                music_input = input("아침에 듣기 좋은 음악을 트시겠습니까? (y or n) ")
                if music_input == 'y' :
                    search_want_music("아침에 듣기 좋은 음악")
                else :
                    music_input = input("다른 음악을 트시겠습니까? (y or n) ")
                    if music_input == 'y' :
                        music_input_input = input("듣고싶은 음악을 적어주세요.(실제로는 불러주세요) ")
                        search_want_music(music_input_input)
        if g_curtain == False :
            curtain_input = input("커튼을 펼치겠습니까? (y or n) ")
            if curtain_input == 'y' :
                print("커튼이 펼쳐졌습니다.")
                g_curtain = not g_curtain
        elif g_curtain == True :
            curtain_input = input("커튼을 치겠습니까? (y or n) ")
            if curtain_input == 'y':
                print("커튼이 쳐졌습니다.")
                g_curtain = not g_curtain
    elif behavior == 2  : # 외출
        if g_Gas_Valve == True :
            print("현재 외출중입니다. 하지만 가스밸브가 열어져 있습니다. 잠그겠습니다.")
            g_Gas_Valve = not g_Gas_Valve
        if g_Door == True :
            print("현재 외출중입니다. 하지만 현관문은 잠그지 않으셨습니다. 잠그겠습니다.")
            g_Door = not g_Door
        if g_lamp == True :
            print("현재 외출중입니다. 하지만 조명은 켜져 있습니다. 끄겠습니다.")
            g_lamp = not g_Door
        if g_speaker == True :
            print("현재 외출중입니다. 하지만 스피커는 커져 있습니다. 끄겠습니다.")
            g_speaker = not g_speaker
        if g_curtain == True :
            curtain_input = input("커튼을 치겠습니까? (y or n) ")
            if curtain_input == 'y':
                print("커튼이 치졌습니다.")
                g_curtain = not g_curtain
    elif behavior == 3 : # 귀가
        if g_lamp == True:
            lamp_input = input("조명이 켜져 있습니다. 조명을 끄겠습니까? (y or n) ")
            if lamp_input == 'y':
                g_lamp = not g_lamp
        elif g_lamp == False:
            lamp_input = input("조명을 켜겠습니까? (y or n) ")
            if lamp_input == 'y':
                print("조명이 켜졌습니다.")
                g_lamp = not g_lamp
        if g_speaker == False :
            speaker_input_false = input("스피커를 키겠습니까? (y or n) ")
            if speaker_input_false == 'y' :
                print("스피커가 켜졌습니다.")
                g_speaker = not g_speaker
                music_input = int(input("어떤 기분이십니까? (1. 즐거움/기쁨 2. 씁쓸/슬픔 3. 화남) "))
                if music_input == 1:
                    search_want_music("최신 클럽 음악")
                elif music_input == 2:
                    search_want_music("슬픈 음악")
                elif music_input == 3:
                    search_want_music("클래식")
                else:
                    music_input = input("다른 음악을 들으시겠습니까? (y or n) ")
                    if music_input == 'y' :
                        music_input_input = input("어떤 음악을 듣고 싶은지 적어주세요(실제로는 불러주세요) ")
                        search_want_music(music_input_input)
        elif g_speaker == True :
            speaker_input_true = input("스피커가 켜져 있습니다. 스피커를 끄겠습니까? (y or n) ")
            if speaker_input_true == 'y' :
                print("스피커를 끄겠습니다.")
                g_speaker = not g_speaker
            else :
                music_input = int(input("어떤 기분이십니까? (1. 즐거움/기쁨 2. 씁쓸/슬픔 3. 화남) "))
                if music_input == 1:
                    search_want_music("최신 클럽 음악")
                elif music_input == 2:
                    search_want_music("슬픈 음악")
                elif music_input == 3:
                    search_want_music("클래식")
                else:
                    music_input = input("다른 음악을 들으시겠습니까? (y or n) ")
                    if music_input == 'y':
                        music_input_input = input("어떤 음악을 듣고 싶은지 적어주세요(실제로는 불러주세요) ")
                        search_want_music(music_input_input)
        if g_curtain == False:
            curtain_input = input("커튼을 펼치겠습니까? (y or n) ")
            if curtain_input == 'y':
                print("커튼이 펼쳐졌습니다.")
                g_curtain = not g_curtain
        elif g_curtain == True:
            curtain_input = input("커튼을 치겠습니까? (y or n) ")
            if curtain_input == 'y':
                print("커튼이 쳐졌습니다.")
                g_curtain = not g_curtain
    elif behavior == 4 : # 식사
        if g_lamp == True:
            lamp_input = input("조명이 켜져 있습니다. 조명을 끄겠습니까? (y or n) ")
            if lamp_input == 'y':
                g_lamp = not g_lamp
        elif g_lamp == False:
            lamp_input = input("조명을 켜겠습니까? (y or n) ")
            if lamp_input == 'y':
                print("조명이 켜졌습니다.")
                g_lamp = not g_lamp
        if g_speaker == False :
            speaker_input_false = input("스피커를 키겠습니까? (y or n) ")
            if speaker_input_false == 'y' :
                print("스피커가 켜졌습니다.")
                g_speaker = not g_speaker
                music_input = int(input("밥 먹을 때 듣기 좋은 음악을 들으시겠습니까? (y or n) "))
                if music_input == 'y' :
                    search_want_music("밥 먹을 때 듣기 좋은 음악")
                else:
                    music_input = input("다른 음악을 들으시겠습니까? (y or n) ")
                    if music_input == 'y' :
                        music_input_input = input("어떤 음악을 듣고 싶은지 적어주세요(실제로는 불러주세요) ")
                        search_want_music(music_input_input)
        elif g_speaker == True :
            speaker_input_true = input("스피커가 켜져 있습니다. 스피커를 끄겠습니까? (y or n) ")
            if speaker_input_true == 'y' :
                print("스피커를 끄겠습니다.")
                g_speaker = not g_speaker
            else :
                music_input = int(input("밥 먹을 때 듣기 좋은 음악을 들으시겠습니까? (y or n) "))
                if music_input == 'y':
                    search_want_music("밥 먹을 때 듣기 좋은 음악")
                else:
                    music_input = input("다른 음악을 들으시겠습니까? (y or n) ")
                    if music_input == 'y':
                        music_input_input = input("어떤 음악을 듣고 싶은지 적어주세요(실제로는 불러주세요) ")
                        search_want_music(music_input_input)
        if g_curtain == False:
            curtain_input = input("커튼을 펼치겠습니까? (y or n) ")
            if curtain_input == 'y':
                print("커튼이 펼쳐졌습니다.")
                g_curtain = not g_curtain
        elif g_curtain == True:
            curtain_input = input("커튼을 치겠습니까? (y or n) ")
            if curtain_input == 'y':
                print("커튼이 쳐졌습니다.")
                g_curtain = not g_curtain

    elif behavior == 5 : # 목욕
        pass
    elif behavior == 6 : # TV 보기
        pass
    elif behavior == 7 : # 음악
        pass
    elif behavior == 8 : # 독서
        pass
    elif behavior == 8 : # 수면
        if g_lamp == True :
            print("조명이 꺼졌습니다.")
            g_lamp = not g_lamp

def ai_weather_info(f_json) :
    global g_Radiator, g_Balcony_Windows, g_curtain, g_speaker, g_ref

    len_f = len(f_json)
    presentHour_int = int(presentHour)

    for i in range(len_f):
        if str(f_json[i]["fcstTime"])[0:2] == str(presentHour_int + 1):
            if f_json[i]["category"] == "T1H": # 기온
                if g_Radiator == False:
                    if f_json[i]["fcstValue"] >= 23 :
                        accept = input("현재 난방기가 꺼져 있습니다. 현재 기온이 23도 이상이므로 난방기를 켜도 괜찮겠습니까? (y or n) ")
                        if accept == 'y':
                            g_Radiator = not g_Radiator
                            print("난방기가 켜졌습니다.")
                else :
                    if f_json[i]["fcstValue"] <= 18 :
                        accept = input("현재 난방기가 켜져 있습니다. 현재 기온이 18도 이하이므로 난방기를 꺼도 괜찮겠습니까? (y or n) ")
                        if accept == 'y':
                            g_Radiator = not g_Radiator
                            print("난방기가 꺼졌습니다.")
            if f_json[i]["category"] == "REH": # 습도
                moi = f_json[i]["fcstValue"]
                if g_Balcony_Windows == False :
                    if moi <= 30 :
                        accept = input("현재 창문이 닫혀 있습니다. 현재 습도가 30% 이하이므로 창문을 열어도 괜찮겠습니까? (y or n) ")
                        if accept == 'y':
                            g_Balcony_Windows = not g_Balcony_Windows
                            print("창문을 열었습니다.")
                else :
                    if moi >= 60 :
                        accept = input("현재 창문이 열어져 있습니다. 현재 습도가 60% 이하이므로 창문을 닫아도 괜찮겠습니까? (y or n) ")
                        if accept == 'y':
                            g_Balcony_Windows = not g_Balcony_Windows
                            print("창문을 닫았습니다.")

            if f_json[i]["category"] == "PTY": # 강수형태
                precipitation = f_json[i]["fcstValue"]
                if g_Balcony_Windows == True :
                    if precipitation != 0 :
                        accept = input("현재 창문이 열어져 있습니다. 현재 비 또는 눈이 내리므로 창문을 닫아도 괜찮겠습니까? (y or n) ")
                        if accept == 'y':
                            g_Balcony_Windows = not g_Balcony_Windows
                            print("창문을 닫았습니다.")
            if f_json[i]["category"] == "SKY": # 하늘상태
                cloud = f_json[i]["fcstValue"]
                if 0 <= cloud <= 2 :
                    if g_curtain == False :
                        accept = input("현재 커튼이 닫혀져 있습니다. 현재 맑으므로 커튼을 쳐도 괜찮겠습니까? (y or n) ")
                        if accept == "y" :
                            g_curtain = not g_curtain
                            print("커튼을 쳤습니다.")

def smart_mode() :
    global g_AI_Mode

    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    print("4. 실시간 기상정보 확인")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1 : # 인공지능 모드 조회
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else : print("중지")

    if menu_num == 2 : # 인공지능 모드 상태 변경
        if g_AI_Mode == True :
            print("현재 인공지능 모드가 작동하고 있습니다.")
            print("중지하였습니다.")
        else :
            print("현재 인공지능 모드가 작동하고 있지 않습니다.")
            print("작동하겠습니다.")
        g_AI_Mode = not g_AI_Mode

    elif menu_num == 3 : # 실시간 기상정보 Update
        get_Realtime_Weather_Info()

    elif menu_num == 4 : # 실시간 기상정보 확인
        print_weather_info(read_weather_info())

def do_behavior(behavior) :
    global g_AI_Mode

    if behavior == 1 : # 기상 - 기상했을 때 자동적으로 업데이트
        pass

    elif behavior == 2 : # 출근/외출
        look_sub_time = input("동구청 지하철 시간표를 확인하시겠습니까? (y or n) ")
        if (look_sub_time == 'y'):
            sub_input = int(input("1. 설화명곡행 2. 안심행 (1 or 2) "))
            if sub_input == 1:
                f = open('subway_sulhwa.csv', 'r')
            elif sub_input == 2:
                f = open('subway_ansim.csv', 'r')
            cal_subway(f, sub_input)
    elif behavior == 3 : # 귀가
        pass
    elif behavior == 4 : # 식사
        while True :
            do_ref = int(input("식사와 관련된 행동을 하시겠습니까? 1: 냉장고 리스트 확인 2: 레시피 보기 3: 재고 수정 4: 재고 추가 5: 종료 "))
            if do_ref == 1 :
                read_ref()
            elif do_ref == 2 :
                make_food_ref()
            elif do_ref == 3 :
                read_ref()
                use_and_update_ref()
            elif do_ref == 4 :
                read_ref()
                add_ref()
            elif do_ref == 5 :
                break
    elif behavior == 5 : # 목욕
        pass
    elif behavior == 6 : # TV 보기
        pass
    elif behavior == 7 : # 음악
        pass
    elif behavior == 8 : # 독서
        pass
    elif behavior == 9 : # 수면
        pass

    get_Realtime_Weather_Info()
    ai_weather_info(read_weather_info())
    ai_person_info()

print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("                             - 박규동 -")


while True :
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1) :
        check_device_status()
    elif(menu_num == 2) :
        control_device()
    elif(menu_num == 3) :
        smart_mode()
    elif(menu_num == 4) :
        behavior = int(input("현재 당신은 무엇을 하고 있습니까? (1. 기상 2. 출근/외출 3. 귀가 4. 식사 5. 목욕 6. TV 보기 7. 음악"
                             "8. 독서 9. 수면) "))
        do_behavior(behavior)
    else :
        break