#coding: cp949

feel = "호감"
#feel = ""
hit_on_count = 0

while feel:
    hit_on_count = hit_on_count + 1
    print("%d번 데이트 신청합니다." %hit_on_count)

    if (hit_on_count == 10) :
        print("고백할 때가 다가 왔네요. ")
        break

    feel = input("현재 그녀에 대한 당신의 감정은 어떤가요?")
    if(feel == "비호감"):
        print("그럼 단념하세요")
        break
