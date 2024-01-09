import time
import requests
from bs4 import BeautifulSoup

# URL들
login_sso_url = 'https://reserv.bucheon.go.kr/SSOService.do'
login_link_url = 'https://sso.bucheon.go.kr/sso/usr/login/link'

start_time = time.time()
# 세션 생성
with requests.Session() as session:
    # 로그인 페이지에 GET 요청
    login_sso_response = session.get(login_sso_url)

    # BeautifulSoup으로 HTML 분석
    soup = BeautifulSoup(login_sso_response.text, 'html.parser')
    print(session.cookies)
    print(login_sso_response.text)

    # agt_r 값 추출 (HTML 구조에 따라 적절하게 수정)
    agt_r = soup.find('input', {'name': 'agt_r'})['value']
    print(agt_r)

    payload = {
        'agt_id': 'bucheon-trserv',
        'agt_url': 'https://reserv.bucheon.go.kr',
        'agt_r': agt_r,
        'returl': 'https://reserv.bucheon.go.kr/site/main/reservLoginProc',
        'failurl': 'https://reserv.bucheon.go.kr/site/main/login'
    }
    login_link_response = session.post(login_link_url, data=payload)
    print(login_link_response.text)

    # 로그인 체크 응답 확인
    if login_link_response.status_code == 200:
        print("로그인 성공")
    else:
        print('로그인 체크 요청 실패:', login_link_response.status_code)

    # 이후 작업 수행...
    end_time = time.time() - start_time
    print(end_time)

