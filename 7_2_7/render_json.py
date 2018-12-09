# encoding: utf-8
"""
@author: jason_sam
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: render_json.py
@time: 2018/12/2 下午4:57
@desc: Splash Api调用，render.json
"""
import requests

url = "http://localhost:8050/render.json?url=https://httpbin.org"
response = requests.get(url)
print(response.json())