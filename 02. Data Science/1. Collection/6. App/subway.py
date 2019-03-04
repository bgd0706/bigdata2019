import urllib.request, csv, re
from bs4 import BeautifulSoup

html = urllib.request.urlopen("http://subway.koreatriptips.com/subway-station/DGS1/SUB40136.html")
soup = BeautifulSoup(html, 'html.parser')

totals = str(soup)
p = re.compile('<tr>\s*<td>(.*)</td>\s*<td>(.*)</td>\s*</tr>')

total = p.findall(totals)

f = open('subway_sulhwa.csv', 'w', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['시', '분'])
for i in range(0, 19) :
    for j in range(len(total[i][1].split(', '))) :
        csv_writer.writerow([total[i][0], total[i][1].split(', ')[j]])

f = open('subway_ansim.csv', 'w', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['시', '분'])
for i in range(20, 38) :
    for j in range(len(total[i][1].split(', '))) :
        csv_writer.writerow([total[i][0], total[i][1].split(', ')[j]])
