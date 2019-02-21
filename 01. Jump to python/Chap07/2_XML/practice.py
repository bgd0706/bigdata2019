if menu_input == 4 :
    dic_col = {}
    index = 1
    ID_to_update = input("수정할 학생의 ID를 입력하세요 : ")
    for stu in range(total_stu) :
        if stu_list[stu].get("ID") == ID_to_update : break
    dic_col[1]=stu_list[stu].get("name")
    dic_col[2]=stu_list[stu].get("sex")
    dic_col[3]=stu_list[stu].findtext("age")
    dic_col[4]=stu_list[stu].findtext("major")
    print("1. 이름: %s" %(stu_list[stu].get("name")))
    print("2. 성별: %s" %(stu_list[stu].get("sex")))
    print("3. 나이: %s" %(stu_list[stu].findtext("age")))
    print("4. 전공: %s" %(stu_list[stu].findtext("major")))
    if not stu_list[stu].find("practicable_computer_languages") :
        print("5. 사용 가능한 컴퓨터 언어 없음")
    else :
        index = 5
        for languages in stu_list[stu].getiterator("practicable_computer_languages"):
            lang_list = languages.findall("language")
            for lang in range(len(lang_list)):
                actual_lang_name = lang_list[lang].get("name")
                actual_lang_level = lang_list[lang].get("level")
                for period in lang_list[lang].getiterator("period"):
                    actual_lang_period = period.get("value")
                print("%s. %s" %(index, actual_lang_name))
                dic_col[index]=actual_lang_name
                index+=1
                print("%s. 학습기간: %s" %(index, actual_lang_period))
                dic_col[index]=actual_lang_period
                index+=1
                print("%s. Level: %s" %(index, actual_lang_level))
                dic_col[index]=actual_lang_level
                index+=1
    key_to_update = int(input("수정할 항목의 번호를 입력하세요: "))
    value_to_update = input("수정할 값을 입력하세요: ")
    for i in list(dic_col.keys()) :
        if (i == key_to_update) :
            dic_col[i]= value_to_update
            break
