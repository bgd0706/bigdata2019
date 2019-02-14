try :
    result = 4/0
    print(result)
except : # 오류 종류에 상관없이 오류가 발생하기만 하면 except 블록을 수행
    print("비정상 정료")

print("Program End")