import requests
from bs4 import BeautifulSoup
import nltk as nltk


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
sentenceList = []

result = bs.find('div', class_='lx-c-sticky')
for tag in result.find_all('li'):
    # print(tag.text)
    sentenceList.append(tag.text)
    

# text = "Hello my name is Choi. Nice to you. How are you? I'm fine. Thank you for asking me."

joined_sentenceList = '.'.join(sentenceList)

print(joined_sentenceList)
print(type(joined_sentenceList))

word_token_Full = nltk.word_tokenize(joined_sentenceList)
print(type(word_token_Full))
print(word_token_Full)
