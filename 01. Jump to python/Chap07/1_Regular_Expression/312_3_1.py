import re

# str = "\" -> '\' 다음에 escape 코드가 와야 하지만 없으므로 문법적으로 오류를 발생한다.
str = "\\" # str은 내부적으로 '\\' 저장이 된다. 하지만 문자로써는 '\'의 의미이다.
print(str) # 출력 결과는 '\'
str = "\\\\" # str은 내부적으로 '\\\\' 저장이 된다. 하지만 문자로써는 '\\'의 의미이다.
print(str) # 출력 결과는 '\\'
str = r'\\' # str은 내부적으로 '\\\\' 저장이 된다. 하지만 문자로써는 '\\'의 의미이다.
print(str)
# str = r'\' -> 현재 버전에서는 'r' raw string옵션을 사용하고 "\"를 한 개 사용하는 것을 허용하지 않는다.

print("\section test")

str = "\section"
if str == '\\section' :
    print(str)
if str == '\section' :
    print(str)