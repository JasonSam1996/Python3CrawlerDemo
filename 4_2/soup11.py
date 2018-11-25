import re
from bs4 import BeautifulSoup

html = """
<div class="panel">
<div class="panel-heading">
<a>Hello, this is a link</a>
<a>Hello, this is a link, too</a>
</div>
</div>
"""
soup = BeautifulSoup(html, 'lxml')
# text参数可用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象
print(soup.find_all(text=re.compile('link')))