import requests
from bs4 import BeautifulSoup

# header ={"user-agent": "Mozilla/5.0"}
# url = "https://abcnews.go.com/International"
# r = requests.get(url, headers=header)
# bs = BeautifulSoup(r.text, "lxml")
# links = bs.select("div.ContentList__Item > a")
# for l in links:
#     print(l.get("href"))
#     bs = BeautifulSoup(r.text, "lxml")
#     contents = bs.select_one("span.oyrP qlwa AGxe")
#     print(contents.text)

url = "https://www.bbc.com/sport/live/football/67700632"
res = requests.get(url)
bs = BeautifulSoup(res.content, "html.parser")

result = bs.find('div', class_='lx-c-sticky')
for tag in result.find_all('li'):
    # print(tag.text)


