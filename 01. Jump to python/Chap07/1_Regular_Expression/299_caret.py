import re
p=re.compile('[^0-9]') # caret은 전체의 not이다.
m=p.match('1')
print(m)

p=re.compile("^0") # caret은 []문자열 클래스 안에만 not 의미를 가짐. []가 없으면 ^ 이것은 문자로 인식됨
m=p.match("1")
print(m)

p = re.compile('^')
m = p.match('^')
print(m)