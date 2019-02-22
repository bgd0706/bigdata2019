import json

while True :
    with open("ITT_Student.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        stu_json = json.loads(json_string)

    print("="*30)
    print("JSON 기반 학생 정보 관리 프로그램")
    print("="*30)
    print("1. 학생 정보입력\n2. 학생 정보조회\n3. 학생 정보수정\n4. 학생정보 삭제\n5. 프로그램 종료")
    print(" ")
    menu_input = int(input("메뉴를 선택하세요: "))
    if (menu_input == 1) : # 학생 정보입력
        print("="*10+"1. 학생 정보 입력 화면"+"="*10)

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
                print("="*30)
                print("* 학생 ID: %s" %stu_json[i]["student_ID"])
                print("* 이름 : %s" %stu_json[i]["student_name"])
                print("* 나이 : %s" %stu_json[i]["student_age"])
                print("* 주소 : %s" %stu_json[i]["address"])
                print("* 수강 정보 ")
                print(" + 과거 수강 횟수 : %s" %stu_json[i]["total_course_info"]["num_of_course_learned"])
                print(" + 현재 수강 과목 ")
                for j in range(len(stu_json[i]["total_course_info"]["learning_course_info"])) :
                    print("-" * 30)
                    print("  강의 코드 : %s" %stu_json[i]["total_course_info"]["learning_course_info"][j]["course_code"])
                    print("  강의명 : %s" %stu_json[i]["total_course_info"]["learning_course_info"][j]["course_name"])
                    print("  강사 : %s" %stu_json[i]["total_course_info"]["learning_course_info"][j]["teacher"])
                    print("  개강일 : %s" %stu_json[i]["total_course_info"]["learning_course_info"][j]["open_date"])
                    print("  종료일 : %s" %stu_json[i]["total_course_info"]["learning_course_info"][j]["close_date"])
        else :
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
                    if search_obj in stu_json[i]["student_age"] :
                        saved_number.append(i)
            elif read_menu_input == 5 : # 주소 검색
                for i in range(len(stu_json)) :
                    if search_obj in stu_json[i]["address"] :
                        saved_number.append(i)
            elif read_menu_input == 6 : # 과거 수강 횟수 검색
                for i in range(len(stu_json)) :
                    if search_obj in stu_json[i]["total_course_info"]["num_of_course_learned"] :
                        saved_number.append(i)
            elif read_menu_input == 7 : # 현재 강의를 수강중인 학생
                for i in range(len(stu_json)) :
                    for j in range(len(stu_json[i]["total_course_info"]["learning_course_info"])) :
                        if search_obj in stu_json[i]["total_course_info"]["learning_course"][j]["course_code"] :
                            saved_number.append(i)
            elif read_menu_input == 8 :  # 현재 강의를 수강중인 강의명
                for i in range(len(stu_json)):
                    for j in range(len(stu_json[i]["total_course_info"]["learning_course_info"])):
                        if search_obj in stu_json[i]["total_course_info"]["learning_course"][j]["course_name"]:
                            saved_number.append(i)
            elif read_menu_input == 9 :  # 현재 수강 강사
                for i in range(len(stu_json)):
                    for j in range(len(stu_json[i]["total_course_info"]["learning_course_info"])):
                        if search_obj in stu_json[i]["total_course_info"]["learning_course"][j]["teacher"]:
                            saved_number.append(i)
            elif read_menu_input == 10 : # 이전 메뉴
                break


