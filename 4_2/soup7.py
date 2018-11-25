from bs4 import BeautifulSoup

html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>	
</a>
    Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
and
<a href="http://example.com/tillie" class="sister" id="link2">Tillie</a>
and they lived at the bottom of a well.
</p>
"""
soup = BeautifulSoup(html, 'lxml')
# 抓取兄弟节点
# 获取下一个的兄弟节点
print("Next Sibling:", soup.a.next_sibling)
# 抓取上一个的兄弟节点
print("Prev Sibling:", soup.a.previous_sibling)
# 抓取下一个的所有兄弟节点
print("Next Siblings:",list(enumerate(soup.a.next_siblings)))
# 抓取上一个的所有兄弟节点
print("Prev Siblings:",list(enumerate(soup.a.previous_siblings)))
