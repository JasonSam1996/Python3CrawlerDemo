from pyquery import PyQuery as pq

html = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.htnl"><span>third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link4.html">fifth item</a></li>
</ul>
</div>
</div>
"""
# 查找节点
# 获取文本
doc = pq(html)
a = doc('.item-0.active')
print(a)
print(a.text())
# 获取HTML使用html()方法
print(a.html())
# 多个元素，text()和html()区别，html返回第一个内部HTML文本，text返回所有li内部的文本，如想获取多个HTML文本，则需要使用遍历方法
li = doc('li')
print(li.html())
print(li.text())
print(type(li.text()))
