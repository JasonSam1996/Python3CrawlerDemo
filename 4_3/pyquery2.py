import requests
from pyquery import PyQuery as pq

# URL初始化
doc = pq(url='https://cuiqingcai.com')
print(doc('title'))
# 下面的功能相同的
doc = pq(requests.get('https://cuiqingcai.com').text)
print(doc('title'))
