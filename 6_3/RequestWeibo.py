# coding=utf-8
# 获取崔庆才微博前10页微博
import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
db = client['weibo']
collection = db['weibo']

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


# 获取ajax
def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("Error", e.args)


weibolist = []


# 解析Ajax
def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            if item:
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                weibolist.append(weibo)
            else:
                weibo['id'] = 0
                weibo['text'] = '这条记录没有mblog'
                weibo['attitudes'] = ""
                weibo['comments'] = ""
                weibo['reposts'] = ""
                weibolist.append(weibo)
            yield weibo


# 保存到MongoDB
def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')

# 运行脚本
if __name__ == "__main__":
    for page in range(1, 11):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            print(result)
            save_to_mongo(result)
            # print(weib、olist)
