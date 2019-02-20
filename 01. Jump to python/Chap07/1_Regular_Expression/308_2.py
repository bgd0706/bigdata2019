import re
original_text = """adsfasdfdsfd
 adsfasdfasdf"""
p=re.compile('[a-z]*. [a-z]*', re.DOTALL)
m=p.match(original_text)
print(m)