import re
original_text = """K1 adfadfadfadsfasdfadsfadsfadsf
b3 adfadfdfdfdfdadfadfadfasdfadfadf
3k adfadfefadfadfefadfefewefdfaefef
5j asdkfjadslfhehfjdfhjadhfeefefefe
k4 adfadfadfefefeadfdfefefdfddfedfe
9p dfadfadfef
u9 dfefadfefe
"""
p=re.compile('[a-zA-Z0-9][0-9]')
m=p.match(original_text)
print(m)