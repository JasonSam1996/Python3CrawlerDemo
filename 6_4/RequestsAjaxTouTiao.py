# encoding: utf-8
"""
@author: jason_sam
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: RequestsAjaxTouTiao.py
@time: 2018/11/25 下午3:11
@desc: 分析Ajax爬取今日头条街拍美图，实战演练
"""
import os
import requests
from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool


# 加载单个Ajax请求的json结果
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',
        'from': 'gallery',
        'pd': ''
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


# 提取每条数据的image_detail字段中的每一张图片链接和标题，并构造一个生成器
def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            if images:
                for image in images:
                    image_url = "https:" + image.get('url')
                    # print("image_url:", image_url)
                    yield {
                        'image': image_url,
                        'title': title
                    }


# 保存图片，在该方法中，首先根据item的title来创建文件夹，然后请求这个图片链接，获取图片的二进制数据，以二进制的形式写入文件
def save_image(item):
    if not os.path.exists("头条爬取街拍图片/"+item.get("title")):
        os.makedirs("头条爬取街拍图片/"+item.get("title"))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format("头条爬取街拍图片/"+item.get("title"), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print("Already Downloaded", file_path)
    except requests.ConnectionError:
        print("Failed to import Pool")


def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)


GROUP_START = 0
GROUP_END = 20

if __name__ == '__main__':
    # 多进程下载图片并保存
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    print(groups)
    pool.map(main, groups)
    pool.close()
    pool.join()
