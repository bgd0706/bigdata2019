m = int(input("총 건수를 입력하시오 : "))
n = int(input("한페이지에 보여줄 게시물 수를 입력하시오 : "))

list = list(divmod(m,n))
if (int(list[1]) == 0) :
    print(list[0])
else :
    print(list[0]+1)