from konlpy.tag import Okt
okt = Okt() # 품사나 공백문자 기준으로 쪼개준다.
malist = okt.pos("아버지 가방에 들어가신다.", norm=True, stem=True)
print(malist)
malist = okt.pos("아버지가 방에 들어가신다.", norm=True, stem=True)
print(malist)