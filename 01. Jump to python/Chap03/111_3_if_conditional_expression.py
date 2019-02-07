# coding: cp949

# 현금과 카드가 모두 없는 경우
#is_cash = 0
#is_card = 0

# 현금만 소유한 경우
#is_cash = 1
#is_card = 0

# 카드만 소유한 경우
#is_cash = 0
#is_card = 1

# 현금과 카드를 모두 소유한 경우
is_cash = 1
is_card = 1

if is_cash+is_card: # 조건식을 사용한 경우
    print("택시를 타고 가라")
else:
    print("걸어 가라.")

