from pyquery import PyQuery as pq

# 文件初始化
doc = pq(filename='demo.html')
print(doc('li'))
print(type(doc('li').text()))
