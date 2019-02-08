f = open('./file3.txt','r',encoding='UTF-8')

lines = f.readlines()
# print(lines) # 모든 라인을 list에 저장한다.
for line in lines :
    print(line)

f.close()