import requests
import json
from pyquery import PyQuery as pq

# 文件存储
# json存储
# 抓取知乎发现-热门话题
url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:63.0) Gecko/20100101 Firefox/63.0'
}
result = []
# 用Requests将网页源代码获取下来
html = requests.get(url, headers=headers).text
# 利用pyquery进行网页解析
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    result_dict = {
        "question": question,
        "author": author,
        "answer": answer
    }
    result.append(result_dict)
    with open('data.json', 'w', encoding='utf-8') as file:
        # indent 缩进字符个数
        file.write(json.dumps(result, indent=4, ensure_ascii=False))

print(result)
