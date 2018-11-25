from bs4 import BeautifulSoup

# 节点选择器
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's storty</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)
# 提取信息，获取名称
print(soup.title.name)
# 获取属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
# 简洁写法
print(soup.p['name'])
# 一个元素可能有多个class，所以返回的是列表
print(soup.p['class'])
# 获取内容
print(soup.p.string)