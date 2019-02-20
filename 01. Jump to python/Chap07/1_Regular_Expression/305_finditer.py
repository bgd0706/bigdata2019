import re
original_text = 'life is too short'
p=re.compile('[a-z]+')

result = p.finditer(original_text)
# 매칭된 결과를 'Match object' 리스트로 반환한다.
for r in result :
    print(r)