import urllib.request, csv
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://news.mk.co.kr/bestClick.php')
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# print(soup.prettify())

# titles = soup.findAll('dt', attrs={'class' : 'tit'})
titles = soup.select('dt > a')

print(titles)
f = open('mk_news_title.csv', 'w', newline='')
csv_writer = csv.writer(f)
for title in titles :
    title_name = title.text
    url_name = title.get('href')
    # csv_writer.writerow([title])
    print(title_name)
    print(url_name)
