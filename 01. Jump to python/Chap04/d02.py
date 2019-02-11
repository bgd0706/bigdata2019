def input_ingredient() :
    while True :
        user = input("안녕하세요. 원하시는 재료를 입력하세요: ")
        if user == "종료" :
            break
        ingredient_list.append(user) # 종료가 입력 될 때까지 ingredient_list에 추가저장
    return ingredient_list # 종료가 입력 되면 리턴한다.

def make_sandwiches(ingredient_list) :
    print("샌드위치를 만들겠습니다.")
    for i in ingredient_list :
        print(i+" 추가합니다.")
    print("여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.")

# 입력받는 변수
num= input("안녕하세요. 저희 가게에 방문해 주셔서 감사합니다. \n 1. 주문 \n 2. 종료 \n 입력:")

# '1. 주문'으로 받았을 경우
if num == "1. 주문":
    ingredient_list = [] # ingredient_list란 리스트를 생성. 초기값으로 빈 리스트로 설정
    input_ingredient() # 함수 실행
    make_sandwiches(ingredient_list)
# '2. 종료'로 받았을 경우
else :
    exit()