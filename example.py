from bs4 import BeautifulSoup
import requests
from config.config import *
import pandas as pd

url = 'https://poezdato.net/raspisanie-poezdov/borisov--minsk/elektrichki/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, "html.parser")
my_list = []

allHeaders = soup.findAll('tr')
print(allHeaders)
for header in allHeaders:
    news = {
        'Data': header.find('a', href_='/raspisanie-po-stancyi/borisov/').text
        # 'Category': header.find('a', href_="/raspisanie-po-stancyi/minsk/").text,
        # 'Title': header.find('span', class_='_time').text,
        # 'Description': header.find('span', class_='_time').text
    }
    my_list.append(news)

for action in my_list:
    print(action)


