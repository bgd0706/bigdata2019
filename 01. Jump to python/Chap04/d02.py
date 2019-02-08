def input_ingredient() :
    while True :
        user = input("안녕하세요. 원하시는 재료를 입력하세요: ")
        if user == "종료" :
            break
        ingredient_list.append(user)
    return ingredient_list

def make_sandwiches(ingredient_list) :
    print("샌드위치를 만들겠습니다.")
    for i in ingredient_list :
        print(i+" 추가합니다.")
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")

num= input("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다. \n 1. 주문 \n 2. 종료 \n 입력:")

if num == "1. 주문":
    ingredient_list = []
    input_ingredient()
    make_sandwiches(ingredient_list)
else :
    exit()