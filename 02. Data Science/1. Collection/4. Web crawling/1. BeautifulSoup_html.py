# pip install bs4
from bs4 import BeautifulSoup

html='''
<html>
Naver 실시간 영화 순위
<td class = "title"> 
<div class= "tit3">
<a href="/movie/bi/mi/basic.nhn?code=158191" title="1위 영화">극한직업
</a>
</div>
</td>
</html>
'''
soup = BeautifulSoup(html,'html.parser')
print(soup)
tag=soup.td
print("\nsoup.td")
print(tag)

tag = soup.div
print("\nsoup.div")
print(tag)

tag = soup.a
print("\nsoup.a")
print(tag)

print("\ntag.name") # tag의 이름을 반환
print(tag.name)

print("\ntag.attrs") # 딕셔녀리 형태로 반환
print(tag.attrs)

print("\ntag.text")
print(tag.text)

print("\ntag.string")
print(tag.string)

print(tag["title"])