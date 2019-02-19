import re

p=re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m=p.search("park 010-1234-1234")
print(m)
print(m.group(1))