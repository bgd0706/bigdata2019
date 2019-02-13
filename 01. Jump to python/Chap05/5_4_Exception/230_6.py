input_denominator = int(input("분모를 입력하세요 "))
try :
    result = 4/input_denominator
    print(result)
    f=open("나없는 파일.txt","r")
    f.close()
except ZeroDivisionError as e :
    print(e)
    print("분모가 0이 되어서는 안됩니다. 다시 입력하세요.")
except FileNotFoundError as e :
    print(e)
    print("해당 파일이 존재하지 않습니다. 230_6.py가 있는 경로에 나없는파일.txt 이 있는지 확인하세요.")

print("Program End")
