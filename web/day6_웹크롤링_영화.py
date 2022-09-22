### Q. 영화 50위까지 영화제목, 평점, 상영시간, 장르, 감독, 배우 출력하기
import csv
from bs4 import BeautifulSoup
import requests

filename = "영화 순위.csv"
f = open(filename, "w", encoding="utf-8")
writer = csv.writer(f)
columns_name = ["영화 제목", "평점", '상영시간', '장르', '감독', '배우'] 
writer.writerow(columns_name)

url = 'https://www.imdb.com/search/title/?title_type=feature&year=2022-01-01,2022-12-31&sort=num_votes,desc&explore=languages'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

for idx in range(1, 51):
    title = soup.select_one(f"#main > div > div.lister.list.detail.sub-list > div > div:nth-child({idx}) > div.lister-item-content > h3 > a").string
    rating = soup.select_one(f'#main > div > div.lister.list.detail.sub-list > div > div:nth-child({idx}) > div.lister-item-content > div > div.inline-block.ratings-imdb-rating > strong').string
    runtime = soup.select_one(f'#main > div > div.lister.list.detail.sub-list > div > div:nth-child({idx}) > div.lister-item-content > p:nth-child(2) > span.runtime').string
    genre = soup.select_one(f'#main > div > div.lister.list.detail.sub-list > div > div:nth-child({idx}) > div.lister-item-content > p:nth-child(2) > span.genre').string.replace('\n', '').strip()
    director = soup.select_one(f'#main > div > div.lister.list.detail.sub-list > div > div:nth-child({idx}) > div.lister-item-content > p:nth-child(5) > a:nth-child(1)').string
    stars = ''
    for i in range(3, 8):
        star = soup.select_one(f'#main > div > div.lister.list.detail.sub-list > div > div:nth-child(6) > div.lister-item-content > p:nth-child(5) > a:nth-child({i})')
        if star != None:
            stars += star.string + ", "
    stars  = stars.rstrip(', ')
    movies = [idx, title, rating, runtime, genre, director, stars]
    #print(movies)
    writer.writerow(movies)
    
f.close()


#강사님 코드 활용
import csv
from bs4 import BeautifulSoup

filename = "영화_순위_2022_강사님.csv"
f = open(filename, "w", encoding="utf-8")
writer = csv.writer(f)
columns_name = ["영화 제목", "평점", '상영시간', '장르', '감독', '배우'] 
writer.writerow(columns_name)

url = 'https://www.imdb.com/search/title/?title_type=feature&year=2022-01-01,2022-12-31&sort=num_votes,desc&explore=languages'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

count=1
for movie in soup.select("div.lister-item-content"):
    if count == 51:
        break
    title = movie.select_one("h3 > a").string
    rating = movie.select_one('div.ratings-imdb-rating > strong').string
    runtime = movie.select_one('p:nth-child(2) > span.runtime').string
    genre = movie.select_one('p:nth-child(2) > span.genre').string.replace('\n', '').strip()
    director = movie.select_one('p:nth-child(5) > a:nth-child(1)').string
    stars = ''
    for i in range(3, 8):
        star = movie.select_one(f'p:nth-child(5) > a:nth-child({i})')
        if star != None:
            stars += star.string + ", "
    stars  = stars.rstrip(', ')
    movies = [count, title, rating, runtime, genre, director, stars]
    #print(movies)
    writer.writerow(movies)
    count+=1
    
f.close()