import time

import requests
from bs4 import BeautifulSoup

# URL들
login_page_url = 'https://www.s-parkresort.co.kr/Member/Login'
login_check_url = 'https://www.s-parkresort.co.kr/Member/Logincheck'
login_url = 'https://www.s-parkresort.co.kr/Member/Login'
reserve_url = 'https://www.s-parkresort.co.kr/Reservation/ReservCalendar'
timelist_url = 'https://www.s-parkresort.co.kr/Reservation/AjaxTimeListDataSet'
calendar_url = 'https://www.s-parkresort.co.kr/Reservation/AjaxCalendarDataSet'
ajax_check_url = 'https://www.s-parkresort.co.kr/Reservation/AjaxReservCheck'
ajax_ok_url = 'https://www.s-parkresort.co.kr/Reservation/AjaxReservOK'

# 헤더들
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36',
    'Referer': login_page_url,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    # 'Cookie': '이곳에 쿠키를 입력하세요',
}

start_time = time.time()
# 세션 생성
with requests.Session() as session:
    # 로그인 페이지에 GET 요청
    login_page_response = session.get(login_page_url)

    # BeautifulSoup으로 HTML 분석
    soup = BeautifulSoup(login_page_response.text, 'html.parser')

    # 토큰 값 추출 (HTML 구조에 따라 적절하게 수정)
    token_value = soup.find('input', {'name': '__RequestVerificationToken'})['value']
    print(token_value)

    # 페이로드
    payload = {
        '__RequestVerificationToken': token_value,
        'user_id': 'tristan10062',
        'user_pwd': 'seungwon3079!',
    }

    # 로그인 체크를 위한 POST 요청
    login_check_response = session.post(login_check_url, data=payload)
    print(session.cookies)
    print(login_check_response.text)

    # 로그인 체크 응답 확인
    if login_check_response.status_code == 200:
        # 결과 획득
        result = login_check_response.json()

        # 결과 코드 확인
        if result['code'] == 0 or result['code'] == 200:
            # 로그인을 위한 POST 요청
            login_response = session.post(login_url, data=payload)
            # BeautifulSoup으로 HTML 분석
            soup = BeautifulSoup(login_response.text, 'html.parser')
            print(soup)

            # 로그인 응답 확인
            if login_response.status_code == 200:
                print('로그인 성공!')
                # 로그인 페이지에서 달력 페이지로 넘어가기 위한 GET 요청
                reserve_response = session.get(reserve_url)

                # BeautifulSoup으로 HTML 분석
                soup = BeautifulSoup(reserve_response.text, 'html.parser')

                # 달력 페이지에서 토큰 값 추출 (bookingForm태그에서 토큰 값 추출)
                token_value = soup.find('input', {'name': '__RequestVerificationToken'})['value']
                print(token_value)

                # 추출한 토큰 값을 기입한 후, AjaxReservCheck 패킷에 페이로드 값 넣기
                payload = {
                    '__RequestVerificationToken': token_value,
                    'rsv_date': '20230916',
                    'rsv_seq': '00108',
                    'daegiDate': '20230916',
                }

                timelist = {
                    'date': '20230915'
                }

                calendarlist = {
                    'day': '20230915',
                    'type': 'today'
                }

                # AjaxTimeListDataSet, AjaxCalendarDataSet 패킷 post 요청
                ajax_timelist_response = session.post(timelist_url, data=timelist)
                print(ajax_timelist_response.text)
                ajax_calendar_response = session.post(calendar_url, data=calendarlist)
                print(ajax_calendar_response.text)

                # AjaxReservCheck 패킷 post 요청(예약버튼 클릭세션)
                ajax_check_response = session.post(ajax_check_url, data=payload)
                soup = BeautifulSoup(ajax_check_response.text, 'html.parser')
                print(session.cookies)
                print(ajax_check_response.text)

                # Ajax 테스트 get 요청
                # ajax_check_response = session.get(ajax_check_url)
                # soup = BeautifulSoup(ajax_check_response.text, 'html.parser')
                # print(session.cookies)
                # print(ajax_check_response.text)

                if ajax_check_response.status_code == 200:
                    print("접속 성공!")

                    # 달력 페이지에서
                    soup = BeautifulSoup(reserve_response.text, 'html.parser')

                    # 달력 페이지에서 토큰 값 추출 (reservation_form태그에서 토큰 값 추출)
                    token_value = soup.find('input', {'name': '__RequestVerificationToken'})['value']
                    print(token_value)

                    payload = {
                        '__RequestVerificationToken': token_value,
                        'lgubun': '160',
                        'rsv_date': '20230916',
                        'rsv_seq': '00108'
                    }
                    # ajax_ok_response -> ok팝업창 등장 후에 페이지 요소로 다시 접근하는 방법 필요
                    ajax_ok_response = session.post(ajax_ok_url, data=payload)
                    if ajax_ok_response.status_code == 200:
                        print("예약 성공!")
                else:
                    print("실패...")
            else:
                print('로그인 실패:', login_response.status_code)
        else:
            print('로그인 체크 실패:', result['msg'])
    else:
        print('로그인 체크 요청 실패:', login_check_response.status_code)

    # 이후 작업 수행...
    end_time = time.time() - start_time
    print(end_time)
