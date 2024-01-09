import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urlparse, parse_qs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
              "Safari/537.36")

# 웹브라우저 창 크기 및 웹페이지 요소 로딩 대기시간 설정
service = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument('--disable-logging')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 15)

url = "https://trendmecca.co.kr/product/메종키츠네-hu00542kt1036-h150-베이비-폭스-패치-바이컬러-브이넥-골프-가디건-트랜드메카/48419/category/1/"
base_home_url = "https://trendmecca.co.kr/index.html"

# 주어진 URL로 이동
driver.get(url)

# 현재 URL 확인
current_url = driver.current_url

# 기본 홈 주소로 리디렉션되었는지 확인
if current_url == base_home_url:
    print("현재 주소가 기본 홈 주소로 리디렉션되었습니다.")
    # 리디렉션에 대한 처리를 추가하세요.
    # 예를 들어, 다른 작업 수행 또는 다른 페이지로 이동 등...
else:
    print("현재 주소는 기본 홈 주소로 리디렉션되지 않았습니다.")
    # 링크 클릭 또는 다른 동작 수행...

# 브라우저 종료
driver.quit()


#
# user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 "
#               "Safari/537.36")
#
# url = 'https://www.hmall.com/pd/pda/itemPtc?sectId=2731205&slitmCd=2154219580'

# 웹브라우저 창 크기 및 웹페이지 요소 로딩 대기시간 설정
# service = Service(ChromeDriverManager().install())
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument('--window-size=1920,1080')
# chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
#                             'like Gecko) Chrome/119.0.0.0 Safari/537.36')
# driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)

# size_cell = "블랙/L"
#
# # ,을 기준으로 문자열 분리
# split_values = str(size_cell).split(',')
#
# # 앞 뒤에 있는 단어를 각각 다른 변수에 저장
# first_word = split_values[0].strip() if len(split_values) > 0 else ""
# second_word = split_values[1].strip() if len(split_values) > 1 else ""
#
# print(first_word)
# print(second_word)
#
# # "slitmCd=" 다음의 인덱스를 찾기
# start_index = url.find("slitmCd=")
#
# # 숫자 시작 인덱스 계산하여 10자리 숫자 추출
# number_start_index = start_index + len("slitmCd=")
# slitmCd_number = url[number_start_index:number_start_index + 10]
#
# price_url = f"https://www.hmall.com/api/hf/dp/v1/item-ptc/item-basic?slitmCd={slitmCd_number}"
# response = requests.get(price_url, headers={"User-Agent": user_agent})
# data_price = response.text
# datas_price = json.loads(data_price)
# current_price = datas_price["respData"]["itemPtc"]["bbprc"]
# print(current_price)
# option_url = f"https://www.hmall.com/api/hf/dp/v1/item-ptc/item-stockcount?slitmCd={slitmCd_number}"
# response = requests.get(option_url, headers={"User-Agent": user_agent})
# data_opt = response.text
# datas_opt = json.loads(data_opt)
# options = datas_opt["respData"]["stockList"]
# for option in options:
#     if str(size_cell) in option.get("uitmTotNm"):
#         quantity = option["stockCount"]
#         if quantity == 0:
#             soldout = "품절"
#         else:
#             soldout = ""
#         break
#     else:
#         soldout = ""
#
# # 결과 출력
# print(f'현재 가격: {current_price} 재고량: {quantity} {soldout}')

