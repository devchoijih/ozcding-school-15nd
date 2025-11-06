from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from bs4 import BeautifulSoup

keyword = input("검색어를 입력해주세요 : ")
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + keyword

options_ = Options()
options_.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options_)
driver.get(url)

for i in range(5):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser") 

result = soup.select(".sds-comps-vertical-layout .sds-comps-full-layout .IoSVvu2hEbI_In6t6FAw")

for i in result:
    ad = i.select_one(".vZ_ErVj5n5d07m6XzhoL")

    if ad:
        continue

    title = i.select_one(".sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1.sds-comps-text-type-headline1.sds-comps-text-weight-sm").text
    writer = i.select_one(".sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1").text
    dsc = i.select_one(".sds-comps-text.sds-comps-text-type-body1.sds-comps-text-weight-sm").text
    link = i.select_one(".ialLiYPc7XEN3dJ4Tujv.pHHExKwXvRWn4fm5O0Hr")["href"]

    print(f"제목 : {title}")
    print(f"작성자 : {writer}")
    print(f"글요약 : {dsc}")
    print(f"링크 : {link}")
    print()

print(len(result))
driver.quit()