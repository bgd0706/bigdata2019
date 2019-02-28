import urllib.request, csv
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# print(soup.prettify())

tags = soup.findAll('div', attrs={'class' : 'tit3'})
direction = soup.findAll('img', attrs={'class':'arrow'})
variation = soup.findAll('td', attrs={'class' : 'range ac'})

f = open('Naver_movie_ranking.csv', 'w', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['순위', '영화명', '변동폭'])
for i in range(50) :
    real = direction[i]["alt"]
    if real == 'down' :
        csv_writer.writerow([i + 1, tags[i].a.text, "-" + variation[i].text])
    elif real == 'up' :
        csv_writer.writerow([ i+1, tags[i].a.text, "+" +variation[i].text])
    else :
        csv_writer.writerow([i + 1, tags[i].a.text, " " + variation[i].text])

# direction = soup.findAll('td', attrs={'class':'ac'})
# real_direction = []
# for i in range(len(direction)) :
#     if i % 3 == 1 :
#         real_direction.append(direction[i])