# # ,을 기준으로 문자열 분리
# split_values = str(size_cell).split(',')
#
# # 앞 뒤에 있는 단어를 각각 다른 변수에 저장
# first_word = split_values[0].strip() if len(split_values) > 0 else ""
# second_word = split_values[1].strip() if len(split_values) > 1 else ""
# print(first_word)
# print(second_word)
#
# # URL 파싱
# parsed_url = urlparse(url)
# # 원하는 부분 추출
# product_id = parsed_url.path.split('/')[-1]
#
# if product_id[0:2] == "LE":
#     # 쿼리 스트링 파싱
#     query_params = parse_qs(parsed_url.query)
#     # sitmNo 값 추출
#     sitmNo_value = query_params.get('sitmNo', [None])[0]
#     new_url = f"https://pbf.lotteon.com/product/v2/detail/search/base/sitm/{sitmNo_value}"
# else:
#     new_url = f"https://pbf.lotteon.com/product/v2/detail/search/base/pd/{product_id}"
#
# print(url)
# print(new_url)
#
# # 새로운 URL로 요청을 보내어 JSON 데이터 가져오기
# response = requests.get(new_url, headers={"User-Agent": "Mozilla/5.0"})
# data = response.text
#
# # options에서 value값이 240인 부분에서 quantity값 추출
# datas = json.loads(data)
# current_price = datas["data"]["priceInfo"]["slPrc"]
# viewOptions = datas["data"]["optionInfo"]["optionList"]
# if len(viewOptions) == 1:
#     for option in viewOptions:
#         for opt in option["options"]:
#             if str(size_cell) in opt["label"]:
#                 if str(opt["disabled"]) == "True":
#                     soldout = "품절"
#                 else:
#                     soldout = ""
#                 break
#             else:
#                 if str(opt["disabled"]) == "True":
#                     soldout = "품절"
#                 else:
#                     soldout = ""
# else:
#     driver.get(url)
#     # 첫 번째 div 클릭
#     first_option_wrap = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//div[@class='optionWrap block withLabel']"))
#     )
#     first_option_wrap.click()
#
#     # first_sel의 하위 selectLists 클래스를 가진 ul 태그 선택
#     ul_element = first_option_wrap.find_element(By.CLASS_NAME, "selectLists")
#
#     # ul 태그의 하위 li 태그들 중에서 disabled 클래스를 갖고 있지 않은 것 선택
#     li_elements = ul_element.find_elements(By.CSS_SELECTOR, "li:not(.disabled)")
#
#     # 각 li 태그에서 caption 클래스를 가진 span 태그의 텍스트를 추출하여 리스트에 저장
#     captions_0 = [li.text for li in li_elements]
#
#     # 저장된 리스트 출력
#     print(captions_0)
#     if first_word in captions_0:
#         # 첫 번째 div 하위 태그 중 selectLists 클래스를 가진 ul 태그의 하위 태그들 중 그레이(194) 텍스트를 가진 span 클릭
#         gray_span_xpath = f"//ul[@class='selectLists']//span[text()='{first_word}']"
#         gray_span = wait.until(EC.element_to_be_clickable((By.XPATH, gray_span_xpath)))
#         gray_span.click()
#
#         sel = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "topOptionContent")))
#         first_sel = sel.find_elements(By.XPATH,
#                                       ".//*[contains(@class, 'optionWrap') and contains(@class, 'block') and contains("
#                                       "@class, 'withLabel')]")[1]
#         first_sel.click()
#
#         # first_sel의 하위 selectLists 클래스를 가진 ul 태그 선택
#         ul_element = first_sel.find_element(By.CLASS_NAME, "selectLists")
#
#         # ul 태그의 하위 li 태그들 중에서 disabled 클래스를 갖고 있지 않은 것 선택
#         li_elements = ul_element.find_elements(By.CSS_SELECTOR, "li:not(.disabled)")
#
#         # 각 li 태그에서 caption 클래스를 가진 span 태그의 텍스트를 추출하여 리스트에 저장
#         captions = [li.find_element(By.CLASS_NAME, "caption").text for li in li_elements]
#
#         # 저장된 리스트 출력
#         print(captions)
#         if second_word in captions:
#             soldout = ""
#         else:
#             soldout = "품절"
#     else:
#         soldout = "품절"
#
# print(f'현재 가격: {current_price} {soldout}')

# # 웹 페이지 열기
# driver.get(url)
#
# # price-definition-ins 클래스를 가진 span 태그의 하위 태그들 중에서 strong 태그의 텍스트값 추출
# price_definition_ins = driver.find_element(By.CLASS_NAME, "price-definition-ins")
# strong_text = price_definition_ins.find_element(By.XPATH, ".//strong")
# current_price = strong_text.text
#
# # sel 클래스를 가진 div 태그의 하위 태그들 중에서 첫 번째 태그 클릭
# sel = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "sel")))
# first_sel = sel.find_elements(By.XPATH, ".//*[contains(@id, 'Sel')]")[0]
# first_sel.click()
#
# # 첫 번째 태그의 하위 태그 중 ul 태그 찾기
# ul_element = first_sel.find_element(By.TAG_NAME, "ul")
#
# # ul_element의 텍스트값을 리스트에 저장
# ul_text = ul_element.text
# ul_text_list = ul_text.split('\n')
# print(ul_text_list)
#
# # DJ6914 블랙이 포함된 경우 해당 a 태그 클릭
# if "250" in ul_element.text:
#     a_tag_black = sel.find_element(By.XPATH, ".//a[contains(text(), '250')]")
#     a_tag_black.click()
#
#     # sel 클래스를 가진 div 태그의 두 번째 태그 클릭 (만약 두 번째 태그가 존재한다면)
#     second_sel = sel.find_elements(By.XPATH, ".//*[contains(@id, 'Sel')]")[2]
#     if second_sel:
#         second_sel.click()
#
#         # 두 번째 태그의 하위 태그 중 ul 태그 찾기
#         ul_element_second = second_sel.find_element(By.TAG_NAME, "ul")
#
#         # ul_element의 텍스트값을 리스트에 저장
#         ul_text = ul_element_second.text
#         ul_text_list_2 = ul_text.split('\n')
#         print(ul_text_list_2)
#     else:
#         print("본 제품은 단품 상품입니다.")
#         soldout = ""
# else:
#     print("해당 옵션은 모두 품절되었습니다.")
#     soldout = "품절"
#
# print(f'현재 가격: {current_price} {soldout}')

