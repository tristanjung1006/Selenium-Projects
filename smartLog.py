from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyperclip
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# 입력사항(아이디, 비밀번호, 조회기간), 블랙리스트에 추가할 IP를 저정하는 리스트
"""
id = 'akssmd123'
pw = ''
daterange = "2023.07.12 - 2023.07.12"
count_1 = 100
"""
id = input("아이디: ")
pw = input("비밀번호: ")
daterange = input("조회기간(예시-> 2023.07.01 - 2023.07.08): ")
count_1 = int(input("사이트 반복 횟수: "))
ip_building_list = ['서울특별시 중구 을지로65', '해외', '경기도 성남시 분당구 불정로 90', '경기도 성남시 분당구',
                    '서울특별시 용산구 한강대로 32', '서울특별시 마포구 월드컵북로 416']
ip_phone_list = ['k']
ip_list = []
ip_list_2 = []

# 웹브라우저 창 크기 및 웹페이지 요소 로딩 대기시간 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# 스마트로그 사이트 로그인
driver.get('https://smlog.co.kr/2020/member/login.html')
time.sleep(4)
id_input = driver.find_element(By.CSS_SELECTOR, '#id')
pw_input = driver.find_element(By.CSS_SELECTOR, '#password')
id_input.click()
pyperclip.copy(id)
id_input.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
pw_input.click()
pyperclip.copy(pw)
pw_input.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
submit_button = driver.find_element(By.XPATH, f"//div[@class='login-button-01']")
submit_button.click()
time.sleep(4)

