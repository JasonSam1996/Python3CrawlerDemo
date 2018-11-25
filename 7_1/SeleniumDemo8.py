# encoding: utf-8
"""
@author: jason_sam
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: SeleniumDemo8.py
@time: 2018/11/25 下午10:25
@desc: Selenium 获取节点信息
"""

from selenium import webdriver

"""
获取属性
"""
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))
"""
获取文本
"""
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)
"""
获取ID、位置、标签名和大小
"""
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)