from xml.etree.ElementTree import Element, SubElement, parse, ElementTree

def digit(x): # x를 기준으로 3만큼 오른쪽 정렬하고, 빈 곳은 0으로 치환
   return "{0:0>3}".format(x)

tree = parse("students_info.xml")

root = tree.getroot()
child = root.getiterator()

print("<화면 출력>\n학생정보 XML 데이터 분석 시작")
while True :
    m_count = 0;w_count = 0;major_count = 0
    twenty_info = [];thirty_info = [];fourty_info = []
    experience_count = 0;superior_count = 0;python_count = 0

    stu_list = root.findall("student")
    lang_list = []
    total_stu = len(stu_list) # 현재 파일에 있는 student 리스트 개수

    menu_input = int(input("[메인 메뉴]\n 1. 요약 정보 \n 2. 입력\n 3. 조회\n 4. 수정\n 5. 삭제\n 6. 종료 \n: "))

    if (menu_input == 1) :
        for stu in range(total_stu) :
            actual_name = stu_list[stu].get("name")
            if stu_list[stu].get("sex") == "남" :
                m_count += 1
            else :
                w_count += 1
            actual_age = int(stu_list[stu].findtext("age"))
            if actual_age >= 20 and actual_age < 30 :
                twenty_info.append(actual_name+ ':'+str(actual_age))
            elif actual_age >= 30 and actual_age < 40 :
                thirty_info.append(actual_name+':'+ str(actual_age))
            elif actual_age >= 40 and actual_age < 50 :
                fourty_info.append(actual_name+':'+str(actual_age))
            actual_major = stu_list[stu].findtext("major")
            if actual_major == "컴퓨터 공학" or actual_major == "통계빅데이터" :
                major_count += 1
            if stu_list[stu].find("practicable_computer_languages") :
                experience_count += 1
                for languages in stu_list[stu].getiterator("practicable_computer_languages") :
                    lang_list = languages.findall("language")
                    for lang in range(len(lang_list)) :
                        if lang_list[lang].get("name") == "Python":
                            python_count += 1
                        if lang_list[lang].get("level") == "상":
                            superior_count += 1

        print("<요약 정보>")
        print("* 전체 학생수 : %s" % total_stu)
        print("* 성별")
        print(" - 남학생: %s명 (%0.1f%%)" % (m_count, (m_count / total_stu) * 100))
        print(" - 여학생: %s명 (%0.1f%%)" % (w_count, (w_count / total_stu) * 100))
        print("* 전공여부")
        print(" - 전공자(컴퓨터 공학, 통계): %s명 (%0.1f%%)" % (major_count, (major_count / total_stu) * 100))
        print(" - 프로그래밍 언어 경험자: %s명 (%0.1f%%)" % (experience_count, (experience_count / total_stu) * 100))
        print(" - 프로그래밍 언어 상급자: %s명 (%0.1f%%)" % (superior_count, (superior_count / total_stu) * 100))
        print(" - 파이썬 경험자: %s명" % python_count)
        print("* 연령대")
        print(" - 20대 : %s명 (%0.1f%%) %s" % (len(twenty_info), len(twenty_info) / total_stu * 100, twenty_info))
        print(" - 30대 : %s명 (%0.1f%%) %s" % (len(thirty_info), len(thirty_info) / total_stu * 100, thirty_info))
        print(" - 40대 : %s명 (%0.1f%%) %s" % (len(fourty_info), len(fourty_info) / total_stu * 100, fourty_info))

    elif menu_input == 2 : # 입력
        while True :
            print("<신규 학생 정보 입력>")
            add_name = input("- 이름을 입력하세요 (종료는 'Enter' 입력): ")
            if add_name == '' :
                break
            add_sex = input("- 성별을 입력하세요: ")
            add_age = input("- 나이를 입력하세요: ")
            add_major = input("- 전공을 입력하세요: ")
            id_number = stu_list[total_stu-1].get("ID")[3:]
            student = Element("student", ID="ITT%s" %(digit(int(id_number)+1)), name=add_name, sex=add_sex)
            SubElement(student, "age").text = add_age
            SubElement(student, "major").text = add_major
            practicable = SubElement(student, "practicable_computer_languages")
            while True :
                print("사용 가능한 컴퓨터 언어를 입력하세요.")
                add_lang_name = input("  > 언어 이름(종료는 'Enter' 입력): ")
                if add_lang_name == '' :
                    break
                add_lang_period = input("  > 학습 기간(년/개월 단위): ")
                add_lang_level = input("  > 수준(상,중,하): ")
                language = Element("language", name=add_lang_name, level=add_lang_level)
                period = Element("period", value=add_lang_period)
                language.append(period)
                practicable.append(language)
            root.append(student)

            ElementTree(root).write("students_info.xml")

    elif menu_input == 3 : # 조회
        while True :
            read_menu_input = input("<조회 서브 메뉴>\n1. 개별 학생 조회\n1. CSV. 전체 학생 조회\n3. 상위 메뉴\n4. 종료\n메뉴 입력 : ")
            if read_menu_input == '1' :
                while True :
                    saved_number = []
                    search_con = input("<검색 조건>\n1. ID\n1. CSV. 이름\n3. 나이\n4. 전공\n5. 컴퓨터 언어 명\n6. 컴퓨터 언어 학습 기간"
                                       "\n7. 컴퓨터 언어 레벨\n8. 상위메뉴\n메뉴 입력: ")
                    if search_con == '8' :
                        break
                    else :
                        search_obj = input("검색어를 입력하세요: ")
                        if search_con == '1' :
                            for stu in range(total_stu) :
                                if search_obj in stu_list[stu].get("ID") :
                                    saved_number.append(stu)
                        elif search_con == '1. CSV':
                            for stu in range(total_stu) :
                                if search_obj in stu_list[stu].get("name") :
                                    saved_number.append(stu)
                        elif search_con == '3':
                            for stu in range(total_stu) :
                                if search_obj in stu_list[stu].findtext("age") :
                                    saved_number.append(stu)
                        elif search_con == '4':
                            for stu in range(total_stu) :
                                if search_obj in stu_list[stu].findtext("major") :
                                    saved_number.append(stu)
                        elif search_con == '5' :
                            for stu in range(total_stu) :
                                for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                                    lang_list = languages.findall("language")
                                    for lang in range(len(lang_list)):
                                        if search_obj in lang_list[lang].get("name") :
                                            saved_number.append(stu)
                        elif search_con == '6' :
                            for stu in range(total_stu) :
                                for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                                    lang_list = languages.findall("language")
                                    for lang in range(len(lang_list)):
                                        for period in lang_list[lang].getiterator("period"):
                                            if search_obj in period.get("value") :
                                                saved_number.append(stu)
                                        break
                                    break
                        elif search_con == '7' :
                            for stu in range(total_stu) :
                                for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                                    lang_list = languages.findall("language")
                                    for lang in range(len(lang_list)):
                                        if search_obj in lang_list[lang].get("level") :
                                            saved_number.append(stu)
                                    break
                                break
                    number_standard = set(saved_number)
                    if number_standard == 1 :
                        for index in range(len(number_standard)) :
                            stu = saved_number[index]
                            print("* %s (%s)" % (stu_list[stu].get("name"), stu_list[stu].get("ID")))
                            print(" - 성별: %s" % (stu_list[stu].get("sex")))
                            print(" - 나이: %s" % (stu_list[stu].findtext("age")))
                            print(" - 전공: %s" % (stu_list[stu].findtext("major")))
                            if not stu_list[stu].find("practicable_computer_languages"):
                                print(" - 사용 가능한 컴퓨터 언어 : 없음")
                            else:
                                print(" - 사용 가능한 컴퓨터 언어")
                                for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                                    lang_list = languages.findall("language")
                                    for lang in range(len(lang_list)):
                                        actual_lang_name = lang_list[lang].get("name")
                                        actual_lang_level = lang_list[lang].get("level")
                                        for period in lang_list[lang].getiterator("period"):
                                            actual_lang_period = period.get("value")
                                        print("  > %s (학습기간: %s, Level: %s)"
                                              % (actual_lang_name, actual_lang_period, actual_lang_level))
                    else :
                        for index in range(len(number_standard)) :
                            stu = saved_number[index]
                            print(" - %s (%s, %s, %s)" %(stu_list[stu].get("ID"), stu_list[stu].get("name"),
                                                         stu_list[stu].findtext("age"),
                                                        stu_list[stu].get("sex")))
            elif read_menu_input == '1. CSV' :
                print("<전체 학생 데이터>")
                for stu in range(total_stu):
                    print("* %s" % stu_list[stu].get("name"))
                    print(" - 성별: %s" % stu_list[stu].get("sex"))
                    print(" - 나이: %s" % stu_list[stu].findtext("age"))
                    print(" - 전공: %s" % stu_list[stu].findtext("major"))
                    if not stu_list[stu].find("practicable_computer_languages"):
                        print(" - 사용 가능한 컴퓨터 언어: 없음")
                    else:
                        print(" - 사용 가능한 컴퓨터 언어")
                        for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                            lang_list = languages.findall("language")
                            for lang in range(len(lang_list)):
                                actual_lang_name = lang_list[lang].get("name")
                                actual_lang_level = lang_list[lang].get("level")
                                for period in lang_list[lang].getiterator("period"):
                                    actual_lang_period = period.get("value")
                                print("  > %s (학습기간: %s, Level: %s)" % (
                                actual_lang_name, actual_lang_period, actual_lang_level))
            elif read_menu_input == '3' :
                break
            elif read_menu_input == '4' :
                exit()

    elif menu_input == 4 : # 수정
        ID_to_update = input("수정할 학생의 ID를 입력하세요 : ")
        # 수정하기 전 리스트 출력
        for stu in range(total_stu) :
            if stu_list[stu].get("ID") == ID_to_update : break
        print("1. 이름: %s" %(stu_list[stu].get("name")))
        print("1. CSV. 성별: %s" %(stu_list[stu].get("sex")))
        print("3. 나이: %s" %(stu_list[stu].findtext("age")))
        print("4. 전공: %s" %(stu_list[stu].findtext("major")))
        index = 5
        if not stu_list[stu].find("practicable_computer_languages") :
            print("5. 사용 가능한 컴퓨터 언어 없음")
        else :
            for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                lang_list = languages.findall("language")
                for lang in range(len(lang_list)):
                    actual_lang_name = lang_list[lang].get("name")
                    actual_lang_level = lang_list[lang].get("level")
                    for period in lang_list[lang].getiterator("period"):
                        actual_lang_period = period.get("value")
                    print("%s. %s" %(index, actual_lang_name))
                    print("%s. 학습기간: %s" %(index+1, actual_lang_period))
                    print("%s. Level: %s" %(index+2, actual_lang_level))
                    index += 3
        # 수정할 번호와 값을 입력
        key_to_update = int(input("\n수정할 항목의 번호를 입력하세요: "))
        if (key_to_update != 5) :
            value_to_update = input("수정할 값을 입력하세요: ")
        # 그 번호를 찾아 값을 수정하는 과정
        for stu in range(total_stu):
            if stu_list[stu].get("ID") == ID_to_update: break
        if (key_to_update == 1):
            stu_list[stu].attrib["name"] = value_to_update # 속성일 때, stu_list[stu].set("속성명", 변경할 값)
        if (key_to_update == 2):
            stu_list[stu].attrib["sex"] = value_to_update
        if (key_to_update == 3) :
            age_find = stu_list[stu].find("age")
            age_find.text = value_to_update
        if (key_to_update == 4) :
            age_major = stu_list[stu].find("major")
            age_major.text = value_to_update
        if (key_to_update == 5) : # 사용할 언어 추가
            name_to_update = input("추가할 언어이름을 입력하세요: ")
            level_to_update = input("추가할 언어수준을 입력하세요: ")
            period_to_update = input("추가할 언어기간을 입력하세요: ")
            language = Element("language")
            language.attrib["level"] = level_to_update
            language.attrib["name"] = name_to_update
            period = Element("period", value=period_to_update)
            language.append(period)
            stu_list[stu].find("practicable_computer_languages").append(language)
        if stu_list[stu].find("practicable_computer_languages") :
            index = 6
            for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                lang_list = languages.findall("language")
                for lang in range(len(lang_list)):
                    actual_lang_name = lang_list[lang].get("name")
                    actual_lang_level = lang_list[lang].get("level")
                    for period in lang_list[lang].getiterator("period"):
                        actual_lang_period = period.get("value")
                    if (key_to_update == index):
                        lang_list[lang].attrib["name"] = value_to_update
                    index += 1
                    if (key_to_update == index):
                        lang_list[lang].attrib["value"] = value_to_update
                    index += 1
                    if (key_to_update == index):
                        lang_list[lang].attrib["level"] = value_to_update
                    index += 1
        # 수정한 값으로 리스트 출력
        for stu in range(total_stu) :
            if stu_list[stu].get("ID") == ID_to_update : break
        print("* %s" % stu_list[stu].get("name"))
        print(" - 성별: %s" % stu_list[stu].get("sex"))
        print(" - 나이: %s" % stu_list[stu].findtext("age"))
        print(" - 전공: %s" % stu_list[stu].findtext("major"))
        if not stu_list[stu].find("practicable_computer_languages"):
            print(" - 사용 가능한 컴퓨터 언어: 없음")
        else:
            print(" - 사용 가능한 컴퓨터 언어")
            for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                lang_list = languages.findall("language")
                for lang in range(len(lang_list)):
                    actual_lang_name = lang_list[lang].get("name")
                    actual_lang_level = lang_list[lang].get("level")
                    for period in lang_list[lang].getiterator("period"):
                        actual_lang_period = period.get("value")
                    print("  > %s (학습기간: %s, Level: %s)"
                          % (actual_lang_name, actual_lang_period, actual_lang_level))
        ElementTree(root).write("students_info.xml")

    elif menu_input == 5 : # 삭제
        ID_to_remove = input("삭제할 ID를 입력하세요: ")

        for stu in range(total_stu) :
            if stu_list[stu].get("ID") == ID_to_remove: break
        root.remove(stu_list[stu])

        print("삭제 되었습니다.")
        ElementTree(root).write("students_info.xml")

    elif menu_input == 6 : # 종료
        break