from bs4 import BeautifulSoup

html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-smail" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""
soup = BeautifulSoup(html,'lxml')
# find_all取包含元素的所有元素
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')))
# 取li 所有元素
for ul in soup.find_all(name='ul'):
    print(ul.find_all('li'))
# 取li元素的值
for ul in soup.find_all(name='ul'):
    print(ul.find_all('li'))
    for li in ul.find_all(name='li'):
        print(li.string)