import requests


def send_telegram_message(token, chat_id, message):
    base_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(base_url)
    return response.json()


# replace with your bot token and chat ID
token = "6375642379:AAGLNSvdE17QCrFnATnvmCq5Qx6tA5Jc3VM"
chat_id = "6324662357"
message = "Hello, this is a test message!"

response = send_telegram_message(token, chat_id, message)
print(response)
