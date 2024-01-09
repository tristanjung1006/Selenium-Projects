import time
import requests
from bs4 import BeautifulSoup

# URL들
login_action_url = 'https://share.gg.go.kr/member/loginAction'

start_time = time.time()
# 세션 생성
with requests.Session() as session:

    # 페이로드
    payload = {
        'referer': 'https://share.gg.go.kr/index',
        'captChaPass': 'Y',
        'mberIdChk': 'tristan1006@naver.com',
        'passwordChk': 'seungwon3079!',
    }

    # 로그인 체크를 위한 POST 요청
    login_check_response = session.post(login_action_url, data=payload)
    print(session.cookies)
    print(login_check_response.text)

    # 로그인 체크 응답 확인
    if login_check_response.status_code == 200:
        print("로그인 성공")
    else:
        print('로그인 체크 요청 실패:', login_check_response.status_code)

    # 이후 작업 수행...
    end_time = time.time() - start_time
    print(end_time)
