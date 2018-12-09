# encoding: utf-8
"""
@author: jason_sam
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: execute.py
@time: 2018/12/2 下午5:01
@desc: Splash Api调用，execute
"""
import requests
from urllib.parse import quote

lua_source = """
function main(splash)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
    return {
        html=treat.as_string(response.body),
        url=response.url,
        status=response.status
    }
end
"""

url = "http://localhost:8050/execute?lua_source="+quote(lua_source)
print(url)
response = requests.get(url)
print(response.text)