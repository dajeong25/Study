# 환율 정보 추출

from bs4 import BeautifulSoup
import urllib.request as req

url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
result = soup.find(class_="value").get_text()
print('미국 USD =', result)


#다른 코드
price = soup.select_one('div.head_info > span.value').string
print('usd/krw =', price)

#다른코드2
price2 = soup.find(id="exchangeList").find('div').find('span').string
print('usd/krw =', price2)
