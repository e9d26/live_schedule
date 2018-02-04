import requests
from bs4 import BeautifulSoup
import re
url = "http://www.yoshimoto.co.jp/mugendai/schedule02.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
schedule_pc = soup.find("div", {"id": "schedule_pc"})
contents = schedule_pc.find_all('ul')
for content in contents:
    time = content.find(re.compile("\d"))
    with open('test.text', 'a') as file:
        file.write(str(time))

schedule = {}


topics = bs.select('.fl, .fr')
news_topics = {}
for news in topics:
    topic = news.select('li')[0].text
    news_topics[topic] = [news_topic.text for news_topic in news.select('li')[1:-2]]

with open('fin.text', 'w') as fin:
    fin.write(str(news_topics))
