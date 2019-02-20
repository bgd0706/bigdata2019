import re
p = re.compile("\w+\spython$", re.MULTILINE)

data_str = """python one python debug
life is too short
python two
you need python
python three
I will study python
"""

print(p.findall(data_str))