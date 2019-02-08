def search_visitor(name) :
    f = open('방명록.txt', 'r', encoding='UTF-8')
    lines = f.readlines()
    for i in lines :
        info = i.split(" ")
        if (name == info[0]) :
            return name
    return ''

while True :
    name = input("이름을 입력하세요: ")
    find = search_visitor(name)

    if name == find:
        print('"'+find+"님 다시 방문해 주셔서 감사합니다. 즐거운 시간되세요.")
    else :
        birthday = input("생년월일을 입력하세요(예:801212): ")
        print(name+"님 환영합니다. 아래 내용을 입력하셨습니다.\n"+name+' '+birthday)

        f = open("방명록.txt", 'a', encoding='UTF-8')
        f.write('\n'+name)
        f.write(' '+birthday)
        f.close()