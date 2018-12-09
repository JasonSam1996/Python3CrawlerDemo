# encoding: utf-8
"""
@author: jason_sam
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: SeleniumTaobao.py
@time: 2018/12/2 下午5:37
@desc: Selenium 抓取淘宝ipad信息
"""
import time
import pymongo
from urllib.parse import quote
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq

KEYWORD = 'ipad'
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'ipad_product'

# Selenium初始化
broswer = webdriver.Chrome()
wait = WebDriverWait(broswer, 10)

# mongodb初始化
clent = pymongo.MongoClient(host='localhost', port=27017)
db = clent['taobao']


def index_page(page):
    """
    抓取索引页
    :param page:页码
    :return:
    """
    print("正在爬取第", page, "页")
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        broswer.get(url)
        # 让程序休眠10秒
        broswer.implicitly_wait(10)
        # 休眠10秒，这样操作是为了扫码登录
        time.sleep(10)
        if page > 1:
            broswer.implicitly_wait(5)
            time.sleep(5)
            # 找到输入页数的输入框
            input_et = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            # 找到跳转页数的按钮
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn')))
            input_et.clear()
            input_et.send_keys(page)
            submit.click()

        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        time.sleep(10)
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据
    """
    # 获取网页源代码
    html = broswer.page_source
    # 初始化pq
    doc = pq(html)
    # 获取ipad列表
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        image = item.find('.pic')
        product = {
            # 获取图片
            'image': 'https:' + item.find('.pic .img').attr('data-src'),
            # 价格
            'price': item.find('.price').text(),
            # 销量
            'deal': item.find('.deal-cnt').text(),
            # 标题
            'title': item.find('.title').text(),
            # 店铺
            'shop': item.find('.shop').text(),
            # 店铺位置
            'location': item.find('.location').text(),
        }
        print(product)
        # 休息1秒再保存
        time.sleep(1)
        # 保存到MongoDB
        save_to_mongodb(product)


def save_to_mongodb(product):
    """
    保存到MongoDB
    :param product: 数据
    :return:
    """
    try:
        if db[MONGO_COLLECTION].insert(product):
            print("保存到MongoDB成功")
    except Exception:
        print("保存到MongoDB失败")


MAX_PAGE = 100
if __name__ == '__main__':
    # index_page(2)
    for i in range(1,MAX_PAGE + 1):
        index_page(i)
