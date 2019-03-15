import pandas as pd
import MySQLdb
import csv,sqlite3,sys

filename = "./Student_Info_DB_Scheme.xlsx"
con = MySQLdb.connect(host='localhost', port=3306, db='my_students', user='root', passwd='1111', charset='utf8mb4')
c = con.cursor()

create_table = """CREATE TABLE IF NOT EXISTS Students
                    (Student_ID VARCHAR(20), Name VARCHAR(10), Sex VARCHAR(10), Age INT(10), Major VARCHAR(10), 
                    Practicable_computer_languages VARCHAR(30), 
                    High_level VARCHAR(20), Middle_level VARCHAR(20), Low_level VARCHAR(20));"""
c.execute(create_table)
con.commit()

def digit(x): # x를 기준으로 3만큼 오른쪽 정렬하고, 빈 곳은 0으로 치환
   return "{0:0>3}".format(x)

def summary () :
    c.execute("SELECT * FROM Students")
    total = c.fetchall()
    c.execute("SELECT * FROM Students WHERE Sex='남'")
    man = c.fetchall()
    c.execute("SELECT * FROM Students WHERE Sex='여'")
    woman = c.fetchall()
    c.execute("SELECT * FROM Students WHERE Major='컴퓨터 공학' OR Major='통계학'")
    programming_major = c.fetchall()
    c.execute("SELECT * FROM Students WHERE NOT Practicable_computer_languages=''")
    programming_exp = c.fetchall()
    c.execute("SELECT * FROM Students WHERE NOT High_level=''")
    high_count = c.fetchall()
    c.execute("SELECT * FROM Students WHERE Practicable_computer_languages='Python'")
    python_exp = c.fetchall()
    c.execute("SELECT Name, Age FROM Students WHERE Age>=20 AND Age<30")
    twenty = c.fetchall()
    two_info = []
    for two in twenty :
        for column_index in range(len(two)) :
            two_info.append(str(two[column_index]))
    c.execute("SELECT Name, Age FROM Students WHERE Age>=30 AND Age<40")
    thirty = c.fetchall()
    three_info = []
    for three in thirty :
        for column_index in range(len(three)) :
            three_info.append(str(three[column_index]))
    c.execute("SELECT Name, Age FROM Students WHERE Age>=40 AND Age<50")
    fourty = c.fetchall()
    fourty_info = []
    for four in fourty :
        for column_index in range(len(four)) :
            fourty_info.append(str(four[column_index]))

    print("<요약정보>")
    print("* 전체 학생수: %s명" %len(total))
    print("* 성별")
    print(" - 남학생: %s명 (%0.1f%%)" %(len(man), len(man)/len(total) * 100))
    print(" - 여학생: %s명 (%0.1f%%)" %(len(woman), len(woman)/len(total) * 100))
    print("* 전공여부")
    print(" - 전공자(컴퓨터 공학, 통계학): %s명 (%0.1f%%)" %(len(programming_major), len(programming_major)/len(total) * 100))
    print(" - 프로그래밍 언어 경험자: %s명 (%0.1f%%)" %(len(programming_exp), len(programming_exp)/len(total) * 100))
    print(" - 프로그래밍 언어 상급자: %s명 (%0.1f%%)" %(len(high_count), len(high_count)/len(total) * 100))
    print(" - 파이썬 경험자: %s명 (%0.1f%%)" %(len(python_exp), len(python_exp)/len(total) * 100))
    print("* 연령대")
    print(" - 20대: %s명 (%0.1f%%)" %(len(twenty), len(twenty)/len(total) * 100), end=' ')
    print("[", end=' ')
    for idx in range(0, len(two_info), 2):
        print("%s:%s " % (two_info[idx], two_info[idx+1]), end= '')
    print("]")
    print(" - 30대: %s명 (%0.1f%%)" %(len(thirty), len(thirty)/len(total) * 100), end= ' ')
    print("[", end=' ')
    for idx in range(0, len(three_info), 2):
        print("%s:%s " % (three_info[idx], three_info[idx+1]), end='')
    print("]")
    print(" - 40대: %s명 (%0.1f%%)" %(len(fourty), len(fourty)/len(total) * 100), end=' ')
    print("[", end=' ')
    for idx in range(0, len(fourty_info), 2):
        print("%s:%s " % (fourty_info[idx], fourty_info[idx+1]), end='')
    print("]")