# # gds_amt 클래스를 가진 div 태그의 하위에서 dd 태그의 텍스트값 가져오기
# gds_amt_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gds_amt')))
# gds_amt_text = gds_amt_element.find_element(By.TAG_NAME, 'dd').text
# current_price = gds_amt_text
#
# # gds_btns 클래스를 가진 div 태그 선택
# gds_btns_div = driver.find_element(By.CLASS_NAME, 'gds_btns')
#
# # disabled 클래스를 가진 button 태그 찾기
# disabled_button = gds_btns_div.find_element(By.CSS_SELECTOR, 'button[disabled="disabled"]')
#
# if disabled_button:
#     print("disabled 클래스를 가진 button이 있습니다.")
#     soldout = "품절"
# else:
#     print("disabled 클래스를 가진 button이 없습니다.")
#     # btn_opt_slt pg 클래스를 가진 첫 번째 div 태그 클릭
#     first_btn_opt_slt = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_opt_slt.pg')))
#     first_btn_opt_slt.click()
#
#     # 첫 번째 div 태그의 하위에서 option이라는 name을 가진 li 태그들 중에서 품절이 아닌 것들 추출
#     option_list = first_btn_opt_slt.find_elements(By.CSS_SELECTOR, 'li[name="option"]')
#     option_texts = [option.find_element(By.CSS_SELECTOR, 'span').text for option in option_list if
#                     "품절" not in option.text]
#     print(option_texts)
#
#     # BKS가 리스트에 있다면 해당 값을 가진 li 태그 클릭
#     if "250" in option_texts:
#         bks_option = first_btn_opt_slt.find_element(By.CSS_SELECTOR, 'li[data-opt_val_nm="250"]')
#         bks_option.click()
#         soldout = ""
#     else:
#         soldout = "품절"
#         print("본 제품의 해당 옵션은 품절입니다.")
#
#     time.sleep(3)
#
#     # 두 번째 div 태그가 존재한다면 클릭
#     second_btn_opt_slt = driver.find_elements(By.CLASS_NAME, 'btn_opt_slt.pg')[1]
#     if second_btn_opt_slt:
#         second_btn_opt_slt.click()
#
#         # 두 번째 div 태그의 하위에서 option이라는 name을 가진 li 태그들 중에서 품절이 아닌 것들 추출
#         second_option_list = second_btn_opt_slt.find_elements(By.CSS_SELECTOR, 'li[name="option"]')
#         second_option_texts = [option.find_element(By.CSS_SELECTOR, 'span').text for option in second_option_list if
#                                "품절" not in option.text]
#         print(second_option_texts)
#         if "100" in second_option_texts:
#             soldout = ""
#         else:
#             soldout = "품절"
#
# print(f'현재 가격: {current_price} {soldout}')

# # select-list-box 클래스를 가진 div 태그 중 첫 번째 태그 클릭
# first_select_list_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='select-list-box ']")))
# first_select_list_box.click()
#
# black_span = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='select-list']//a[text()='BLACK']")))
# black_span.click()
#
# # select-list 클래스를 가진 두 번째 ul 태그 선택
# second_select_list_box = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='select-list-box '])[2]")))
# second_select_list_box.click()
# ul_element = driver.find_elements(By.CLASS_NAME, "select-list-box ")[1]
#
# # ul 태그의 하위 a 태그들 중 텍스트값이 "품절"이 아닌 경우 텍스트를 리스트에 저장
# non_soldout_texts = [a.text for a in ul_element.find_elements(By.TAG_NAME, "a") if "품절" not in a.text]
#
# # 결과 출력
# print(non_soldout_texts)

