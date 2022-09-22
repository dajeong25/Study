### Q. 네이버 실시간 인기 웹툰 1~10위 제목 추출 후 csv 파일에 저장하기
import csv
from bs4 import BeautifulSoup
import requests

filename = "네이버 웹툰 인기 순위.csv"
f = open(filename, "w", encoding='utf-8')
writer = csv.writer(f)
columns_name = ['순위', '웹툰명']
writer.writerow(columns_name)

url = 'https://comic.naver.com/webtoon/weekday'

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
for rank in range(1, 10):
    cartoon_list = soup.select_one(f'#realTimeRankFavorite > li.rank0{rank} > a').string
    data = [str(rank)+"위", cartoon_list]
    writer.writerow(data)
cartoon_list = soup.select_one(f'#realTimeRankFavorite > li.rank10 > a').string
data = ["10위", cartoon_list]
writer.writerow(data)

f.close()



#강사님 풀이
#https://comic.naver.com/webtoon/weekday  네이버 실시간 인기 웹툰 1위~10위 제목 추출 후 csv파일에 저장하기

url ="https://comic.naver.com/webtoon/weekday"

filename = "네이버 웹툰 인기 순위.csv"
f = open(filename, "w", encoding="utf-8")
writer = csv.writer(f)
columns_name = ["순위", "웹툰명"] 
writer.writerow(columns_name)

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.select("ol#realTimeRankFavorite a")
for idx, cartoon in enumerate(cartoons) :
    title = cartoon.get("title")
    data = [str(idx+1), title]
    #print(data)
    writer.writerow(data)

f.close()