def insert () :
    print("신규 학생 정보 입력>")
    while True :
        add_name = input(("- 이름을 입력하세요 (종료는 'Enter' 입력): "))
        if add_name == '' : break
        add_sex = input(("- 성별을 입력하세요: "))
        add_age = int(input(("- 나이를 입력하세요: ")))
        add_major = input(("- 전공을 입력하세요: "))
        list_pro_name = []
        list_pro_high_level = []
        list_pro_middle_level = []
        list_pro_low_level = []
        while True :
            print("- 사용 가능한 컴퓨터 언어를 입력하세요:")
            add_pro_name = input((" > 언어를 입력하세요 (종료는 'Enter' 입력): "))
            if add_pro_name == '' : break
            add_pro_level = input(" > 수준(상,중,하): ")
            list_pro_name.append(add_pro_name)
            if add_pro_level == "상" :
                list_pro_high_level.append(add_pro_name)
            elif add_pro_level == "중" :
                list_pro_middle_level.append(add_pro_name)
            elif add_pro_level == "하" :
                list_pro_low_level.append(add_pro_name)

        c.execute("SELECT Student_ID FROM Students")
        rows = c.fetchall()
        row_list_id = []
        for row in rows:
            row_list_id = []
            for column_index in range(len(row)):
                row_list_id.append(str(row[column_index]))
        len_id = len(row_list_id)
        int_number = 000
        if len_id != 0 :
            int_number = int(row_list_id[len_id-1][3:])
        c.execute("INSERT INTO Students VALUES ('ITT%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s');"
                  %( digit(int_number + 1), add_name, add_sex, add_age, add_major, (',').join(list_pro_name),
                     (',').join(list_pro_high_level), (',').join(list_pro_middle_level), (',').join(list_pro_low_level) ))
        con.commit()

def each_select () :
    each_input=int(input("""
< 검색 조건 >
1. ID
2. 이름
3. 나이
4. 전공
5. 컴퓨터 언어 명
6. 컴퓨터 언어 레벨
7. 상위 메뉴
메뉴 입력 : """))
    if each_input == 1 :
        search = input("검색어를 입력하세요: ")
        c.execute("SELECT * FROM Students WHERE Student_ID LIKE '%%%s%%'" %search)
    elif each_input == 2 :
        search = input("검색어를 입력하세요: ")
        c.execute("SELECT * FROM Students WHERE Name LIKE '%%%s%%'" % search)
    elif each_input == 3 :
        search = input("검색어를 입력하세요: ")
        c.execute("SELECT * FROM Students WHERE Age LIKE'%%%s%%'" % search)
    elif each_input == 4 :
        search = input("검색어를 입력하세요: ")
        c.execute("SELECT * FROM Students WHERE Major LIKE '%%%s%%'" % search)
    elif each_input == 5 :
        search = input("검색어를 입력하세요: ")
        c.execute("SELECT * FROM Students WHERE Practicable_computer_languages LIKE '%%%s%%'" % search)
    elif each_input == 6 :
        search = input("검색어를 입력하세요: ")
        if search == '상' :
            c.execute("SELECT * FROM Students WHERE High_level != 'nan'")
        elif search == '중' :
            c.execute("SELECT * FROM Students WHERE Middle_level != 'nan'")
        elif search == '하':
            c.execute("SELECT * FROM Students WHERE low_level != 'nan'")

    rows = c.fetchall()
    if len(rows) == 1 :
        for row in rows:
            row_list_output = []
            for column_index in range(len(row)) :
                row_list_output.append(str(row[column_index]))
            print("* %s (%s)" %(row_list_output[1], row_list_output[0]))
            print(" - 성별: %s" %row_list_output[2])
            print(" - 나이: %s" %row_list_output[3])
            print(" - 전공: %s" %row_list_output[4])
            if row_list_output[5] != '' :
                practicable = row_list_output[5].split(',')
                High = row_list_output[6].split(',')
                Middle = row_list_output[7].split(',')
                Low = row_list_output[8].split(',')
                print(" - 사용 가능한 컴퓨터 언어")
                for pra_idx in range (len(practicable)) :
                    for h in range(len(High)) :
                        if High[h] == practicable[pra_idx] :
                            print("   > %s (Level : 상)" %practicable[pra_idx])
                            break
                    for m in range(len(Middle)) :
                        if Middle[m] == practicable[pra_idx] :
                            print("   > %s (Level : 중)" % practicable[pra_idx])
                            break
                    for l in range(len(Low)) :
                        if Low[l] == practicable[pra_idx]:
                            print("   > %s (Level : 하)" % practicable[pra_idx])
                            break
    else :
        for row in rows:
            row_list_output = []
            for column_index in range(len(row)) :
                row_list_output.append(str(row[column_index]))
            print("- %s (%s, %s, %s)" %(row_list_output[0], row_list_output[1], row_list_output[2], row_list_output[3]))

