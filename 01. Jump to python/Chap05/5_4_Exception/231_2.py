try :
    input_denominator = int(input("분모를 입력하세요: "))
    print("Progress 1")
    f = open('foo.txt','r')
    print("Progress 2")
    result = 4/input_denominator
    print("Progress 3")
    f.close()
    print("Progress 4")
except Exception as e :
    print(e)

