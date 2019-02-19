import re
original_text = "a"
p=re.compile('[a-c]')
m=p.match(original_text)
print(m)