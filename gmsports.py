import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
import time
import msvcrt


def wait_until(target_time):
    """target_time까지 대기하는 함수"""
    while True:
        now = datetime.now()
        if now >= target_time:
            print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - 예약 시간이 되어 작업을 시작합니다.")
            break
        else:
            # 남은 시간을 초로 계산하여 1초마다 대기
            remaining_time = (target_time - now).total_seconds()
            print(f"남은 시간: {int(remaining_time)}초", end="\r")
            time.sleep(1)


def get_reserve_time():
    """사용자에게 예약 시간을 입력받아 유효한 datetime 객체를 반환하는 함수"""
    while True:
        reserve_time_str = input("예약 시간을 입력하세요 (형식: 2023-12-07 15:30): ")
        try:
            reserve_time = datetime.strptime(reserve_time_str, "%Y-%m-%d %H:%M")
            return reserve_time
        except ValueError:
            print("잘못된 입력입니다. 형식에 맞춰 다시 입력해 주세요.")


court = input("테니스장 번호: ")
id = input("아이디: ")
pw = input("패스워드: ")
date = input("예약날짜 (양식 -> 2023-12-07): ")
clock = input("예약시간 (양식 -> 21:00): ")
name = input("예약자 성명: ")
phone = input("예약자 전화번호: ")
people = input("동반자 수: ")
repeat = int(input("반복 횟수: "))

# 사용자가 입력한 예약 시간을 datetime 형식으로 변환
reserve_time = get_reserve_time()

# 현재 시간과 예약 시간 비교 후 대기
now = datetime.now()
if now < reserve_time:
    print(f"예약 시간이 될 때까지 대기 중... (현재 시간: {now.strftime('%Y-%m-%d %H:%M:%S')})")
    wait_until(reserve_time)
else:
    print("예약 시간이 이미 지났습니다. 즉시 예약을 시도합니다.")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 '
                  'Safari/537.36'
}

main_url = f"https://gmsc9400.mycafe24.com/bbs/board.php?bo_table=booking&office_no={court}"

login_url = "https://gmsc9400.mycafe24.com/bbs/login_check.php"

reserve_url = f"https://gmsc9400.mycafe24.com/bbs/write.php?bo_table=booking&office_no={court}&select={date}"

write_url = "https://gmsc9400.mycafe24.com/bbs/write_update_gmsc.php"

token_url = "https://gmsc9400.mycafe24.com/bbs/write_token.php"

payload_login = {
    'url': f'%2Fbbs%2Fboard.php%3Fbo_table%3Dbooking%26office_no%3D{court}',
    'mb_id': id,
    'mb_password': pw
}

payload_reserve = {
    'bo_table': 'booking',
    'office_no': court,
    'select': date
}

payload_token = {
    'bo_table': 'booking'
}

for i in range(repeat):
    start_time = time.time()

    # 세션 생성 및 POST 요청
    with requests.Session() as session:
        response_main = session.get(main_url, headers=headers)
        soup = BeautifulSoup(response_main.text, 'html.parser')

        response_login = session.post(login_url, headers=headers, data=payload_login)
        soup_2 = BeautifulSoup(response_login.text, 'html.parser')

        response_reserve = session.get(reserve_url, headers=headers, data=payload_reserve)
        soup_3 = BeautifulSoup(response_reserve.text, 'html.parser')

        response_token = session.post(token_url, headers=headers, data=payload_token)
        soup_4 = BeautifulSoup(response_token.text, 'html.parser')

        response_data = json.loads(response_token.text)
        token_value = response_data.get("token")

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y%m%d%H%M%S%f")[:16]

        payload_write = {
            "token": token_value,
            "uid": formatted_time,
            "w": "",
            "wr_id": "0",
            "ca_name": court,
            "bo_table": "booking",
            "select": date,
            "wr_content": f"테니스장 {court}면 예약",
            "wr_1": date,
            "wr_2": clock,
            "od_time": "",
            "wr_4": "관내",
            "wr_name": name,
            "wr_5": people,
            "wr_6": name,
            "wr_subject": phone,
            "agree": "Y",
        }

        response_write = session.post(write_url, headers=headers, data=payload_write)
        soup_5 = BeautifulSoup(response_write.text, 'html.parser')

        if response_write.status_code == 200:
            print("예약에 성공했습니다.")
        else:
            print("예약에 실패했습니다.")

    end_time = time.time() - start_time
    print(f"{end_time}초 걸렸습니다.")

# 아무 키나 누를 때까지 대기
print("예약작업이 종료되었습니다. 아무 키나 누르세요...")
msvcrt.getch()
