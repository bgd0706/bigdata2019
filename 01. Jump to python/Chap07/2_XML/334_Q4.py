import re

p = re.compile('.*[@].*(?=[.].*$)')
m = p.search("bgd0706@hanmail.net")
print (m.group())