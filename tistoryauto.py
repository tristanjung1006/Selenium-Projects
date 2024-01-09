import requests
import time
from bs4 import BeautifulSoup, NavigableString, Tag

access_token = '39d6c12381ee410d111c8b71b6ba4ade_33877198f12435820f1db8cf46b27317'
output_type = 'json'
blogName = "infomationpit"
title = "건우"
content = "안녕하세요 글 테스트중입니다."
visibility = 0
category_id = 0
published = time.time()

url = f"https://www.tistory.com/apis/post/write?access_token={access_token}&output={output_type}&blogName={blogName}&title={title}&content={content}&visibility={visibility}&category={category_id}&published={published}"


requests.post(url)

# # URL
# search_url = 'https://namu.wiki/w/줄리어스%20로버트%20오펜하이머'
#
# # Create a session
# with requests.Session() as session:
#     # Send a GET request to the search URL
#     search_url_res = session.get(search_url)
#
#     # Check if the request was successful
#     if search_url_res.status_code == 200:
#         # Parse the HTML content using BeautifulSoup
#         soup = BeautifulSoup(search_url_res.text, 'html.parser')
#
#         paragraph_texts = []
#         current_paragraph = []
#
#         # Iterate over every element in the parsed HTML
#         for tag in soup.recursiveChildGenerator():
#             if isinstance(tag, NavigableString):
#                 current_paragraph.append(tag.strip())
#             elif isinstance(tag, Tag) and current_paragraph:
#                 # Join the current paragraph texts and add to the list
#                 paragraph_texts.append(' '.join(current_paragraph))
#                 current_paragraph = []
#
#         # Print the extracted paragraphs
#         for paragraph in paragraph_texts:
#             if paragraph:  # Skip empty paragraphs
#                 print(paragraph)
#     else:
#         print(f"Failed to fetch the URL. Status code: {search_url_res.status_code}")

