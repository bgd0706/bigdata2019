import re
p=re.compile('[\d]') # [0-9]
m=p.match('1')
print(m)

p=re.compile('[\D]') # [^0-9]
m=p.match('1')
print(m)

p=re.compile('[\s]') # [ ] or re.compile(' ')
m=p.match(' 1')
print(m)
m=p.match('     1') # \t
print(m)
m=p.match('''
1''') # \n
print(m)