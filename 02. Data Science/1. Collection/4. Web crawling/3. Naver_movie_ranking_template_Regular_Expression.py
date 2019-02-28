import urllib.request, csv, re
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

totals = soup
total = str(totals)
p = re.compile('code=.+title=["](.+)["]')
q = re.compile('alt=["](na|up|down)["]')
s = re.compile('range ac">(.+)<')

title = p.findall(total)
dir = q.findall(total);dir.pop(0)
var = s.findall(total);var.pop(0)

f = open('Naver_movie_ranking_regular_expression.csv', 'w', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['순위', '영화명', '변동폭'])
for i in range(50) :
    if dir[i] == "down" :
        csv_writer.writerow([i + 1, title[i], "-" + var[i]])
    elif dir[i] == "up" :
        csv_writer.writerow([i + 1, title[i], "+" + var[i]])
    else :
        csv_writer.writerow([i + 1, title[i], " " + var[i]])