import urllib.request, csv, re, os
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(html, 'html.parser')

totals = str(soup)

p = re.compile('code=.+title=["](.+)["].+\s+.+\s+.+\s+.+\s+.+\s+.+alt=["]([a-z]+)["].+\s+.+range ac">(.+)<')

total = p.findall(totals)

upper_dir = input("상위 폴더를 입력하세요: ")
lower_dir = input("하위 폴더를 입력하세요: ")

def makeFile () :
    os.chdir('../')
    upper_len = 3*(len(os.listdir())-1) # 0 3 6 9 12 ....

    os.chdir(lower_dir+"%s" %str(len(os.listdir()))) # 파일을 만들고 싶은 naver_ranking 디렉터리에 감
    lower_len = len(os.listdir())+1 # 1 1. CSV 3 으로 반복

    f = open('movie%s.csv' % str(upper_len+lower_len), 'w', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['순위', '영화명', '변동폭'])
    for i in range(len(total)):
        if total[i][1] == "down":
            csv_writer.writerow([i + 1, total[i][0], "-" + total[i][2]])
        elif total[i][1] == "up":
            csv_writer.writerow([i + 1, total[i][0], "+" + total[i][2]])
        else:
            csv_writer.writerow([i + 1, total[i][0], " " + total[i][2]])

if os.path.exists(upper_dir) == False :
    os.mkdir(upper_dir)
os.chdir(upper_dir)  # V BigData 디렉토리로 가기

if len(os.listdir()) == 0 : # Naver_ranking 디렉터리가 하나도 없을 경우
    os.mkdir(lower_dir+"%s" % str(len(os.listdir())+1)) # Naver_ranking 디렉터리 생성
    os.chdir(lower_dir+"%s" % str(len(os.listdir())))  # Naver_ranking 위치로 가기
else : # Naver_ranking 디렉터리가 하나도 있을 경우
    os.chdir(lower_dir+"%s" % str(len(os.listdir()))) # 그 디렉터리로 간다.
    if (len(os.listdir()) == 3) : # 만약 그 디렉터리에 있는 파일이 3개 있을 경우
        os.chdir('../') # 상위 폴더로 가서
        os.mkdir(lower_dir+"%s" % str(len(os.listdir()) + 1)) # 그 다음 Naver_ranking 디렉터리를 생성한다.
        os.chdir(lower_dir+"%s" % str(len(os.listdir())))
makeFile()