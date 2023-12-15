import requests
from bs4 import BeautifulSoup
import nltk as nltk

url = "https://www.bbc.com/sport/live/football/67700632"
res = requests.get(url)
bs = BeautifulSoup(res.content, "html.parser")
sentenceList = []

result = bs.find('div', class_='lx-c-sticky')
for tag in result.find_all('li'):
    sentenceList.append(tag.text)

joined_sentenceList = '.'.join(sentenceList)

#print(joined_sentenceList)
#print(type(joined_sentenceList))

word_token_Full = nltk.word_tokenize(joined_sentenceList)
#print(type(word_token_Full))
#print(word_token_Full)

lowered_word_token_Full = []

for i in word_token_Full:
    lowered_word_token_Full.append(i.lower())
    
#print(lowered_word_token_Full)

tagged_lowered_word_token_Full = nltk.pos_tag(lowered_word_token_Full)

#print(tagged_lowered_word_token_Full)

Noun_words = []
for word, pos in tagged_lowered_word_token_Full:
    if 'NN' in pos:
        Noun_words.append(word)
#print(Noun_words)

wlem = nltk.WordNetLemmatizer()
lemmatized_words = []
for word in Noun_words:
    new_word = wlem.lemmatize(word)
    lemmatized_words.append(new_word)

#print(lemmatized_words)

from collections import Counter
c = Counter(lemmatized_words)
#print(c)
k = 20
#print(c.most_common(k))


print(Noun_words)

considerable_words = []

count_of_blanks = int(input("몇개의 빈칸으로 이루어져 있나요?"))

for word in Noun_words:
     if len(word) == count_of_blanks:
         considerable_words.append(word)
         
         
print(considerable_words)




# 대충 직접 컴퓨터가 맞추는형태가 아니라 우리가 행맨게임을 가장 빠르게 우승하도록 도와주는 코드
# 단어들 중에서 5개의 빈칸이다
# 어느자리에 어떠한 단어가 들어간다로 실행과 구성