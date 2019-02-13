# result = system_cal()
# if result = -1
# 	print(" XXXX 에러를 발생했습니다.“)
# 	exit()
# else
# 	print(result)
# result = system_utill()
# if result = -1
# 	print(" XXXX 에러를 발생했습니다.“)
# 	exit()
# else
# 	print(result)
# print("Program End")
#  -> 위 코드는 번잡해서 밑 코드로 변형

try :
    result = 4/2
    print(result)
    f=open("나없는파일.txt","r")
    f.close()
except Exception as e : # 모든 Failure를 동일하게 처리하고 싶고, Exception의 유형을 정확히 모를 때 유용하다.
                        # (일반적인 상황에서 적용할 수 있는 Tip)
    print(e)

print("Program End")

