import requests
from bs4 import BeautifulSoup
import nltk as nltk

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

lowered_word_token_Full = []

for i in word_token_Full:
    lowered_word_token_Full.append(i.lower())
    
print(lowered_word_token_Full)

tagged_lowered_word_token_Full = nltk.pos_tag(lowered_word_token_Full)

print(tagged_lowered_word_token_Full)

Noun_words = []
for word, pos in tagged_lowered_word_token_Full:
    if 'NN' in pos:
        Noun_words.append(word)
print(Noun_words)

wlem = nltk.WordNetLemmatizer()
lemmatized_words = []
for word in Noun_words:
    new_word = wlem.lemmatize(word)
    lemmatized_words.append(new_word)

print(lemmatized_words)

from collections import Counter
c = Counter(lemmatized_words) # input type should be a list of words (or tokens)
print(c)
k = 20
print(c.most_common(k)) # 빈도수 기준 상위 k개 단어 출력

import wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from os import path


noun_text = ''
for word in lemmatized_words:
    noun_text = noun_text +' '+word

wordcloud = WordCloud(max_font_size=60, relative_scaling=.5, background_color='white').generate(noun_text)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()