import re

p = re.compile('a[.]{3,}b')
m = p.match("a....b")
print(m)