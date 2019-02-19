import re
# original_text = "a\nb"
original_text = """a
b"""
# p=re.compile('a.b')     # 정규식 '.'는 원문에 \n에 대해서 기본 옵션으로 사용하면 패턴 매칭이 일어나지 않는다.
p=re.compile("a\nb")    # 참고) 정규식에 '\n'을 사용한 경우는 기본 옵션을 사용해도 패턴 매칭을 할 수 있다.
# p=re.compile('a.b', re.DOTALL)
# 원문의 줄바꿈 '\n'을 매칭 시킬 ','이 re.DOTALL 옵션사용시 필요하다.
m=p.match(original_text)
print(m)