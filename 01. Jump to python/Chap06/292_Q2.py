while True :
    num = input("수를 입력하세요. : ")

    if  len(num)!= 10 or len(num) > len(set(num)) :
        print ("false")
    else :
        print("true")
    if num == "종료" :
        exit()