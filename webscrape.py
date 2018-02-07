import requests
from bs4 import BeautifulSoup
import re
url = "http://www.yoshimoto.co.jp/mugendai/schedule02.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')
schedule_pc = soup.find("div", {"id": "schedule_pc"})
contents = schedule_pc.find_all('ul')

schedule = {}
for content in contents:
    body = str(content)
    timepattern = re.compile('(?<=開演)\d{2}:\d{2}')
    namepattern = re.compile('(?<=公演名</div>\n<div class="schedule_con">)[^<]*')
#    memberpattern = re.compile('(?<=<div class="day_con_name">\n).{10}')
#    day = content.find(id="dayTitle")
#    day = content.find("li", {"id": "dayTitle"})
    time = timepattern.search(body)
    name = namepattern.search(body)
    member = memberpattern.search(body)
#    member = content.find("div", {"class": "day_con_name"})
    schedule['time'] = time.group()
    schedule['name'] = name.group()
#    schedule['member'] = member.group()
#    schedule['member'] = member.string
    with open('regex.text', 'a') as file:
#        file.write(day.string)
        file.write(str(schedule))

    print(schedule)


    with open('regex.text', 'a') as file:
#        file.write(day.string)
        file.write(time.group())
        file.write(name.group())
        file.write(member.string)



    print(time)
    print(name)






topics = bs.select('.fl, .fr')
news_topics = {}
for news in topics:
    topic = news.select('li')[0].text
    news_topics[topic] = [news_topic.text for news_topic in news.select('li')[1:-2]]

with open('fin.text', 'w') as fin:
    fin.write(str(news_topics))
