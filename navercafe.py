import requests
from bs4 import BeautifulSoup

# 검색어 설정
query = "한우"

# 해당 사이트의 검색 URL 구조에 따라 URL을 조절해야 합니다.
# 아래의 URL은 예시로 제공된 것이므로 실제 사이트의 검색 URL 구조에 맞게 수정해야 합니다.
url = f"https://cafe.naver.com/hotellife/search?q={query}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

# Naver 카페는 대부분의 내용이 iframe으로 되어 있기 때문에 추가적인 처리가 필요합니다.
soup = BeautifulSoup(response.text, 'html.parser')
iframe_url = soup.find('iframe')['src']
response = requests.get(f"https://cafe.naver.com{iframe_url}", headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 게시물 제목 및 링크 추출 (이 부분은 사이트의 구조에 따라 수정해야 함)
posts = soup.find_all('a', class_='search_article_subject')

for post in posts:
    title = post.text.strip()
    link = post['href']
    print(title, link)
