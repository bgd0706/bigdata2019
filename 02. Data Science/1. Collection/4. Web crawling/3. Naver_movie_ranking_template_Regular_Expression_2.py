import urllib.request, csv, re
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

totals = soup
total = str(totals)

p = re.compile('code=.+title=["](.+)["].+\s+.+\s+.+\s+.+\s+.+\s+.+alt=["]([a-z]+)["].+\s+.+range ac">(.+)<')

title = p.findall(total)
print(title)

f = open('Naver_movie_ranking_regular_expression_2.csv', 'w', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['순위', '영화명', '변동폭'])
for i in range(len(title)) :
    if title[i][1] == "down" :
        csv_writer.writerow([i + 1, title[i][0], "-" + title[i][2]])
    elif title[i][1] == "up" :
        csv_writer.writerow([i + 1, title[i][0], "+" + title[i][2]])
    else :
        csv_writer.writerow([i + 1, title[i][0], " " + title[i][2]])

