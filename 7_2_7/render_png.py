# encoding: utf-8
"""
@author: jason_sam
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: render_png.py
@time: 2018/12/2 下午4:51
@desc: Splash Api调用，render.png
"""
import requests

url = "http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700"
response = requests.get(url)
with open('jd.png', 'wb') as f:
    f.write(response.content)
