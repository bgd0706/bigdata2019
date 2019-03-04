from Step5_Weather_realtime_info_for_student import get_Realtime_Weather_Info
import time, json

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False

def print_main_menu() :
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 프로그램 종료")

def print_device_status(device_name, device_status) :
    print("%s 상태: " %device_name, end="")
    if device_status == True : print("작동")
    else : print("정지")

def check_device_status() :
    print_device_status('난방기', g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)

def print_device_menu() :
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")

def control_device() :
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1 : g_Radiator = not g_Radiator
    if menu_num == 2 : g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3 : g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4 : g_Door = not g_Door

    check_device_status()

def get_realtime_weather_info() :
    get_Realtime_Weather_Info()

def get_json_weather_info() :
    presentYear = time.strftime('%Y', time.localtime(time.time()))
    presentMonth = time.strftime('%m', time.localtime(time.time()))
    presentDay = time.strftime('%d', time.localtime(time.time()))
    presentHour = time.strftime('%H', time.localtime(time.time()))
    presentMinute = time.strftime('%M', time.localtime(time.time()))
    presentSecond = time.strftime('%S', time.localtime(time.time()))

    print("현재 시각은 %s년 %s월 %s일 %s시 %s분 %s초 입니다." % (
        presentYear, presentMonth, presentDay, presentHour, presentMinute, presentSecond))

    with open("동구_신암동_초단기예보조회.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        f_json = json.loads(json_string)

    len_f = len(f_json)
    presentHour_int = int(presentHour)
    presentMinute_int = int(presentMinute)

    if 0 <= presentMinute_int <= 30:  # 현재 시간이 0분에서 30분 일 때
        for i in range(len_f):
            if str(f_json[i]["fcstTime"])[0:2] == presentHour:
                if f_json[i]["category"] == "T1H":
                    print("현재 기온은 %s℃ 입니다." % f_json[i]["fcstValue"])
                if f_json[i]["category"] == "RN1":
                    print("현재 1시간 강수량은 %smm 입니다." % f_json[i]["fcstValue"])
                if f_json[i]["category"] == "SKY":
                    print("현재 하늘상태는 %s 입니다." % f_json[i]["fcstValue"])
                if f_json[i]["category"] == "UUU":
                    print("현재 동서풍은 %sm/s 입니다." % f_json[i]["fcstValue"])
                if f_json[i]["category"] == "VVV":
                    print("현재 남북풍은 %sm/s 입니다." % f_json[i]["fcstValue"])
                if f_json[i]["category"] == "REH":
                    print("현재 습도는 %s%% 입니다." % f_json[i]["fcstValue"])
                if f_json[i]["category"] == "PTY":
                    print("현재 강수형태는 %s 입니다." % f_json[i]["fcstValue"])
                if f_json[i]["category"] == "LGT":
                    print("현재 낙뢰는 %s 입니다." % f_json[i]["fcstValue"])
                if f_json[i]["category"] == "VEC":
                    print("현재 풍향은 %s 입니다." % f_json[i]["fcstValue"])
                if f_json[i]["category"] == "WSD":
                    print("현재 풍속은 %s 입니다." % f_json[i]["fcstValue"])
    else:  # 현재 시간이 31분에서 59분 일 때
        for i in range(len_f):
            if presentHour_int == 23:
                if str(f_json[i]["fcstTime"])[0:2] == '00':
                    if f_json[i]["category"] == "T1H":
                        print("00시 기온은 %s℃ 일 것으로 예상됩니다." % f_json[i]["fcstValue"])
                    if f_json[i]["category"] == "RN1":
                        print("00시 1시간 강수량은 %smm 일 것으로 예상됩니다." % f_json[i]["fcstValue"])
                    if f_json[i]["category"] == "SKY":
                        print("00시 하늘상태는 %s 일 것으로 예상됩니다." % f_json[i]["fcstValue"])
                    if f_json[i]["category"] == "UUU":
                        print("00시 동서풍은 %sm/s 일 것으로 예상됩니다." % f_json[i]["fcstValue"])
                    if f_json[i]["category"] == "VVV":
                        print("00시 남북풍은 %sm/s 일 것으로 예상됩니다." % f_json[i]["fcstValue"])
                    if f_json[i]["category"] == "REH":
                        print("00시 습도는 %s%% 일 것으로 예상됩니다." % f_json[i]["fcstValue"])
                    if f_json[i]["category"] == "PTY":
                        print("00시 강수형태는 %s 일 것으로 예상됩니다." % f_json[i]["fcstValue"])
                    if f_json[i]["category"] == "LGT":
                        print("00시 낙뢰는 %s 일 것으로 예상됩니다." % f_json[i]["fcstValue"])
                    if f_json[i]["category"] == "VEC":
                        print("00시 풍향은 %s 일 것으로 예상됩니다." % f_json[i]["fcstValue"])
                    if f_json[i]["category"] == "WSD":
                        print("00시 풍속은 %s 일 것으로 예상됩니다." % f_json[i]["fcstValue"])
            else:
                if str(f_json[i]["fcstTime"])[0:2] == str(presentHour_int + 1):
                    if f_json[i]["category"] == "T1H":
                        print("%s시 기온은 %s℃ 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
                    if f_json[i]["category"] == "RN1":
                        print("%s시 1시간 강수량은 %smm 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
                    if f_json[i]["category"] == "SKY":
                        print("%s시 하늘상태는 %s 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
                    if f_json[i]["category"] == "UUU":
                        print("%s시 동서풍은 %sm/s 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
                    if f_json[i]["category"] == "VVV":
                        print("%s시 남북풍은 %sm/s 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
                    if f_json[i]["category"] == "REH":
                        print("%s시 습도는 %s%% 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
                    if f_json[i]["category"] == "PTY":
                        print("%s시 강수형태는 %s 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
                    if f_json[i]["category"] == "LGT":
                        print("%s시 낙뢰는 %s 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
                    if f_json[i]["category"] == "VEC":
                        print("%s시 풍향은 %s 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
                    if f_json[i]["category"] == "WSD":
                        print("%s시 풍속은 %s 일 것으로 예상됩니다." % (presentHour_int + 1, f_json[i]["fcstValue"]))
def smart_mode() :
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1 : # 인공지능 모드 조회
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else : print("중지")

    if menu_num == 2 : # 인공지능 모드 상태 변경
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True:
            print("작동\n")
            get_json_weather_info()
        else:
            print("중지")

    elif menu_num == 3 : # 실시간 기상정보 Update
        get_realtime_weather_info()

print("<스마트 홈네트워크 시뮬레이션 프로그램 ver 1.0>")
print("                             - 박규동 -")
Step5_Weather_realtime_info_for_student.get_Realtime_Weather_Info()
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
        break


