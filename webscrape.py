import requests
from bs4 import BeautifulSoup
url = "http://www.yoshimoto.co.jp/mugendai/schedule02.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
with open('schedule.text', 'w') as file:
    file.write(soup.text)

soup = BeautifulSoup(response.content, 'html.parser')
    bs = BeautifulSoup(response.text, "lxml")
bs = BeautifulSoup(response.text, "lxml")
topics = bs.select('.fl, .fr')
news_topics = {}
for news in topics:
    topic = news.select('li')[0].text
    news_topics[topic] = [news_topic.text for news_topic in news.select('li')[1:-2]]

with open('fin.text', 'w') as fin:
    fin.write(str(news_topics))