# # 1. 첫 번째 div 클릭
# first_option_wrap = driver.find_element(By.CSS_SELECTOR, ".optionContent .optionWrap.withLabel")
# first_option_wrap.click()
#
# # 첫 번째 div 하위 태그 중 selectLists 클래스를 가진 ul 태그의 하위 태그들 중 그레이(194) 텍스트를 가진 span 클릭
# gray_span = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "//ul[@class='selectLists']//span[text()='그레이(194)']"))
# )
# gray_span.click()
#
# # 2. 두 번째 div 클릭
# second_option_wrap = driver.find_element(By.CSS_SELECTOR, ".optionContent .optionWrap.withLabel:nth-child(2)")
# second_option_wrap.click()
#
# # 두 번째 div 하위 태그 중 selectLists 클래스를 가진 ul 태그의 하위 태그들 중 disabled 클래스가 없는 li 태그의 caption 값을 리스트에 저장
# lis = driver.find_elements(By.CSS_SELECTOR, ".optionContent .optionWrap.withLabel:nth-child(2) .selectLists li:not(.disabled)")
# caption_values = [li.find_element(By.CSS_SELECTOR, ".caption").text for li in lis]
#
# print("Captions:", caption_values)

# optvalnm_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@name='optSelect0']")))
# optvalnm_option.click()
#
# optselect0_select = wait.until(EC.element_to_be_clickable((By.XPATH, f"//option[@optvalnm='WHITE(100)']")))
# optselect0_select.click()
#
# # optvalnm이 "L"인 option 태그 클릭
# optvalnm_option_2 = wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@name='optSelect1']")))
#
# # 선택된 태그의 모든 하위 옵션 태그들의 텍스트 추출
# options_text = [option.text for option in optvalnm_option_2.find_elements(By.TAG_NAME, 'option') if '품절' not in option.text]
#
# # options_text 출력
# print(options_text)

# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# html = response.text
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# # name이 'option_list'인 ul 태그 찾기
# option_list_ul = soup.find('ul', {'name': 'option_list'})
#
# # ul 태그 출력
# if option_list_ul:
#     print(option_list_ul)
# else:
#     print("name이 'option_list'인 ul 태그를 찾을 수 없습니다.")
#
# # class가 'g_self'인 dl 태그 찾기
# g_self_dl = soup.find('dl', class_='g_self')
#
# # dl 태그 출력
# if g_self_dl:
#     print(g_self_dl)
# else:
#     print("class가 'g_self'인 dl 태그를 찾을 수 없습니다.")

