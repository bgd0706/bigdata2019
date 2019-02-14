import mod1
# print(mod1.sum(3,4))
# print(mod1.sum(3,"4")) # 두 인자의 형이 다르기 때문에 에러를 발생시킨다.
print(mod1.safe_sum(3,"4"))
print(mod1.safe_sum(4,5))
