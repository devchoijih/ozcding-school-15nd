## 표준모듈
## 다양한 표준 모듈을 볼 수 있는 공식 사이트: https://docs.python.org/ko/3/library/index.html
## 파이썬에 기본적으로 내장되어 있는 모듈을 표준모듈이라고 함

## 사용방법 import 모듈 이름

"""
import math

print(math.sin(5))
print(math.cos(5))
print(math.ceil(3.6))
print(math.floor(4.1))
"""

"""

from math import sin,cos,ceil,floor

print(sin(5))
print(cos(5))
print(ceil(3.6))
print(floor(4.1))

"""

"""
from math import *

print(sin(5))
print(cos(5))
print(ceil(3.6))
print(floor(4.1))

"""

"""
from math import m

print(m.sin(5))
print(m.cos(5))
print(m.ceil(3.6))
print(m.floor(4.1))

"""

##외부모듈
## pip install 모듈 이름 //powersell 이용

## beautifulsoup4 공식 페이지 : https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/

"""
from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://www.weather.go.kr/w/weather/forecast/short-term.do?stnId=109")

soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

url = "https://www.weather.go.kr/w/weather/forecast/short-term.do?stnId=109"

opts = Options()
opts.add_argument("--headless=new")
driver = webdriver.Chrome(options=opts)
driver.get(url)

# JS가 표를 채울 시간 잠깐 대기
time.sleep(2)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")

# 페이지 구조에 맞는 선택자(예: 시간별 표, 카드 등)로 골라서 파싱
# 예시) 표 행 가져오기 (필요 시 개발자도구로 클래스명 확인)
for row in soup.select("table tbody tr"):
    tds = [td.get_text(strip=True) for td in row.select("th,td")]
    print(tds)