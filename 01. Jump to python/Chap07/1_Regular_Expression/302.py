import re
p=re.compile('ab?c') # ? == {0.1}
m=p.match('ac') # b가 0 이라
print(m)
m=p.match('abc') # b가 1 이라
print(m)
m=p.match('abbc') # b가 2 이라
print(m)
m=p.match('abbbc') # b가 3 이라
print(m)
m=p.match('abcd') # 정규식을 기준으로 a 1개, b 1개, c 1개가 있으므로 abc까지 만족
print(m)
