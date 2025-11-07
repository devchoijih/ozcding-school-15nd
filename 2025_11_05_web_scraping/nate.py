import re, time, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def human_type(el, text, a=0.05, b=0.15):
    el.clear()
    for ch in text:
        el.send_keys(ch)
        time.sleep(random.uniform(a, b))

options = Options()

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# 진짜 브라우저 User-Agent로 바꿔라 (예시는 Windows Chrome 최신)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.7390.123 Safari/537.36")

# (선택) 창 크기와 언어 설정 — 사람이 쓰는 환경처럼
options.add_argument("--window-size=1200,900")
options.add_argument("--lang=ko-KR")

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

driver.get("https://www.nate.com")

# 1) 아이디 입력
id_box = wait.until(EC.element_to_be_clickable((By.ID, "ID")))
human_type(id_box, "아뒤")

# 2) 가짜 비번칸(#PASSDM) 클릭 → 진짜(#PASSWD) 보이길 기다림
dm = wait.until(EC.element_to_be_clickable((By.ID, "PASSDM")))
dm.click()

# 진짜 패스워드 input이 표시될 때까지 대기 (display:none → visible)
pw_box = wait.until(EC.visibility_of_element_located((By.ID, "PASSWD")))

# 혹시 여전히 숨김이면 강제로 표시(백업)
if not pw_box.is_displayed():
    driver.execute_script("""
        document.getElementById('PASSDM').style.display='none';
        var p = document.getElementById('PASSWD');
        p.style.display = '';
        p.removeAttribute('readonly');
        p.removeAttribute('disabled');
        p.focus();
    """)

pw_box = wait.until(EC.element_to_be_clickable((By.ID, "PASSWD")))
human_type(pw_box, "비번")

# 3) 로그인 버튼 클릭
login_btn = wait.until(EC.element_to_be_clickable((By.ID, "btnLOGIN")))
time.sleep(random.uniform(0.2, 0.6))
login_btn.click()

time.sleep(random.uniform(2.5, 4.0))

try:
    mail_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@href,'mail3.nate.com') and contains(.,'메일')]")
    ))
    mail_link.click()
except Exception:
    # 직접 이동(최후 수단)
    driver.get("https://mail3.nate.com/#INBOX")

# 메일 로딩 대기
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".list_body")))

subjects = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.subject.nmSubject"))
)

# 0번째 <p> 안의 a.title 클릭
a_tag = subjects[0].find_element(By.CSS_SELECTOR, "a.title")
a_tag.click()

frame = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".nmReadViewContent iframe._nmContent"))
)
driver.switch_to.frame(frame)

def get_by_label(label_text):
    xpath = f"//td[normalize-space()='{label_text}']/following-sibling::td[1]"
    el = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    return el.text.strip()

시간 = get_by_label("시간")
위치 = get_by_label("위치")
기기 = get_by_label("기기")

# 위치에서 IP만 추출 (선택)
m = re.search(r"\(([\d\.]+)\)", 위치)
ip = m.group(1) if m else None

print("시간:", 시간)
print("위치:", 위치)
print("IP:", ip)
print("기기:", 기기)

# 끝났으면 프레임 복귀
driver.switch_to.default_content()