f=open("./file2.txt", 'a')
# f.write("Hello Daegu!!!!!!!!!!!!!!!!!!!!!!!!") # 이전 파일의 마지막 위치에서 값을 쓴다.
 # 따라서 줄 단위로 입력을 하고 싶으면 메세지의 마지막에 \n을 명시적으로 붙인다.
# f.write("\nHello Pusan!!!!!!!!!!!!!!!!!!!!!!!!") # 이전 파일의 마지막 위치에서 값을 쓴다.
my_message="""Hello Seoul!!
Hello Jeju!!
Hello Incheon!!
"""
f.write(my_message)
f.close()