# # 원본 URL
# original_url = "https://www.lotteon.com/p/product/LE1000194491?sitmNo=LE1000194491_1001157077&mall_no=2&dp_infw_cd=SCH%EC%A7%80%EA%B0%91&areaCode=SCH"
# # URL 파싱
# parsed_url = urlparse(original_url)
# # Query 파싱
# parsed_query = parse_qs(parsed_url.query)
# # 원하는 부분 추출
# product_id = parsed_url.path.split('/')[-1]
# # 새로운 URL 생성
# new_url = f"https://pbf.lotteon.com/product/v2/detail/search/base/pd/{product_id}"
# print(new_url)
#
# # 새로운 URL로 요청을 보내어 JSON 데이터 가져오기
# response = requests.get(new_url, headers={"User-Agent": "Mozilla/5.0"})
# data = response.text
#
# size_cell = ""
#
# # options에서 value값이 240인 부분에서 quantity값 추출
# datas = json.loads(data)
# current_price = datas["data"]["priceInfo"]["slPrc"]
# viewOptions = datas["data"]["optionInfo"]["optionList"]
#
# for option in viewOptions:
#     for opt in option["options"]:
#         if str(size_cell) in opt["label"]:
#             if opt["disabled"]:
#                 soldout = "품절"
#             else:
#                 soldout = ""
#         else:
#             if opt["disabled"]:
#                 soldout = "품절"
#             else:
#                 soldout = ""
#
# print(f'현재 가격: {current_price} {soldout}')
# # 웹페이지 내용을 가져오기
# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# html = response.text
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# optimum_discount_price = soup.find('span', id='span_optimum_discount_price')
# price_text = ''
#
# for element in optimum_discount_price.contents:
#     if element.name == 'span' and 'style' in element.attrs:
#         # 스타일 속성을 가진 span 태그 (무시)
#         continue
#     # 스타일이 없는 태그의 텍스트 추출
#     price_text += str(element)
#
# # 'oban_list' 클래스를 가진 ol 태그 찾기
# ol_element = soup.find('ol', class_='oban_list')
#
# # 결과를 저장할 리스트 초기화
# strong_texts = []
#
# size_cell = "S56UI0128 P4455 T8013"
#
# if ol_element:
#     # ol 태그의 하위 li 태그들 중에서 soldout 클래스를 가진 것들 찾기
#     soldout_li_elements = ol_element.find_all('li', class_='soldout')
#
#     for soldout_li in soldout_li_elements:
#         # li 태그의 하위 a 태그 찾기
#         a_element = soldout_li.find('a')
#         if a_element:
#             # a 태그의 하위 div 태그 중 oban_model 클래스를 가진 것 찾기
#             oban_model_div = a_element.find('div', class_='oban_model')
#             if oban_model_div:
#                 # div 태그의 하위 strong 태그 텍스트 추출하여 리스트에 저장
#                 strong_element = oban_model_div.find('strong')
#                 if strong_element:
#                     strong_texts.append(strong_element.get_text(strip=True))
#                     if size_cell in strong_texts:
#                         soldout = "품절"
#                     else:
#                         soldout = ""
#                 else:
#                     print("Strong 태그를 찾을 수 없습니다.")
#                     soldout = ""
#             else:
#                 print("oban_model 클래스를 가진 div 태그를 찾을 수 없습니다.")
#                 soldout = ""
#         else:
#             print("a 태그를 찾을 수 없습니다.")
#             soldout = ""
# else:
#     print("본 제품은 단품 상품입니다.")
#     soldout = ""
#
# # 결과 출력
# current_price = price_text.strip()
# print(f'현재 가격: {current_price} {soldout}')

# # "new"를 "info"로 바꾸기
# modified_url = url.replace("/new?", "/info?")
#
# response = requests.get(modified_url)
#
# # JSON 파싱
# data = response.json()
#
# current_price = data.get("productPrice", {}).get("sellAmt")
# print(current_price)
#
# size_cell = ""
#
# # prdtOptnNo가 300인 부분의 totalStockQty 값 출력
# for option in data.get("productOption", []):
#     totalStockQty = option.get("prdtOptnNo", "Not found")
#     if totalStockQty == str(size_cell):
#         print("totalStockQty: " + totalStockQty)
#         if option.get("totalStockQty", "Not found") == "74":
#             soldout = "품절"
#         else:
#             soldout = ""
#         break
# else:
#     print("Option with prdtOptnNo 300 not found.")
#     soldout = ""
#     totalStockQty = option.get("totalStockQty", "Not found")
#
# soldout += str(totalStockQty)
#
# print(f'현재 가격: {current_price} 재고량: {soldout}')

# size = "2"
#
# # HTTP 요청이 성공했는지 확인
# if response.status_code == 200:
#     # BeautifulSoup을 사용하여 HTML 파싱
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     # price03 클래스를 가진 span 태그의 텍스트 출력
#     price03_element = soup.find("span", class_="price03")
#     if price03_element:
#         current_price = price03_element.get_text(strip=True)
#     else:
#         print("price03 클래스를 가진 span 태그를 찾을 수 없습니다.")
#
#     # optSelect0 name을 가진 select 태그의 하위 option 태그들의 텍스트 출력
#     opt_select0_element = soup.find("select", {"name": "optSelect0"})
#     if opt_select0_element:
#         option_texts = [option.get_text(strip=True) for option in opt_select0_element.find_all("option") if
#                         "품절" not in option.get_text(strip=True)]
#         if str(size) in option_texts:
#             soldout = ""
#         elif "단품" in option_texts:
#             soldout = ""
#         else:
#             soldout = "품절"
#     else:
#         print("optSelect0 name을 가진 select 태그를 찾을 수 없습니다.")
# else:
#     print(f"HTTP 요청 오류: {response.status_code}")
#
# print(f'현재 가격: {current_price} {soldout}')

