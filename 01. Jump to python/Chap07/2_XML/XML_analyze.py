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

tree = parse("students_info.xml")
root = tree.getroot() # root가 student_list

childs = root.getiterator() # student1, student2, student3 ....

for child in childs :
    if child.tag == 'student' :
        count_all = count_all + 1
        if child.get("sex") == '남' :
            m_count = m_count+1
        else :
            w_count = w_count+1
        actual_name = child.get("name")
    elif child.tag == "major" :
        if child.text == "컴퓨터 공학" or child.text == "통계빅데이터":
            major_count = major_count + 1
    elif child.tag == "age" :
        if int(child.text) >= 20 and int(child.text) < 30:
            twenty = twenty + 1
            twenty_info.append([actual_name, int(child.text)])
        elif int(child.text) >= 30 and int(child.text) < 40:
            thirty = thirty + 1
            thirty_info.append([actual_name, int(child.text)])
        elif int(child.text) >= 40 and int(child.text) < 50:
            fourty = fourty + 1
            fourty_info.append([actual_name, int(child.text)])
    elif child.tag == 'practicable_computer_languages' :
        for child2 in child :
            programming_experience = programming_experience + 1
            break
    elif child.tag == 'language' :
        if child.get("level") == '상' :
            superior_count = superior_count + 1
        elif child.get("name") == 'python' :
            python_count = python_count + 1


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
    print(" - 파이썬 경험자: %s명 (%s%%)" %(python_count, (python_count/count_all)*100))
    print("* 연령대")
    print(" - 20대 : %s명" %twenty, end=' ')
    print('[', end='')
    for i in twenty_info :
        print("%s : %s" %(i[0], i[1]), end=' ')
    print(']')
    print(" - 30대 : %s명" %thirty, end=' ')
    print('[', end='')
    for i in thirty_info:
        print("%s : %s" % (i[0], i[1]), end=' ')
    print(']')
    print(" - 40대 : %s명" %fourty, end=' ')
    print('[', end='')
    for i in fourty_info:
        print("%s : %s" % (i[0], i[1]), end=' ')
    print(']')
elif menu_input == 2 :
    print("전체 학생 데이터")
else :
    print("학생 정보 분석 완료")
    exit()

