import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=꿀"

rep = requests.get(url) #get 기능의 이름 + 실행시킨다는 의미()
#위 코드를 실행하면 사이트를 구성함에 필요한 html,css,js 코드를 서버가 준다.

#웹 코드가 문지 중요하지 않아요 -> 데이터 타입으로만 구분합니다. 그래서 => 문서 또는 글자(텍스트)로 판단합니다.
html = rep.text

#받아온 html,css,js 코드를 python은 하나도 몰라요 => 번역을 도와줄 조력자가 필요하다.
soup = BeautifulSoup(html, "html.parser") #html에서 사용된 모든 태그의 유형을 알려줍니다.

print(soup)

soup.select("클래스명")

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