for k in range(count_1):
    # 방문자 페이지 접속 후 특정 IP를 블랙리스트에 자동 추가
    ## 조회기간 설정 후 조회하기 버튼 클릭
    ### florutyudpsay.shop
    print("florutyudpsay.shop: 다음 사이트에 대한 부정 IP 차단을 시작하겠습니다.")
    driver.get('https://smlog.co.kr/hmisNew/vsl_visit.html?svid=20995')
    time.sleep(4)
    daterange_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@name='daterange']")))
    daterange_btn.click()
    daterange_btn.send_keys(Keys.CONTROL + "A")
    pyperclip.copy(daterange)
    daterange_btn.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)
    search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@id='search_btn']")))
    search_btn.click()
    time.sleep(2)

    while True:
        try:
            # 현재 페이지에서 IP 개수 COUNT 후, 루프문에서 반복횟수로 사용
            ip_count = driver.find_element(By.XPATH, f"//table[@id='result_data_table']/tbody")
            ip_count_child = ip_count.find_elements(By.XPATH, ".//tr")

            # 확장 버튼 누를시, 명칭이 영구적으로 변화함 (icon-plus ip_extend -> ip_extend icon-plus)
            # icon-plus ip_extend 클래스에 대한 번호(색인)를 부여할 필요가 없다 (한 페이지당 IP 최대 20개)
            for i in range(len(ip_count_child) // 2):
                ## IP 세부사항 열람
                ip_extend_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//i[@class='icon-plus ip_extend']")))
                ip_extend_btn.click()
                time.sleep(5)
                num = 2 * (i + 1)
                driver.switch_to.frame(
                    driver.find_element(By.XPATH, f"//*[@id='result_data_table']/tbody/tr[{num}]/td/div/iframe"))

                ## IP 보유 기관주소, 모바일기기 일치여부 확인 후 블랙리스트 추가 -> 추가된 IP는 리스트에 저장
                ### IP 보유 기관주소 위치는 고정, 모바일기기 위치가 유동적이므로 예외처리
                ip_building = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/p")
                try:
                    ip_phone = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div/div[2]/div/div[2]")
                except NoSuchElementException:
                    print("모바일 기기가 존재하지 않습니다.")
                    ip_phone = None

                if ip_phone is not None:
                    print(ip_building.text + ", " + ip_phone.text)
                    for j in range(len(ip_building_list)):
                        if ip_building.text == ip_building_list[j]:
                            print("부정IP에 해당하는 주소이므로 블랙리스트에 추가합니다.")
                            blacklist = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mci-s-3')))
                            blacklist.click()
                            time.sleep(1)
                            alert = Alert(driver)
                            alert.accept()
                            time.sleep(1)
                            print("부정IP에 해당하는 주소이므로 구글광고노출을 차단합니다.")
                            googleadblock = driver.find_element(By.XPATH, f"//button[@data-ad_click_num='0']")
                            googleadblock.click()
                            time.sleep(1)
                            alert = Alert(driver)
                            alert.accept()
                            ip_address = driver.find_element(By.XPATH, "/html/body/div[1]/h2")
                            ip_list.append(ip_address.text)
                            print("해당IP를 메모장에 추가했습니다.")
                            break
                        elif ip_phone.text == ip_phone_list[0]:
                            print("부정IP에 해당하는 모바일 기기이므로 블랙리스트에 추가합니다.")
                            blacklist = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mci-s-3')))
                            blacklist.click()
                            time.sleep(1)
                            alert = Alert(driver)
                            alert.accept()
                            time.sleep(1)
                            print("부정IP에 해당하는 모바일 기기이므로 구글광고노출을 차단합니다.")
                            googleadblock = driver.find_element(By.XPATH, f"//button[@data-ad_click_num='0']")
                            googleadblock.click()
                            time.sleep(1)
                            alert = Alert(driver)
                            alert.accept()
                            ip_address = driver.find_element(By.XPATH, "/html/body/div[1]/h2")
                            ip_list.append(ip_address.text)
                            print("해당IP를 메모장에 추가했습니다.")
                            break
                        else:
                            continue

                time.sleep(1)
                ## 블랙리스트 추가 작업 이후 IP 세부사항 닫기
                driver.switch_to.default_content()
                ip_close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//i[@class='ip_extend icon-minus']")))
                ip_close_btn.click()
                time.sleep(1)

            # 현재 페이지 위치 특정한 후, 다음 페이지로 넘어가기
            try:
                paging_active = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='paging active']")))
                next_tag = paging_active.find_element(By.XPATH, "following-sibling::a")
                next_tag.click()
                time.sleep(5)
            except TimeoutException:
                print("첫번째 사이트의 첫 페이지입니다.")
                break
        except NoSuchElementException:
            print("첫번째 사이트에서 마지막 페이지입니다.")
            break

    # 리스트에 저장된 IP 중에서 중복값 제거작업
    ip_list_dup = list(set(ip_list))

    # 구글 ads에 추가할 IP 데이터들을 페이지가 넘어가는 주기마다 파일 오픈 후 데이터 추가
    with open('ip_florutyudpsay.txt', 'w') as f:
        for ip in ip_list_dup:
            f.write(f'{ip}\n')

    # 방문자 페이지 접속 후 특정 IP를 블랙리스트에 자동 추가
    ## 조회기간 설정 후 조회하기 버튼 클릭
    ### ticketbuble10.com
    print("ticketbuble10.com: 다음 사이트에 대한 부정 IP 차단을 시작하겠습니다.")
    driver.get('https://smlog.co.kr/hmisNew/vsl_visit.html?svid=21073')
    time.sleep(4)
    daterange_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@name='daterange']")))
    daterange_btn.click()
    daterange_btn.send_keys(Keys.CONTROL + "A")
    pyperclip.copy(daterange)
    daterange_btn.send_keys(Keys.CONTROL, 'v')
    time.sleep(1)
    search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@id='search_btn']")))
    search_btn.click()
    time.sleep(2)

    while True:
        try:
            # 현재 페이지에서 IP 개수 COUNT 후, 루프문에서 반복횟수로 사용
            ip_count = driver.find_element(By.XPATH, f"//table[@id='result_data_table']/tbody")
            ip_count_child = ip_count.find_elements(By.XPATH, ".//tr")

            # 확장 버튼 누를시, 명칭이 영구적으로 변화함 (icon-plus ip_extend -> ip_extend icon-plus)
            # icon-plus ip_extend 클래스에 대한 번호(색인)를 부여할 필요가 없다 (한 페이지당 IP 최대 20개)
            for i in range(len(ip_count_child) // 2):
                ## IP 세부사항 열람
                ip_extend_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//i[@class='icon-plus ip_extend']")))
                ip_extend_btn.click()
                time.sleep(5)
                num = 2 * (i + 1)
                driver.switch_to.frame(
                    driver.find_element(By.XPATH, f"//*[@id='result_data_table']/tbody/tr[{num}]/td/div/iframe"))

                ## IP 보유 기관주소, 모바일기기 일치여부 확인 후 블랙리스트 추가 -> 추가된 IP는 리스트에 저장
                ### IP 보유 기관주소 위치는 고정, 모바일기기 위치가 유동적이므로 예외처리
                ip_building = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/p")
                try:
                    ip_phone = driver.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div/div[2]/div/div[2]")
                except NoSuchElementException:
                    ip_phone = None

                if ip_phone is not None:
                    print(ip_building.text + ", " + ip_phone.text)
                    for j in range(len(ip_building_list)):
                        if ip_building.text == ip_building_list[j]:
                            print("부정IP에 해당하는 주소이므로 블랙리스트에 추가합니다.")
                            blacklist = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mci-s-3')))
                            blacklist.click()
                            time.sleep(1)
                            alert = Alert(driver)
                            alert.accept()
                            time.sleep(1)
                            print("부정IP에 해당하는 주소이므로 구글광고노출을 차단합니다.")
                            googleadblock = driver.find_element(By.XPATH, f"//button[@data-ad_click_num='0']")
                            googleadblock.click()
                            time.sleep(1)
                            alert = Alert(driver)
                            alert.accept()
                            ip_address = driver.find_element(By.XPATH, "/html/body/div[1]/h2")
                            ip_list_2.append(ip_address.text)
                            print("해당IP를 메모장에 추가했습니다.")
                            break
                        elif ip_phone.text == ip_phone_list[0]:
                            print("부정IP에 해당하는 모바일 기기이므로 블랙리스트에 추가합니다.")
                            blacklist = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mci-s-3')))
                            blacklist.click()
                            time.sleep(1)
                            alert = Alert(driver)
                            alert.accept()
                            time.sleep(1)
                            print("부정IP에 해당하는 모바일 기기이므로 구글광고노출을 차단합니다.")
                            googleadblock = driver.find_element(By.XPATH, f"//button[@data-ad_click_num='0']")
                            googleadblock.click()
                            time.sleep(1)
                            alert = Alert(driver)
                            alert.accept()
                            ip_address = driver.find_element(By.XPATH, "/html/body/div[1]/h2")
                            ip_list_2.append(ip_address.text)
                            print("해당IP를 메모장에 추가했습니다.")
                            break
                        else:
                            continue

                time.sleep(1)
                ## 블랙리스트 추가 작업 이후 IP 세부사항 닫기
                driver.switch_to.default_content()
                ip_close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, f"//i[@class='ip_extend icon-minus']")))
                ip_close_btn.click()
                time.sleep(1)

                # 현재 페이지 위치 특정한 후, 다음 페이지로 넘어가기
            try:
                paging_active = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='paging active']")))
                next_tag = paging_active.find_element(By.XPATH, "following-sibling::a")
                next_tag.click()
                time.sleep(5)
            except TimeoutException:
                print("두번째 사이트의 첫 페이지입니다.")
                break
        except NoSuchElementException:
            print("두번째 사이트에서 마지막 페이지입니다.")
            break

    # 리스트에 저장된 IP 중에서 중복값 제거작업
    ip_list_2_dup = list(set(ip_list_2))

    # 구글 ads에 추가할 IP 데이터들을 페이지가 넘어가는 주기마다 파일 오픈 후 데이터 추가
    with open('ip_ticketbuble10.txt', 'w') as f:
        for ip in ip_list_2_dup:
            f.write(f'{ip}\n')

driver.quit()
