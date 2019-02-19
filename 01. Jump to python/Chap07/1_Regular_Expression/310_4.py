import re
p = re.compile("python", re.MULTILINE) # findall의 결과와 동일한 효과

data_str = """python one python debug
life is too short
python two
you need python
python three
I will study python
"""

print(p.findall(data_str))