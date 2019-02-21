from xml.etree.ElementTree import Element, SubElement, parse, dump, ElementTree

m_count = 0;w_count = 0;major_count = 0
twenty = 0;thirty = 0;fourty = 0
experience_count = 0
superior_count = 0;python_count = 0

def digit(x):
  if x < 10:
    return "00" + str(x)
  elif x < 100:
    return "0" + str(x)
  return str(x)

tree = parse("students_info.xml")

root = tree.getroot()
child = root.getiterator()

stu_list = root.findall("student")
lang_list = []
total_stu = len(stu_list)

menu_input = int(input("학생정보 XML 데이터 분석 시작\n 1. 요약 정보 \n 2. 입력\n 3. 조회\n 4. 수정\n 5. 삭제\n 6. 종료 \n: "))

if (menu_input == 1) :
    print("<요약 정보>")
    print("* 전체 학생수 : %s" %total_stu)
    for stu in range(total_stu) :
        if stu_list[stu].get("sex") == "남" :
            m_count += 1
        else :
            w_count += 1
        actual_age = int(stu_list[stu].findtext("age"))
        if actual_age >= 20 and actual_age < 30 :
            twenty += 1
        elif actual_age >= 30 and actual_age < 40 :
            thirty += 1
        elif actual_age >= 40 and actual_age < 50 :
            fourty += 1
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
    print(" - 남학생: %s명 (%s%%)" % (m_count, (m_count / total_stu) * 100))
    print(" - 여학생: %s명 (%s%%)" % (w_count, (w_count / total_stu) * 100))
    print("* 전공여부")
    print(" - 전공자(컴퓨터 공학, 통계): %s명 (%s%%)" % (major_count, (major_count / total_stu) * 100))
    print(" - 프로그래밍 언어 경험자: %s명 (%s%%)" % (experience_count, (experience_count / total_stu) * 100))
    print(" - 프로그래밍 언어 상급자: %s명 (%s%%)" % (superior_count, (superior_count / total_stu) * 100))
    print(" - 파이썬 경험자: %s명" % python_count)
    print("* 연령대")
    print(" - 20대 : %s명 (%s%%)" % (twenty, twenty / total_stu * 100))
    print(" - 30대 : %s명 (%s%%)" % (thirty, thirty / total_stu * 100))
    print(" - 40대 : %s명 (%s%%)" % (fourty, fourty / total_stu * 100))

