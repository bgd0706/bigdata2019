import re

p = re.compile('(blue|white|red)')
m = p.sub('colour', 'blue socks and red shoes')
print (m)

m = p.sub('colour', 'blue socks and red shoes', count=1)
print(m)

m = p.subn('colour', 'blue socks and red shoes') # 변경되는 것과 몇번 매치가 되었는지 튜플로 리턴
print(m)