def total_select () :
    c.execute("SELECT * FROM Students")
    rows = c.fetchall()
    for row in rows:
        row_list_output = []
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print("* %s (%s)" % (row_list_output[1], row_list_output[0]))
        print(" - 성별: %s" % row_list_output[2])
        print(" - 나이: %s" % row_list_output[3])
        print(" - 전공: %s" % row_list_output[4])
        if row_list_output[5] != '' :
            practicable = row_list_output[5].split(',')
            High = row_list_output[6].split(',')
            Middle = row_list_output[7].split(',')
            Low = row_list_output[8].split(',')
            print(" - 사용 가능한 컴퓨터 언어")
            for pra_idx in range(len(practicable)):
                for h in range(len(High)):
                    if High[h] == practicable[pra_idx]:
                        print("   > %s (Level : 상)" % practicable[pra_idx])
                        break
                for m in range(len(Middle)):
                    if Middle[m] == practicable[pra_idx]:
                        print("   > %s (Level : 중)" % practicable[pra_idx])
                        break
                for l in range(len(Low)):
                    if Low[l] == practicable[pra_idx]:
                        print("   > %s (Level : 하)" % practicable[pra_idx])
                        break

def update () :
    ID_to_update = input("수정할 학생의 ID를 입력하세요: ")
    c.execute("SELECT * FROM Students WHERE Student_ID = '%s'" %ID_to_update)
    rows = c.fetchall()
    row_list_output = []
    for row in rows:
        for column_index in range(len(row)):
            row_list_output.append(str(row[column_index]))
        print("1. 이름: %s" % row_list_output[1])
        print("2. 성별: %s" % row_list_output[2])
        print("3. 나이: %s" % row_list_output[3])
        print("4. 전공: %s" % row_list_output[4])
        if row_list_output[5] == '' :
            print("5. 사용 가능한 언어 없음")
        else :
            practicable = row_list_output[5].split(',')
            High = row_list_output[6].split(',')
            Middle = row_list_output[7].split(',')
            Low = row_list_output[8].split(',')
            lan_level = {}
            for pra_idx in range(len(practicable)) :
                for h in range(len(High)):
                    if High[h] == practicable[pra_idx]:
                        lan_level[practicable[pra_idx]] = '상'
                        break
                for m in range(len(Middle)):
                    if Middle[m] == practicable[pra_idx]:
                        lan_level[practicable[pra_idx]] = '중'
                        break
                for l in range(len(Low)):
                    if Low[l] == practicable[pra_idx]:
                        lan_level[practicable[pra_idx]] = '하'
                        break
            print("<사용 가능한 컴퓨터 언어>")
            look_index = 5
            for pra_idx in range(len(practicable)) :
                print("%s. %s" %(look_index, practicable[pra_idx]))
                look_index += 1
                print("%s. Level: %s" %(look_index, lan_level[practicable[pra_idx]]))
                look_index += 1
    index_to_update = int(input("수정할 항목의 번호를 입력하세요: "))
    if row_list_output[5] != "" :
        value_to_update = input("수정할 값을 입력하세요: ")
    if index_to_update == 1 :
        c.execute("UPDATE Students SET Name='%s' WHERE Student_ID='%s';" %(value_to_update, ID_to_update))
    elif index_to_update == 2 :
        c.execute("UPDATE Students SET Sex='%s' WHERE Student_ID='%s';" % (value_to_update, ID_to_update))
    elif index_to_update == 3 :
        c.execute("UPDATE Students SET Age='%s' WHERE Student_ID='%s';" % (value_to_update, ID_to_update))
    elif index_to_update == 4 :
        c.execute("UPDATE Students SET Major='%s' WHERE Student_ID='%s';" % (value_to_update, ID_to_update))
    else :
        if row_list_output[5] == '' :
            list_pro_name = []
            list_pro_high_level = []
            list_pro_middle_level = []
            list_pro_low_level = []
            while True:
                print("- 사용 가능한 컴퓨터 언어를 입력하세요:")
                add_pro_name = input((" > 언어를 입력하세요 (종료는 'Enter' 입력): "))
                if add_pro_name == '': break
                add_pro_level = input(" > 수준(상,중,하): ")
                list_pro_name.append(add_pro_name)
                if add_pro_level == "상":
                    list_pro_high_level.append(add_pro_name)
                elif add_pro_level == "중":
                    list_pro_middle_level.append(add_pro_name)
                elif add_pro_level == "하":
                    list_pro_low_level.append(add_pro_name)
            c.execute("UPDATE Students SET Practicable_computer_languages='%s', High_level='%s', Middle_level='%s',"
                      "Low_level='%s' WHERE Student_ID='%s'"
                      % ( (',').join(list_pro_name),(',').join(list_pro_high_level),(',').join(list_pro_middle_level),
                          (',').join(list_pro_low_level), ID_to_update))
        else :
            standard_index_lan = 5
            if index_to_update % 2 != 0 : # 컴퓨터 언어 이름
                for pra_idx_update in range(len(practicable)) :
                    if (index_to_update-standard_index_lan) == pra_idx_update*2  :
                        remove_value = practicable.pop(pra_idx_update)
                        practicable.append(value_to_update)
                        for h in range(len(High)):
                            if High[h] == remove_value:
                                High.pop(h)
                                High.append(value_to_update)
                                c.execute("UPDATE Students SET Practicable_computer_languages='%s', High_level='%s' WHERE Student_ID='%s'"
                                          % ( (',').join(practicable), (',').join(High), ID_to_update))
                                break
                        for m in range(len(Middle)):
                            if Middle[m] == remove_value:
                                Middle.pop(m)
                                Middle.append(value_to_update)
                                c.execute("UPDATE Students SET Practicable_computer_languages='%s', Middle_level='%s' WHERE Student_ID='%s'"
                                    % ((',').join(practicable), (',').join(Middle), ID_to_update))
                                break
                        for l in range(len(Low)):
                            if Low[l] == remove_value:
                                Low.pop(l)
                                Low.append(value_to_update)
                                c.execute("UPDATE Students SET Practicable_computer_languages='%s', Low_level='%s' WHERE Student_ID='%s'"
                                    % ((',').join(practicable), (',').join(Low), ID_to_update))
                                break
            else : # 컴퓨터 언어 수준
                for pra_idx_update in range(len(practicable)) :
                    if ((index_to_update-1)-standard_index_lan) == pra_idx_update*2  :
                        remove_value = lan_level[practicable[pra_idx_update]]
                        if remove_value == '상' :
                            for h in range(len(High)) :
                                if practicable[pra_idx_update] == High[h] :
                                    High.pop(h)
                                    c.execute("UPDATE Students SET High_level='%s' WHERE Student_ID='%s'"
                                              % ((',').join(High), ID_to_update))
                                    break
                        elif remove_value == '중' :
                            for m in range(len(Middle)) :
                                if practicable[pra_idx_update] == Middle[m] :
                                    Middle.pop(m)
                                    c.execute("UPDATE Students SET Middle_level='%s' WHERE Student_ID='%s'"
                                              % ((',').join(Middle), ID_to_update))
                                    break
                        elif remove_value == '하' :
                            for l in range(len(Low)) :
                                if practicable[pra_idx_update] == Low[l] :
                                    Low.pop(l)
                                    c.execute("UPDATE Students SET Low_level='%s' WHERE Student_ID='%s'"
                                              % ((',').join(Low), ID_to_update))
                                    break
                        if value_to_update == '상' :
                            if High[0] == '' :
                                High.pop(0)
                            High.append(practicable[pra_idx_update])
                            c.execute("UPDATE Students SET High_level='%s' WHERE Student_ID='%s'"
                                % ( (',').join(High), ID_to_update))
                        elif value_to_update == '중':
                            if Middle[0] == '' :
                                Middle.pop(0)
                            Middle.append(practicable[pra_idx_update])
                            c.execute("UPDATE Students SET Middle_level='%s' WHERE Student_ID='%s'"
                                      % ((',').join(Middle), ID_to_update))
                        elif value_to_update == '하' :
                            if Low[0] == '' :
                                Low.pop(0)
                            Low.append(practicable[pra_idx_update])
                            c.execute("UPDATE Students SET Low_level='%s' WHERE Student_ID='%s'"
                                % ( (',').join(Low), ID_to_update))
    con.commit()

def delete () :
    ID_to_delete = input("삭제할 ID를 입력하세요: ")
    c.execute("DELETE FROM Students WHERE Student_ID='%s'" %ID_to_delete)
    con.commit()

def main () :
    while True :
        print("<화면 출력>\n학생정보 DB 데이터 분석 시작..")
        menu_input = int(input(("[메인 메뉴]\n1. 요약정보\n2. 입력\n3. 조회\n4. 수정\n5. 삭제\n6. 종료\n메뉴 입력: ")))
        if menu_input == 1 : # 요약정보
            summary()
        elif menu_input == 2 : # 입력
            insert()
        elif menu_input == 3 : # 조회
            while True :
                select_input= int(input(("<조회 서브 메뉴>\n1. 개별 학생 조회\n2. 전체 학생 조회\n3. 상위메뉴\n메뉴 입력: ")))
                if select_input == 1 : # 개별 학셍 조회
                    each_select()
                elif select_input == 2 : # 전체 학생 조회
                    total_select()
                elif select_input == 3 : # 상위 메뉴
                    break
        elif menu_input == 4 : # 수정
            update()
        elif menu_input == 5 : # 삭제
            delete()
        elif menu_input == 6 : # 종료
            break

main()