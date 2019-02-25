from xml.etree.ElementTree import parse

m_count = 0;w_count = 0;major_count = 0
twenty = 0;thirty = 0;fourty = 0
experience_count = 0
superior_count = 0;python_count = 0

tree = parse("students_info.xml")

root = tree.getroot()
child = root.getiterator()

stu_list = root.findall("student")
total_stu = len(stu_list)

print("학생 정보 (students_info.xml)을 읽어와서 아래 화면출력데로 학생정보를 분석하는 프로그램을 작성하시오.")
menu_input = int(input("학생정보 XML 데이터 분석 시작\n 1. 요약 정보 \n 2. 전체 데이터 조회\n 3. 종류\n 메뉴 입력 : "))

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
    print("<전체 학생 데이터>")
    for stu in range(total_stu) :
        print("* %s" %stu_list[stu].get("name"))
        print(" - %s" %stu_list[stu].get("sex"))
        print(" - %s" %stu_list[stu].findtext("age"))
        print(" - %s" %stu_list[stu].findtext("major"))
        if not stu_list[stu].find("practicable_computer_languages") :
            print(" - 사용 가능한 컴퓨터 언어 : 없음")
        else :
            print(" - 사용 가능한 컴퓨터 언어")
            for languages in stu_list[stu].getiterator("practicable_computer_languages") :
                lang_list = languages.findall("language")
                for lang in range(len(lang_list)) :
                    actual_lang_name = lang_list[lang].get("name")
                    actual_lang_level = lang_list[lang].get("level")
                    for period in lang_list[lang].getiterator("period") :
                        actual_lang_period = period.get("value")
                    print("  > %s (학습기간: %s, Level: %s)" %(actual_lang_name, actual_lang_period, actual_lang_level))
elif menu_input == 3 :
    exit()

