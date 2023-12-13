from math import trunc
import requests
from bs4 import BeautifulSoup
import re
import os
import json
import random


from requests.api import get

url = input('url을 넣어주세요')
r = requests.get(url)
bs = BeautifulSoup(r.text, 'lxml')
lists = bs.select(".gnt_m_th_a")

def get_News():
    for li in lists:
        href = url+li["href"]
        r = requests.get(href)
        bs = BeautifulSoup(r.text, 'lxml')
        texts = bs.select("div.gnt_ar_b >  p.gnt_ar_b_p")
        
        contents = [p.text for p in texts]
        contents = " ".join(contents)
        return contents.lower()
    return None

print(contents)