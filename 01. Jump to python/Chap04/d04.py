def search_visitor(name) :
    f = open('방명록.txt', 'r', encoding='UTF-8')
    lines = f.read().splitlines() # 한줄씩 읽는다. (이름+생년월일)
    for i in lines :
        info = i.split(" ") # 이름과 생년월일을 info리스트에 분할하여 넣는다.
        if (name == info[0]) : #이름은 info[0]에 저장되어 있으므로
            return name
    return ''

while True :
    name = input("이름을 입력하세요: ")
    find = search_visitor(name)

    if name == '종료' :
        break

    if name == find:
        print('"'+find+"님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요.")
    else :
        birthday = input("생년월일을 입력하세요(예:801212): ")
        print(name+"님 환영합니다. 아래 내용을 입력하셨습니다.\n"+name+' '+birthday)

        f = open("방명록.txt", 'a', encoding='UTF-8')
        f.write('\n'+name)
        f.write(' '+birthday)
        f.close()