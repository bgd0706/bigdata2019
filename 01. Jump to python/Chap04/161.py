f=open("./file3.txt", 'w', encoding="UTF-8")
 # Pycharm에서 한글 설정을 하려면 환경설정에서 file encoding을 EUC-KR로 변경
for i in range(1, 11) :
    data = '%d번째 줄입니다.\n' %i
    f.write(data)
f.close()