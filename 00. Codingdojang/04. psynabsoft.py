name = input("이름을 입력하세요. ").split(',')

print(len(list(map(lambda x : x[0]=='김', name))))
print(len(list(filter(lambda x : x[0]=='김', name))))
print(len(list(filter(lambda x : x[0]=='이', name))))

print(name.count("이재영"))

set = list(set(name))
print(set)
set.sort()
print(set)