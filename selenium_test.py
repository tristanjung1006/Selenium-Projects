import time
import openpyxl
import pyperclip
import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from openpyxl.styles import PatternFill
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse, parse_qs
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException, \
    ElementClickInterceptedException, UnexpectedAlertPresentException, NoAlertPresentException

user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
              "Safari/537.36")

# 웹브라우저 창 크기 및 웹페이지 요소 로딩 대기시간 설정
service = Service(ChromeDriverManager().install())
chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument('--disable-logging')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 15)

url_img = 'https://www.remove.bg/ko'

url = 'https://item.gmarket.co.kr/Item?goodscode=1579104167'

# 웹페이지 내용을 가져오기
response = requests.get(url, headers={"User-Agent": user_agent})
html = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, 'html.parser')

img_link = soup.find('div', class_='thumb-gallery uxecarousel')

img_element = soup.find('img')

# img 태그의 src 속성 가져오기
img_src = img_element.get('src')

img_link = 'https:' + img_src
print(img_link)

driver.get(url_img)

img_cc = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@class='text-typo-secondary select-photo-url-btn underline']")))
img_cc.click()

wait.until(EC.alert_is_present())

# alert 창으로 전환
try:
    alert = driver.switch_to.alert
    alert.send_keys(img_link)
    alert.accept()
except NoAlertPresentException:
    print("Alert이 나타나지 않았습니다.")

time.sleep(10)

img_download = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='page-content']/div/div/div/div/div[2]/div[2]/div[2]/button")))
img_download.click()

time.sleep(10)

driver.quit()