# # HTTP GET 요청
# response = requests.get(url)
#
# # HTTP 요청이 성공했는지 확인
# if response.status_code == 200:
#     # BeautifulSoup을 사용하여 HTML 파싱
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     # sale 클래스를 가진 dd 태그의 하위 em 태그의 텍스트 출력
#     sale_element = soup.find("dd", class_="sale")
#     if sale_element:
#         em_element = sale_element.find("em")
#         if em_element:
#             current_price = em_element.get_text(strip=True)
#             soldout = ""
#         else:
#             print("em 태그를 찾을 수 없습니다.")
# else:
#     print(f"HTTP 요청 오류: {response.status_code}")
#
# print(f'현재 가격: {current_price} {soldout}')


# # /product와 ? 사이에 /info 문자열을 추가하여 원하는 주소로 변환
# desired_url = url.replace("/product?", "/product/info?")
#
# # 변환된 주소로 HTTP GET 요청
# response = requests.get(desired_url)
#
# # HTTP 요청이 성공했는지 확인
# if response.status_code == 200:
#     # JSON 데이터 파싱
#     product_data = response.json()
#
#     # productPrice의 sellAmt 값 출력
#     current_price = product_data.get("productPrice", {}).get("sellAmt")
#
#     size = ""
#
#     # productOption에서 optnName이 220인 부분의 totalStockQty 값 출력
#     product_options = product_data.get("productOption", [])
#     for option in product_options:
#         if option.get("optnName") == str(size):
#             total_stock_qty = option.get("totalStockQty")
#             if total_stock_qty == 0:
#                 soldout = "품절"
#             else:
#                 soldout = ""
#             break
#         else:
#             total_stock_qty = option.get("totalStockQty")
#             if total_stock_qty == 0:
#                 soldout = "품절"
#             else:
#                 soldout = ""
# else:
#     print(f"HTTP 요청 오류: {response.status_code}")
#
# print(f'현재 가격: {current_price} 재고량: {total_stock_qty} {soldout}')

# # class가 'item_price_wrap'인 div 태그의 하위 strong 태그를 선택
# i_tag = soup.select_one('.c_price')
#
# # strong 태그의 하위 em 태그의 텍스트를 추출
# if i_tag:
#     current_price = i_tag.find('i').get_text()
#     print(current_price)
# else:
#     print("해당 요소를 찾을 수 없습니다.")
#
# # id가 'selectMulti'인 select 태그를 선택
# select_tag = soup.find('select', id='selectMulti')
#
# size = "LKH/100(L)"
#
# if select_tag:
#     # select 태그의 하위에 있는 모든 옵션 태그를 선택
#     option_tags = select_tag.find_all('option')
#
#     # '품절'이라는 텍스트가 없는 옵션의 텍스트를 추출하여 리스트에 저장
#     text_list = [option.get_text() for option in option_tags if '품절' not in option.get_text()]
#
#     print(text_list)
#
#     if str(size) in text_list:
#         soldout = ""
#     else:
#         soldout = "품절"
# else:
#     print("본 제품은 단품 상품입니다.")
#     soldout = ""
#
# print(f'현재 가격: {current_price} {soldout}')

# # URL을 '/'로 분할하고, 그 중에서 마지막 부분을 선택한 후 '+'를 기준으로 다시 분할
# url_parts = url.split('/')
# last_part = url_parts[-1].split('?')[0]
#
# # 추출된 부분에서 처음 8자리를 선택
# extracted_number = last_part[-8:]
#
# # 새로운 URL 생성
# new_url = f"https://displaygateway.trenbe.com/v1/sdp?goodsno={extracted_number}"
#
# # 새로운 URL로 요청을 보내어 JSON 데이터 가져오기
# response = requests.get(new_url, headers={"User-Agent": "Mozilla/5.0"})
# data = response.text
#
# size = None
# # options에서 value값이 240인 부분에서 quantity값 추출
# options = json.loads(data)
# current_price = options["data"]["product"]["finalPrice"]
# viewOptions = options["data"]["product"]["options"]
# quantity = ""
# for option in viewOptions:
#     if option.get("value") == str(size):
#         quantity = option["quantity"]
#         if quantity == 0:
#             soldout = "품절"
#         else:
#             soldout = ""
#         break
#     else:
#         soldout = ""
#
# # 결과 출력
# print("최종 URL:", new_url)
# print("Quantity 값:", quantity)
# print(f'현재 가격: {current_price} {size} {soldout}')

# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# # total-price-view view_price member-price-2 클래스를 가진 span 태그의 텍스트 추출
# current_price = soup.find('span', class_='total-price-view view_price member-price-2').get_text(strip=True)
#
# size_cell = None
# # '그레이 / L' 값을 가진 option 태그의 data-stock 속성 값을 출력
# gray_l_option = soup.find('select', id='opt').find('option', {'value': {size_cell}})
# if gray_l_option:
#     data_stock_value = gray_l_option.get('data-stock')
#     if data_stock_value == 0:
#         soldout = "품절"
#     else:
#         soldout = data_stock_value
# else:
#     print("Option '그레이 / L'을 찾을 수 없습니다.")
#     soldout = "품절"
#
# print(f'현재 가격: {current_price} {size_cell} 재고량: {soldout}')

# # price_cost라는 class를 가진 span태그에서 추출
# price_cost = soup.find('span', class_='prod-price')
# print(price_cost)
# current_price = price_cost.get_text(strip=True)
# print(current_price)
#
# # "new"를 "info"로 바꾸기
# modified_url = url.replace("/new?", "/info?")
# print(modified_url)
#
# response = requests.get(modified_url, headers={"User-Agent": "Mozilla/5.0"})
# html = response.text
#
# # JSON 파싱
# data = json.loads(html)
#
# # prdtOptnNo가 300인 부분의 totalStockQty 값 출력
# for option in data.get("productOption", []):
#     if option.get("prdtOptnNo") == "300":
#         if option.get("totalStockQty", "Not found") == 0:
#             soldout = "품절"
#         else:
#             soldout = ""
#         print("totalStockQty:", option.get("totalStockQty", "Not found"))
#         break
# else:
#     print("Option with prdtOptnNo 300 not found.")
#
# print("현재 가격: " + current_price + " " + soldout)
# ssg_price = soup.find('em', class_='ssg_price')
# current_price = ssg_price.get_text(strip=True)
#
# # cdtl_select_lst _drop_list 클래스를 가진 ul 태그 찾기
# ul_element = soup.find('ul', class_='cdtl_select_lst _drop_list')
#
# # ul_element가 존재하는 경우에만 계속 진행
# if ul_element:
#     # li 태그 중에서 stock disabled soldout_link 클래스가 없는 것들 찾기
#     valid_li_tags = ul_element.find_all('li', class_=lambda x: 'stock' not in x.split())
#
#     # 각 li 태그의 하위 txt 클래스를 가진 span 태그의 텍스트 추출
#     txt_values = [li.find('span', class_='txt').text.strip() for li in valid_li_tags]
#
#     # 결과 출력
#     print(txt_values)
# else:
#     print("ul 태그를 찾을 수 없습니다.")
#
# print("현재 가격: " + current_price + " ")
# # discount라는 class를 가진 p 태그 찾기
# discount_element = soup.find('p', class_='discount')
# price_element = discount_element.find('em')
# current_price = price_element.get_text(strip=True)
#
# index = url.find('slitmCd=')
# if index != -1:
#     slitmCd_value = url[index + len('slitmCd='):index + len('slitmCd=') + 10]
#     payload = {'slitmCd': {slitmCd_value}}
#     url = 'https://www.hmall.com/p/pda/selectUitmPrfr.do'
#
#     response = requests.post(url, data=payload)
#
#     if response.status_code == 200:
#         # HTML을 파싱
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         # data 클래스를 가진 p 태그들 찾기
#         data_paragraphs = soup.find_all('p', class_='data')
#
#         # 각 p 태그의 텍스트를 리스트에 저장
#         data_texts = [paragraph.get_text(strip=True) for paragraph in data_paragraphs]
#
#         # 결과 출력
#         print(data_texts)
#         if '260' in data_texts:
#             soldout = ""
#         else:
#             soldout = "품절"
#
#     else:
#         print(f"Failed to fetch data. Status code: {response.status_code}")
# else:
#     print("URL에서 slitmCd를 찾을 수 없습니다.")

# print("현재 가격: " + current_price + " " + soldout)

# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# html = response.text
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# # product_article_price라는 class를 가진 span 태그 찾기
# price_element = soup.find('span', class_='product_article_price')
# current_price = price_element.get_text(strip=True)
#
# # option1이라는 id를 가진 select 태그 찾기
# option_element = soup.find('select', id='option1')
#
# # option_element가 존재하는 경우에만 계속 진행
# if option_element:
#     # option_element 하위에 있는 모든 option 태그 찾기
#     option_tags = option_element.find_all('option')
#
#     # 각 option 태그의 텍스트값을 리스트에 저장
#     option_texts = [option.text.strip() for option in option_tags]
#
#     # 결과 출력
#     print(option_texts)
# else:
#     print("Option1 select 태그를 찾을 수 없습니다.")
#
# print("현재 가격: " + current_price)

# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# html = response.text
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# print(soup)
# # price_red라는 class를 가진 span 태그 선택
# price_red_element = soup.find('span', class_='price_red')
# print(price_red_element)
#
# if price_red_element:
#     strong_tag = price_red_element.find('strong')
#     price_present = strong_tag.get_text(strip=True)
#     print(price_present)

# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# html = response.text
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# # option1이라는 id를 가진 select 태그 찾기
# option_element = soup.find('select', id='option1')
#
# # option_element가 존재하는 경우에만 계속 진행
# if option_element:
#     # option_element 하위에 있는 모든 option 태그 찾기
#     option_tags = option_element.find_all('option')
#
#     # 각 option 태그의 텍스트값을 리스트에 저장
#     option_texts = [option.text for option in option_tags]
#
#     # 결과 출력
#     print(option_texts)
# else:
#     print("Option1 select 태그를 찾을 수 없습니다.")

# # 웹페이지 내용을 가져오기
# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# html = response.text
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# optimum_discount_price = soup.find('span', id='span_optimum_discount_price')
# price_text = ''
#
# for element in optimum_discount_price.contents:
#     if element.name == 'span' and 'style' in element.attrs:
#         # 스타일 속성을 가진 span 태그 (무시)
#         continue
#     # 스타일이 없는 태그의 텍스트 추출
#     price_text += str(element)
#
# # 가격 텍스트 출력
# print(price_text.strip())
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# # 'select' 태그에서 'option' 태그들 찾기
# select_element = soup.find('select', id='product_option_id1')
# option_tags = select_element.find_all('option')
#
# # 품절이 아닌 'option' 태그의 텍스트를 저장할 리스트
# non_soldout_options = []
#
# for option in option_tags:
#     text = option.text  # <option> 태그의 텍스트 내용 가져오기
#     if '품절' not in text:
#         print(text)
#         non_soldout_options.append(text)
#
# print(non_soldout_options)


# # 웹페이지 내용을 가져오기
# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
# html = response.text
#
# # BeautifulSoup을 사용하여 HTML 파싱
# soup = BeautifulSoup(html, 'html.parser')
#
# # 'headquarters--discount' 클래스를 가진 span 태그 찾기
# span_element = soup.find('span', class_='headquarters--discount')
#
# if span_element:
#     # span 태그의 하위 em 태그 찾기
#     em_element = span_element.find('em')
#
#     if em_element:
#         # em 태그 안의 텍스트 추출
#         text_inside_em = em_element.get_text(strip=True)
#         print(text_inside_em)
#     else:
#         print("em 태그를 찾을 수 없습니다.")
# else:
#     print("headquarters--discount 클래스를 가진 span 태그를 찾을 수 없습니다.")
#
# url = url.replace("shop/goodsView", "controller/product/loadOptionDatas")
# # 웹페이지 내용 가져오기
# response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
#
# if response.status_code == 200:
#     data = response.text
#     start_index = data.find("var devOptionData = {")  # devOptionData 객체 시작 위치 찾기
#     if start_index != -1:
#         data = data[start_index:]
#         end_index = data.find("};")  # devOptionData 객체 끝 위치 찾기
#         if end_index != -1:
#             data = data[:end_index + 1]
#
#             # JSON 형식으로 파싱
#             devOptionData = json.loads(data[len("var devOptionData = "):])
#             viewOptions = devOptionData.get("viewOptions", [])
#
#             for option in viewOptions:
#                 if option.get("option_name") == "사이즈":
#                     optionDetailList = option.get("optionDetailList", [])
#                     for detail in optionDetailList:
#                         if detail.get("option_div") == "260":
#                             option_stock = detail.get("option_stock")
#                             if option_stock == 0:
#                                 soldout = "품절"
#                             else:
#                                 soldout = ""
#                             print(f"Option Stock (option_div 220): {option_stock}")
#                             break
#         else:
#             print("devOptionData 객체의 끝을 찾을 수 없습니다.")
#     else:
#         print("devOptionData 객체의 시작을 찾을 수 없습니다.")
# else:
#     print(f"HTTP 요청 오류: {response.status_code}")
