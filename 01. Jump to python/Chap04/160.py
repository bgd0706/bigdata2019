# f = open("새파일.txt",'w') # 현재 소스코드 파일이 있는 경로에 파일 생성
                             # Unix 계열에서는 실행이 안될 수도 있다.
# f = open("d:\새파일.txt",'w') # 절대경로(absolute path)에 파일 생성
# f = open("d:/새파일.txt",'w')
# f = open("D:\MyPath\새파일.txt",'w')
# f = open("D:/MyPath/새파일.txt",'w')
# f = open("D:\MyPath\new\새파일.txt",'w') # \n은 특수문자 이기 때문에 에러가 발생한다.
# f = open("D:\MyPath\\new\새파일.txt",'w') # \\ -> \로 인식
# f = open("D:\\MyPath\\new\\새파일.txt",'w')
 # 실수를 줄이기 위해서 경로를 표시할 대는 모든 \를 \\로 표시한다.
f = open("D:/MyPath/new/새파일.txt",'w') # /를 한번만 사용해도 됨
 # 하위 버전과 연동이 되는지는 확인해야됨
f.close()