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
</p>
<p class="story">...</p>
"""
# 抓取父节点
soup = BeautifulSoup(html, 'lxml')
print(soup.a.parent)
print(soup.a.parents)
for i, child in enumerate(soup.a.parents):
    print(i, child)