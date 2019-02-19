import re
original_text = """1a adfadfadfadsfasdfadsfadsfadsf
b3 adfadfdfdfdfdadfadfadfasdfadfadf
3k adfadfefadfadfefadfefewefdfaefef
5j asdkfjadslfhehfjdfhjadhfeefefefe
k4 adfadfadfefefeadfdfefefdfddfedfe
9p dfadfadfef
u9 dfefadfefe
"""
p=re.compile('1a [a-z]+.b3')
# p=re.compile('.+[a-z][0-9]', re.DOTALL)
m=p.match(original_text)
print(m)