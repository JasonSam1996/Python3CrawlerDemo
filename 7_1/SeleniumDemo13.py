# encoding: utf-8
"""
@author: jason_sam
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: SeleniumDemo13.py
@time: 2018/11/25 下午10:58
@desc: Selenium 选项卡管理，窗口管理
"""
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com/')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org/')