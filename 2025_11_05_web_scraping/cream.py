from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

url = "https://kream.co.kr"

#테스트용 크롬 브라우저에 옵션 적용
options_ = Options()
options_.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options_)
driver.get(url)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(1)
# 여기까지가 돋보기를 누르고 검색을 할 수 있도록 만드는 코드였습니다.

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(2)

for item in range(20):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".product_card.pc\:overflow-hidden.flex-shrink-0")
print(len(items))

for item in items:
    product_name = item.select_one('.text_body.pc\:w-fill.pc\:h-fit').text
    print(f"제품명 : {product_name}")
    print()


driver.quit()
