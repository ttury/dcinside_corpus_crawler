import requests
from urllib import request
from bs4 import BeautifulSoup
import time

BASE_URL = "https://gall.dcinside.com/board/lists"
ARTICLE_BASE_URL = "https://gall.dcinside.com"
BASE_URL_MOBILE = "https://m.dcinside.com/board/maplestory/"

# 헤더 설정
headers = {
    "User-Agent" : "Monika (Android; Hello_world)",
    }

#몇 페이지부터 몇 페이지까지
for i in range(1, 10):
    # 파라미터 설정
    params = {'id': 'maplestory','page':i}
    # response = requests.get(BASE_URL, params=params, headers=headers)
    response = requests.get(BASE_URL_MOBILE, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    #실질적 글 목록 부분
    article_list = soup.find('tbody').find_all('tr')
    # 한 페이지에 있는 모든 게시물을 긁어오는 코드
    for tr_item in article_list:
        print('+'*12)
        # 제목 추출
        title_tag = tr_item.find('a', href=True)
        title = title_tag.text
        print("제목: ", title)
        print("주소: ", title_tag['href'])
        # article_response = requests.get(ARTICLE_BASE_URL + title_tag['href'], headers=headers)


