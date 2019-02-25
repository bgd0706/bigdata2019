import json, os

def digit(x): # x를 기준으로 3만큼 오른쪽 정렬하고, 빈 곳은 0으로 치환
   return "{0:0>3}".format(x)

def start(stu_json) :
    while True :
        print("="*30)
        print("JSON 기반 학생 정보 관리 프로그램")
        print("="*30)
        print("1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n4. 학생정보 삭제\n5. 프로그램 종료")
        print(" ")
        menu_input = int(input("메뉴를 선택하세요: "))
        if (menu_input == 1) : # 학생 정보입력
            print("="*10+"1. 학생 정보 입력 화면"+"="*10)
            add_index = len(stu_json) # Dictionary list 리스트 길이 반환
            if add_index == 0 : # 리스트가 하나도 없으면
                id_number = "000" # 0부터 시작
            else : # 리스트가 하나라도 있으면
                id_number = stu_json[add_index-1]["student_ID"][3:]
            add_student_ID = 'ITT' + (digit(int(id_number) + 1))
            add_name = input("이름(예: 홍길동): ")
            add_age = int(input("나이(예: 29): "))
            add_address = input("주소(예: 대구광역시 동구 아양로 135): ")
            add_num_learned = int(input("과거 수강 횟수(예: 1): "))
            stu_json.append({"address" : add_address, "student_ID" : add_student_ID, "student_age" : add_age, "student_name" : add_name,
                             "total_course_info" : {"learning_course_info" : [],"num_of_course_learned" : add_num_learned}})
            add_confirm_learning = input("현재 수강 과목이 있습니까? (예: y/n): ")
            while add_confirm_learning == 'y' : # 현재 수강 과목이 없다고 할 때까지
                add_course_code = input("강의코드 (예: IB171106, OB0104 ..): ")
                add_course_name = input("강의명 (예: IOT 빅데이터 실무반): ")
                add_teacher = input("강사 (예: 이현구): ")
                add_open_date = input("개강일 (예: 2017-11-06): ")
                add_close_date = input("종료일 (예: 2018-09-05): ")
                add_info = {"close_date" : add_close_date, "course_code" : add_course_code, "course_name" : add_course_name,
                            "open_date" : add_open_date, "teacher" : add_teacher} # 현재 수강 과목 value에도 Dictionary가 있으므로
                stu_json[add_index]["total_course_info"]["learning_course_info"].append(add_info)
                add_confirm_learning = input("현재 수강하는 과목이 더 있습니까 (y/n): ")
                if add_confirm_learning == 'n' :
                    break
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(stu_json, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json SAVED')

        elif (menu_input == 2) : # 학생 정보조회
            print("""
            1. 전체 학생정보조회
             <검색 조건 선택>
            2. ID 검색
            3. 이름 검색
            4. 나이 검색
            5. 주소 검색
            6. 과거 수강 횟수 검색
            7. 현재 강의를 수강중인 학생
            8. 현재 수강 중인 강의명
            9. 현재 수강 중인 강의명
            10. 이전메뉴
            """)
            read_menu_input = int(input("메뉴를 선택하세요: "))
            if read_menu_input == 1 :
                for i in range(len(stu_json)) :
                    print("="*15+"%s번째 학생" %(i+1)+"="*15)
                    print("* 학생 ID: %s" %stu_json[i]["student_ID"])
                    print("* 이름 : %s" %stu_json[i]["student_name"])
                    print("* 나이 : %s" %stu_json[i]["student_age"])
                    print("* 주소 : %s" %stu_json[i]["address"])
                    print("* 수강 정보 ")
                    print(" + 과거 수강 횟수 : %s" %stu_json[i]["total_course_info"]["num_of_course_learned"])
                    if len(stu_json[i]["total_course_info"]["learning_course_info"])== 0 :
                        print(" + 현재 수강 과목 없음")
                    else :
                        print(" + 현재 수강 과목 ")
                        for j in range(len(stu_json[i]["total_course_info"]["learning_course_info"])) : # 현재 수강 과목 리스트 길이
                            print("-" * 15 + "%s번째 강의" %(j+1)+"-"*15)
                            print("  강의 코드 : %s" %stu_json[i]["total_course_info"]["learning_course_info"][j]["course_code"])
                            print("  강의명 : %s" %stu_json[i]["total_course_info"]["learning_course_info"][j]["course_name"])
                            print("  강사 : %s" %stu_json[i]["total_course_info"]["learning_course_info"][j]["teacher"])
                            print("  개강일 : %s" %stu_json[i]["total_course_info"]["learning_course_info"][j]["open_date"])
                            print("  종료일 : %s" %stu_json[i]["total_course_info"]["learning_course_info"][j]["close_date"])
            elif read_menu_input == 10 :
                pass
            else:
                saved_number = []
                search_obj = input("검색어를 입력하세요: ")
                if read_menu_input == 2 : # ID 검색
                    for i in range(len(stu_json)) :
                        if search_obj in stu_json[i]["student_ID"] :
                            saved_number.append(i)
                elif read_menu_input == 3 : # 이름 검색
                    for i in range(len(stu_json)) :
                        if search_obj in stu_json[i]["student_name"] :
                            saved_number.append(i)
                elif read_menu_input == 4 : # 나이 검색
                    for i in range(len(stu_json)) :
                        if search_obj in str(stu_json[i]["student_age"]) :
                            saved_number.append(i)
                elif read_menu_input == 5 : # 주소 검색
                    for i in range(len(stu_json)) :
                        if search_obj in str(stu_json[i]["address"]) :
                            saved_number.append(i)
                elif read_menu_input == 6 : # 과거 수강 횟수 검색
                    for i in range(len(stu_json)) :
                        if search_obj in str(stu_json[i]["total_course_info"]["num_of_course_learned"]) :
                            saved_number.append(i)
                elif read_menu_input == 7 : # 현재 강의를 수강중인 학생
                    for i in range(len(stu_json)) :
                        for j in range(len(stu_json[i]["total_course_info"]["learning_course_info"])) :
                            if search_obj in stu_json[i]["total_course_info"]["learning_course_info"][j]["course_code"] :
                                saved_number.append(i)
                elif read_menu_input == 8 :  # 현재 강의를 수강중인 강의명
                    for i in range(len(stu_json)):
                        for j in range(len(stu_json[i]["total_course_info"]["learning_course_info"])):
                            if search_obj in stu_json[i]["total_course_info"]["learning_course_info"][j]["course_name"]:
                                saved_number.append(i)
                elif read_menu_input == 9 :  # 현재 수강 강사
                    for i in range(len(stu_json)):
                        for j in range(len(stu_json[i]["total_course_info"]["learning_course_info"])):
                            if search_obj in stu_json[i]["total_course_info"]["learning_course_info"][j]["teacher"]:
                                saved_number.append(i)

                set_saved_number = set(saved_number)
                number_standard = len(set_saved_number)
                if number_standard == 1 : # 검색 결과가 하나 일 때
                    print("1개의 결과가 검색되었습니다.")
                    for index in range(number_standard) :
                        stu = saved_number[index]
                        print("* 학생 ID: %s" %stu_json[stu]["student_ID"])
                        print("* 이름: %s" %stu_json[stu]["student_name"])
                        print("* 나이: %s" %stu_json[stu]["student_age"])
                        print("* 주소: %s" %stu_json[stu]["address"])
                        print("* 수강정보")
                        print(" + 과거 수강 횟수: %s" %stu_json[stu]["total_course_info"]["num_of_course_learned"])
                        print(" + 현재 수강 과목")
                        for j in range(len(stu_json[stu]["total_course_info"]["learning_course_info"])) :
                            print("-" * 15 + "%s번째 강의" % (j + 1) + "-" * 15)
                            print("  강의 코드: %s" %stu_json[stu]["total_course_info"]["learning_course_info"][j]["course_code"])
                            print("  강의명: %s" %stu_json[stu]["total_course_info"]["learning_course_info"][j]["course_name"])
                            print("  강사: %s" %stu_json[stu]["total_course_info"]["learning_course_info"][j]["teacher"])
                            print("  개강일: %s" %stu_json[stu]["total_course_info"]["learning_course_info"][j]["open_date"])
                            print("  종료일: %s" %stu_json[stu]["total_course_info"]["learning_course_info"][j]["close_date"])
                else : # 여러 경우 일 때
                    print("복수(%s)개의 결과가 검색되었습니다." %number_standard)
                    print(" ----- 요약결과 -----")
                    for index in range(number_standard) :
                        stu = saved_number[index]
                        print(">> 학생 ID: %s, 학생 이름: %s" %(stu_json[stu]["student_ID"],stu_json[stu]["student_name"]))

        elif menu_input == 3 : # 학생 정보수정
            ID_to_update = input("수정할 학생 ID를 입력하세요: ")
            menu_input_to_update = int(input("1. 학생 이름\n2. 나이\n3. 주소\n4. 과거 수강 횟수\n5. 현재 수강 중인 강의 정보\n0. 이전메뉴\n : "))
            if menu_input_to_update != 5 : value_to_update = input("변경할 값을 입력하세요: ")
            for stu in range(len(stu_json)):
                if ID_to_update == stu_json[stu]["student_ID"] : break
            if menu_input_to_update == 1 :
                stu_json[stu]["student_name"] = value_to_update
            elif menu_input_to_update == 2 :
                stu_json[stu]["student_age"] = int(value_to_update)
            elif menu_input_to_update == 3 :
                stu_json[stu]["student_address"] = value_to_update
            elif menu_input_to_update == 4 :
                stu_json[stu]["total_course_info"]["num_of_course_learned"] = int(value_to_update)
            elif menu_input_to_update == 5 :
                if len(stu_json[stu]["total_course_info"]["learning_course_info"])== 0 :
                    add_confirm_learning = input("현재 수강 과목이 있습니까? (예: y/n): ")
                    while add_confirm_learning == 'y':
                        add_course_code = input("강의코드 (예: IB171106, OB0104 ..): ")
                        add_course_name = input("강의명 (예: IOT 빅데이터 실무반): ")
                        add_teacher = input("강사 (예: 이현구): ")
                        add_open_date = input("개강일 (예: 2017-11-06): ")
                        add_close_date = input("종료일 (예: 2018-09-05): ")
                        add_info = {"close_date": add_close_date, "course_code": add_course_code,
                                    "course_name": add_course_name,
                                    "open_date": add_open_date, "teacher": add_teacher}
                        stu_json[stu]["total_course_info"]["learning_course_info"].append(add_info)
                        add_confirm_learning = input("현재 수강하는 과목이 더 있습니까 (y/n): ")
                        if add_confirm_learning == 'n':
                            break
                else :
                    learning_menu_input_to_update = int(input("1. 강의 코드\n2. 강의명\n3. 강사\n4. 개강일\n5. 종료일\n0. 취소\n : "))
                    num_learning_to_update = len(stu_json[stu]["total_course_info"]["learning_course_info"])
                    if num_learning_to_update == 1 :
                        learning_value_to_update = input("변경할 값을 입력하세요: ")
                        if learning_menu_input_to_update == 1 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][0]["course_code"] = learning_value_to_update
                        elif learning_menu_input_to_update == 2 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][0]["course_name"] = learning_value_to_update
                        elif learning_menu_input_to_update == 3 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][0]["teacher"] = learning_value_to_update
                        elif learning_menu_input_to_update == 4 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][0]["open_date"] = learning_value_to_update
                        elif learning_menu_input_to_update == 5 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][0]["close_date"] = learning_value_to_update
                        elif learning_menu_input_to_update == 0 :
                            break
                    else :
                        what_num = input("몇번째 강의를 변경하시겠습니까")
                        learning_value_to_update = input("변경할 값을 입력하세요: ")
                        if learning_menu_input_to_update == 1 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][what_num-1]["course_code"] = learning_value_to_update
                        elif learning_menu_input_to_update == 2 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][what_num-1]["course_name"] = learning_value_to_update
                        elif learning_menu_input_to_update == 3 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][what_num-1]["teacher"] = learning_value_to_update
                        elif learning_menu_input_to_update == 4 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][what_num-1]["open_date"] = learning_value_to_update
                        elif learning_menu_input_to_update == 5 :
                            stu_json[stu]["total_course_info"]["learning_course_info"][what_num-1]["close_date"] = learning_value_to_update
                        elif learning_menu_input_to_update == 0 :
                            break
            print("* 학생 ID: %s" % stu_json[stu]["student_ID"])
            print("* 이름 : %s" % stu_json[stu]["student_name"])
            print("* 나이 : %s" % stu_json[stu]["student_age"])
            print("* 주소 : %s" % stu_json[stu]["address"])
            print("* 수강 정보 ")
            print(" + 과거 수강 횟수 : %s" % stu_json[stu]["total_course_info"]["num_of_course_learned"])

            if len(stu_json[stu]["total_course_info"]["learning_course_info"]) == 0 :
                print(" + 현재 수강 과목 없음 ")
            else :
                for j in range(len(stu_json[stu]["total_course_info"]["learning_course_info"])):
                    print("-" * 15 + "%s번째 강의" %(j+1)+"-"*15)
                    print("  강의 코드 : %s" % stu_json[stu]["total_course_info"]["learning_course_info"][j]["course_code"])
                    print("  강의명 : %s" % stu_json[stu]["total_course_info"]["learning_course_info"][j]["course_name"])
                    print("  강사 : %s" % stu_json[stu]["total_course_info"]["learning_course_info"][j]["teacher"])
                    print("  개강일 : %s" % stu_json[stu]["total_course_info"]["learning_course_info"][j]["open_date"])
                    print("  종료일 : %s" % stu_json[stu]["total_course_info"]["learning_course_info"][j]["close_date"])

            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(stu_json, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json MODIFIED')

        elif menu_input == 4 : # 학생 정보삭제
            ID_to_remove = input("삭제할 학생 ID를 입력하세요: ")
            menu_input_to_remove = int(input("삭제 유형을 선택하세요.\n1. 전체 선택\n2. 현재 수강 중인 특정 과목정보 삭제\n3. 이전 메뉴\n메뉴 번호를 선택하세요: "))
            for stu in range(len(stu_json)):
                if ID_to_remove == stu_json[stu]["student_ID"]: break
            if menu_input_to_remove == 1 :
                del stu_json[stu]
            elif menu_input_to_remove == 2 :
                if len(stu_json[stu]["total_course_info"]["learning_course_info"]) == 1  :
                    stu_json[stu]["total_course_info"]["learning_course_info"] = [] #del을 하면 key도 없어지기 때문에 빈 리스트로
                elif len(stu_json[stu]["total_course_info"]["learning_course_info"]) == 0 :
                    print("삭제할 강의가 없습니다.")
                else :
                    learning_ID_to_remove = input("삭제할 강의코드를 적으세요: ")
                    for j in range(len(stu_json[stu]["total_course_info"]["learning_course_info"])) :
                        if learning_ID_to_remove == stu_json[stu]["total_course_info"]["learning_course_info"][j]["course_code"] :
                            del stu_json[stu]["total_course_info"]["learning_course_info"][j]
                            break
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(stu_json, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json REMOVED')

        elif menu_input == 5 : # 프로그램 종료
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(stu_json, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json SAVED')
            break

def read_content () :
    try :
        with open("ITT_Student.json", encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            stu_json = json.loads(json_string)
        start(stu_json)

    except FileNotFoundError :
        print("기존파일을 찾을 수 없습니다. 아래 중 선택하세요.")
        choice = int(input("1. 새로운 파일 생성 2. 파일 경로 선택 : "))
        if choice == 1 :
            pass
        elif choice == 2 :
            address = input("파일 경로를 선택하세요. : ")
            os.chdir("%s" %address)
        stu_json = []
        start(stu_json)

read_content()