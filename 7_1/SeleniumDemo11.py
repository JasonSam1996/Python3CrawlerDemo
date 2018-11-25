# encoding: utf-8
"""
@author: jason_sam
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: SeleniumDemo11.py
@time: 2018/11/25 下午10:52
@desc: Selenium 前进和后退
"""

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
# 后退
browser.back()
time.sleep(1)
# 前进
browser.forward()
browser.close()