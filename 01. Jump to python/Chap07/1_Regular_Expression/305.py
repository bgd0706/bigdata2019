import re
p=re.compile('[a-z]+')
m=p.search('3 python')
# m=p.match('python')
print(m)

if m:
    print('Match found:', m.group()) # 문자열 문자열 사이 공백
else :
    print('No match')