from xml.etree.ElementTree import parse

count_all= 0
m_count = 0
w_count = 0
major_count = 0
twenty = 0
thirty = 0
fourty = 0
programming_experience = 0
superior_count = 0
python_count = 0
twenty_info = []
thirty_info = []
fourty_info = []
all_student_info = []

tree = parse("students_info.xml")
root = tree.getroot() # root가 student_list

childs = root.getiterator() # student1, student2, student3 ....

for child in childs :
    if child.tag == 'student' :
        count_all = count_all + 1
        actual_sex = child.get("sex")
        if actual_sex == '남' :
            m_count = m_count+1
        else :
            w_count = w_count+1
        actual_name = child.get("name")
        for child_2 in child :
            if child_2.tag == 'major' :
                actual_major = child_2.text
                if actual_major == "컴퓨터 공학" or actual_major == "통계빅데이터" :
                    major_count = major_count + 1
            elif child_2.tag == 'age' :
                actual_age = int(child_2.text)
                if actual_age>= 20 and actual_age < 30:
                    twenty = twenty + 1
                    twenty_info.append([actual_name, int(child_2.text)])
                elif actual_age >= 30 and  actual_age < 40:
                    thirty = thirty + 1
                    thirty_info.append([actual_name, int(child_2.text)])
                elif actual_age >= 40 and actual_age < 50:
                    fourty = fourty + 1
                    fourty_info.append([actual_name, actual_age])
            elif child_2.tag == 'practicable_computer_languages' :
                enable_programming_languages = []
                for child_3 in child_2:
                    programming_experience = programming_experience + 1
                    break
                for child_3 in child_2:
                    actual_programming_level = child_3.get("level")
                    actual_programming_name = child_3.get("name")
                    if actual_programming_level == '상' :
                        superior_count = superior_count + 1
                    elif actual_programming_name == 'python' :
                        python_count = python_count + 1
                    for child_4 in child_3 :
                        actual_programming_period = child_4.text
                    enable_programming_languages.append([actual_programming_name, actual_programming_period, actual_programming_name])
                all_student_info.append([actual_name, actual_sex, actual_age, actual_major, enable_programming_languages])


print("학생 정보 (students_info.xml)을 읽어와서 아래 화면출력데로 학생정보를 분석하는 프로그램을 작성하시오.")

menu_input = int(input("학생정보 XML 데이터 분석 시작\n 1. 요약 정보 \n 2. 전체 데이터 조회\n 3. 종류\n 메뉴 입력 : "))

if (menu_input == 1) :
    print("<요약 정보>")
    print("* 전체 학생수 : %s" %count_all)
    print("* 성별")
    print(" - 남학생: %s명 (%s%%)" %(m_count, (m_count/count_all)*100))
    print(" - 여학생: %s명 (%s%%)" %(w_count, (w_count/count_all)*100))
    print("* 전공여부")
    print(" - 전공자(컴퓨터 공학, 통계): %s명 (%s%%)" %(major_count, (major_count/count_all)*100))
    print(" - 프로그래밍 언어 경험자: %s명 (%s%%)" %(programming_experience, (programming_experience/count_all)*100))
    print(" - 프로그래밍 언어 상급자: %s명 (%s%%)" %(superior_count, (superior_count/count_all)*100))
    print(" - 파이썬 경험자: %s명" %python_count)
    print("* 연령대")
    print(" - 20대 : %s명" % twenty, end=' ')
    print('[', end='')
    for i in twenty_info:
        print("%s : %s" % (i[0], i[1]), end=' ')
    print(']')
    print(" - 30대 : %s명" % thirty, end=' ')
    print('[', end='')
    for i in thirty_info:
        print("%s : %s" % (i[0], i[1]), end=' ')
    print(']')
    print(" - 40대 : %s명" % fourty, end=' ')
    print('[', end='')
    for i in fourty_info:
        print("%s : %s" % (i[0], i[1]), end=' ')
    print(']')
elif menu_input == 2:
    print("전체 학생 데이터")
    for i in range(count_all) :
        print("* %s" %(all_student_info[i][0]))
        print(" - 성별: %s" %(all_student_info[i][1]))
        print(" - 나이: %s" %(all_student_info[i][2]))
        print(" - 전공: %s" %(all_student_info[i][3]))
        if all_student_info[i][4] == [] :
            print("사용 가능한 컴퓨터 언어: 없음")
        else :
            for j in range(enable_programming_languages.__len__()) :
                print("> %s (학습기간: %s, Level: %s)" %(all_student_info[i][4][enable_programming_languages[j][0]],
                                                        all_student_info[i][4][enable_programming_languages[j][1]],
                                                        all_student_info[i][4][enable_programming_languages[j][2]]))
else:
    print("학생 정보 분석 완료")
    exit()

