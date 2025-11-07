from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pymysql

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

items = soup.select("a.product_card[data-sdui-id^='product_card/']")
print(len(items))

product_list = []
for item in items:
    category = "상의"
    product_name = item.select_one('p.text-element.text-lookup.display_paragraph:not(.semibold)').get_text(strip=True)

    if "후드" in product_name:
        brand_name = item.select_one("[data-sdui-id^='product_brand_name/'] p.semibold").get_text(strip=True)
        product_price = item.select_one(".price-info-container .label-text-container p.semibold").get_text(strip=True)

        product_info = [category, product_name, brand_name, product_price]
        product_list.append(product_info)

        print(f"제품명 : {product_name}")
        print(f"브랜드이름 : {brand_name}")
        print(f"가격 : {product_price}")
        print()

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="kream",
    charset="utf8mb4"
)

def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ()) # select * from kream3
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            connection.commit()

for i in product_list:
    execute_query(connection, "INSERT INTO KREAM (category, brand, product_name, price) VALUES (%s, %s, %s, %s)",(i[0],i[1],i[2],i[3]))

driver.quit()
