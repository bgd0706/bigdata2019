import re
p = re.compile('[\d]')
print(p.search('7'))
p = re.compile('\d')
print(p.search('7'))
p = re.compile('[\w]')
print(p.search('7'))
p = re.compile('\w')
print(p.search('7'))
p = re.compile('[\s]')
print(p.search('7'))
p = re.compile('\s')
print(p.search('7'))