elif menu_input == 2 :
    while True :
        print("<신규 학생 정보 입력>")
        add_name = input("- 이름을 입력하세요 (종료는 'Enter' 입력): ")
        if add_name == '' :
            break
        add_sex = input("- 성별을 입력하세요: ")
        add_age = input("- 나이를 입력하세요: ")
        add_major = input("- 전공을 입력하세요: ")
        student = Element("student", id="ITT%s" %(digit(total_stu+1)), name=add_name, sex=add_sex)
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
        saved_number = []
        read_menu_input = input("<조회 서브 메뉴>\n1. 개별 학생 조회\n2. 전체 학생 조회\n3. 상위 메뉴\n4. 종료\n메뉴 입력 : ")
        if read_menu_input == '1' :
            search_con = input("<검색 조건>\n1. ID\n2. 이름\n3. 나이\n4. 전공\n5. 컴퓨터 언어 명\n6. 컴퓨터 언어 학습 기간"
                               "\n7. 컴퓨터 언어 레벨\n8. 상위메뉴\n메뉴 입력: ")
            search_obj = input("검색어를 입력하세요: ")
            if search_con == '1' :
                for stu in range(total_stu) :
                    if search_obj == stu_list[stu].get("ID") :
                        saved_number.append(stu)
            elif search_con == '2':
                for stu in range(total_stu) :
                    if search_obj == stu_list[stu].get("name") :
                        saved_number.append(stu)
            elif search_con == '3':
                for stu in range(total_stu) :
                    if search_obj == stu_list[stu].findtext("age") :
                        saved_number.append(stu)
            elif search_con == '4':
                for stu in range(total_stu) :
                    if search_obj == stu_list[stu].findtext("major") :
                        saved_number.append(stu)
            elif search_con == '5' :
                for stu in range(total_stu) :
                    for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                        lang_list = languages.findall("language")
                        for lang in range(len(lang_list)):
                            if search_obj == lang_list[lang].get("name") :
                                saved_number.append(stu)
            elif search_con == '6' :
                for stu in range(total_stu) :
                    for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                        lang_list = languages.findall("language")
                        for lang in range(len(lang_list)):
                            for period in lang_list[lang].getiterator("period"):
                                if search_obj == period.get("value") :
                                    saved_number.append(stu)
                                    break
                            break
            elif search_con == '7' :
                for stu in range(total_stu) :
                    for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                        lang_list = languages.findall("language")
                        for lang in range(len(lang_list)):
                            if search_obj == lang_list[lang].get("level") :
                                saved_number.append(stu)
                                break
                        break
            for index in range(len(saved_number)) :
                stu = saved_number[index]
                print("* %s (%s)" % (stu_list[stu].get("name"), stu_list[stu].get("ID")))
                print(" - 성별: %s" % (stu_list[stu].get("sex")))
                print(" - 나이: %s" % (stu_list[stu].findtext("age")))
                print(" - 전공: %s" % (stu_list[stu].findtext("major")))
                if not stu_list[stu].find("practicable_computer_languages"):
                    print("- 사용 가능한 컴퓨터 언어 : 없음")
                else:
                    print("- 사용 가능한 컴퓨터 언어")
                    for languages in stu_list[stu].getiterator("practicable_computer_languages"):
                        lang_list = languages.findall("language")
                        for lang in range(len(lang_list)):
                            actual_lang_name = lang_list[lang].get("name")
                            actual_lang_level = lang_list[lang].get("level")
                            for period in lang_list[lang].getiterator("period"):
                                actual_lang_period = period.get("value")
                            print("  > %s (학습기간: %s, Level: %s)" % (actual_lang_name, actual_lang_period, actual_lang_level))

        elif read_menu_input == '2' :
            print("<전체 학생 데이터>")
            for stu in range(total_stu):
                print("* %s" % stu_list[stu].get("name"))
                print(" - %s" % stu_list[stu].get("sex"))
                print(" - %s" % stu_list[stu].findtext("age"))
                print(" - %s" % stu_list[stu].findtext("major"))
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
                            print("  > %s (학습기간: %s, Level: %s)" % (
                            actual_lang_name, actual_lang_period, actual_lang_level))

elif menu_input == 4 :
    dic_col = {}
    index = 1
    ID_to_update = input("수정할 학생의 ID를 입력하세요 : ")
    key_to_update = int(input("수정할 항목의 번호를 입력하세요: "))
    value_to_update = input("수정할 값을 입력하세요: ")

    for stu in range(total_stu) :
        if stu_list[stu].get("ID") == ID_to_update : break
    print("%s. 이름: %s" %(index, stu_list[stu].get("name")))
    if (key_to_update == index) :
        stu_list[stu].attrib["name"] = value_to_update
    index+=1
    print("%s. 성별: %s" %(index, stu_list[stu].get("sex")))
    if (key_to_update == index) :
        stu_list[stu].attrib["sex"] = value_to_update
    index+=1
    print("%s. 나이: %s" %(index, stu_list[stu].findtext("age")))
    # if (key_to_update == index) :
        # stu_list[stu].text["age"] = value_to_update
    index+=1
    print("%s. 전공: %s" %(index, stu_list[stu].findtext("major")))
    # if (key_to_update == index) :
    #     stu_list[stu].text["major"] = value_to_update
    index+=1
    if not stu_list[stu].find("practicable_computer_languages") :
        print("%s. 사용 가능한 컴퓨터 언어 없음")
    else :
        for languages in stu_list[stu].getiterator("practicable_computer_languages"):
            lang_list = languages.findall("language")
            for lang in range(len(lang_list)):
                actual_lang_name = lang_list[lang].get("name")
                actual_lang_level = lang_list[lang].get("level")
                for period in lang_list[lang].getiterator("period"):
                    actual_lang_period = period.get("value")
                print("%s. %s" %(index, actual_lang_name))
                if (key_to_update == index):
                    lang_list[lang].attrib["name"] = value_to_update
                index+=1
                print("%s. 학습기간: %s" %(index, actual_lang_period))
                if (key_to_update == index):
                    lang_list[lang].attrib["value"] = value_to_update
                index+=1
                print("%s. Level: %s" %(index, actual_lang_level))
                if (key_to_update == index):
                    lang_list[lang].attrib["level"] = value_to_update
                index+=1