import re

s = '<html><head><title>Title<\\title>'
print(len(s))

print(re.match('<.*>', s).span())

print(re.match('<.*>', s).group())

print(re.match('<.*?>', s).group())