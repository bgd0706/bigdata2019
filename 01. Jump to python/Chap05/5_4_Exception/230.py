try :
    result = 4/2
    print(result)
except ZeroDivisionError as e: # 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행
                               # -> 이 오류 메세지를 출력하고 싶을 때
    print(e)

print("Program End")