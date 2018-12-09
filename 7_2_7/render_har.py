# encoding: utf-8
"""
@author: jason_sam
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: render_har.py
@time: 2018/12/2 下午4:55
@desc: Splash Api调用，render.har
"""
import requests

url = "http://localhost:8050/render.har?url=https://www.jd.com&wait=5"
response = requests.get(url)
print(response.text)
