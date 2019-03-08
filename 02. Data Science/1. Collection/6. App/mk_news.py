import urllib.request, csv
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://news.mk.co.kr/bestClick.php')
soup = BeautifulSoup(html, 'html.parser')

titles = soup.select('dt > a')

def main() :
    f = open('mk_news_title.csv', 'w', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    for title in titles :
        title_name = title.text
        url_name = title.get('href')
        csv_writer.writerow([title_name, '!', url_name])

main()


