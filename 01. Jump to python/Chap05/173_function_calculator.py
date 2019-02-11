result1 = 0
result2 = 0
result3 = 0
result4 = 0

def adder1(num) :
    global result1 # 읽을 때는 필요없지만 값을 변경할 때는 해줘야 한다!
    print("%d값을 입력받았습니다." %num)
    result1 += num
    return result1

def adder2(num) :
    global result2
    print("%d값을 입력받았습니다." % num)
    result2 += num
    return result2

def adder3(num) :
    global result3
    print("%d값을 입력받았습니다." % num)
    result3 += num
    return result3

print(adder1(3))
print(adder1(4))
print(adder2(3))
print(adder2(7))
print(adder3(2))
print(adder1(6))
