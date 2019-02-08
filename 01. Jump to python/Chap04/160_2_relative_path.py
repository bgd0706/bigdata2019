# f = open("새파일.txt",'w') # 현재 소스코드 파일이 있는 경로에 파일 생성
                             # Unix 계열에서는 실행이 안될 수도 있다.
# f=open("./새파일.txt",'w') # 현재 경로에 파일 생성
                             # windows, unix 모든 운영체제에서 통용됨
# f= open("../새파일.txt", 'w') # 현재 경로의 상위 폴더
# f = open("../../../MyPath/new/새파일.txt","w")
 # 위 코드만 비교하면 f = open("d:/MyPath/new/새파일.txt")가 간결하다.
 # 하지만 d 드라이브가 없는 컴퓨터에 배포가 되어 돌아간다면 오류를 발생하게 된다.
 # 따라서 워크스페이스를 벗어난 .. 는 위험할 수 있다.

# f = open("../Path_exer/새파일.txt","w")
# f = open("../Path_exer/new1/새파일.txt","w")
# f = open("../Path_exer/renew1/새파일.txt","w")
 # 상대경로는 소스코드를 기준으로 예측가능한 경로를 활용해야 한다.
f = open("../path_exer/새파일.txt","w")
 # 생성이 되는 결과는 Windows 운영체제에서만 가능한 결과이다.
 # 따라서 호환성을 위하여 Windows에서도 대소문자를 가리는 것이 좋다.
f.close()