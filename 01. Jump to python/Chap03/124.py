#coding: cp949
menu_prompt = """
1. 입력
2. 조회
3. 수정
4. 삭제
5. 종료

메뉴를 선택하세요 (1~5): """

customer_choice = 0
while customer_choice != 5 :
#    print(menu_prompt)
    customer_choice = int(input(menu_prompt))
