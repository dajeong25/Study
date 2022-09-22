## 동적 페이지 스크레이핑
#1. yes24에서 파이썬 검색
#2. 그 중 책 제목 10개만 추출 후 반환

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#yes24 접속
service = Service(executable_path="../../chromedriver.exe") 
driver = webdriver.Chrome(service=service)
location = "http://www.yes24.com/Main/Default.aspx"
driver.get(location)

#파이썬 검색
searchBox = driver.find_element(by=By.NAME, value='query')
searchBox.click()
searchBox.send_keys('파이썬')
driver.find_element(By.CSS_SELECTOR, '#yesSForm button').click() #페이지 내의 검색버튼 누름
print("파이썬 검색 후 접속")

#책제목 10개 추출
count=1 
titles = driver.find_elements(By.CSS_SELECTOR, '#yesSchList a.gd_name')
for title in titles:
    if count == 11:
        break
    print(count, title.text)
    count+=1

#모두 수행 후 창 종료
driver.close()



###################강사님 코드######################
from selenium.webdriver.common.keys import Keys

location ="http://www.yes24.com/Main/default.aspx"
SEARCH = "파이썬"
TIMEOUT = 3
  
try:
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service)    #브라우저 실행시키위한 드라이버 객체 생성 (브라우저 실행)
    driver.get(location)                          #url 요청
    driver.implicitly_wait(TIMEOUT)               #응답데이터 받을때까지 지연

    search = driver.find_element(by=By.ID, value="query")  #응답된 웹페이지에서 ID가 query인 문서 객체(Element)를 추출
    search.clear()                      #검색어 입력란 clear처리
    search.send_keys(SEARCH)             #검색어 입력
    search.send_keys(Keys.RETURN)      #엔터키 입력 , 검색어가 서버에 전송됨
   
    #검색결과 응답 페이지로부터 검색 결과 책 제목의 요소들 추출
    elements = driver.find_elements(by=By.CSS_SELECTOR, value="div.item_info > div.info_row.info_name > a.gd_name")
    print(len(elements))                             #추출된 요소 개수 출력
    driver.implicitly_wait(TIMEOUT)
        
    for idx, title in enumerate(elements):    #추출된 요소중 10개의 책 제목만 출력
            if idx==10 : break
            print(title.text)
            
except Exception:
        raise
    
finally:
     if driver is not None:
        driver.quit()
        