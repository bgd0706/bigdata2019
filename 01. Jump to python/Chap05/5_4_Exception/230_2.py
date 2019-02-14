try :
    result = 4/0
    print(result)
except ZeroDivisionError : # 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행:
    print("비정상 정료")

print("Program End")