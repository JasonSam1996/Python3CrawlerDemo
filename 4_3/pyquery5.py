from pyquery import PyQuery as pq

html = """
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.htnl"><span>third item</span></a></li>
<li class="item-0 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link4.html">fifth item</a></li>
</ul>
</div>
"""
doc = pq(html)
# 查找节点
# 子节点
items = doc('.list')
print(type(items))
print(items)
# find()的查找范围是节点的所有子孙节点
lis = items.find('li')
print(type(lis))
print(lis)
# 而如果我们只想查找子节点，那么可以用children()的方法，如果想筛选所有子节点中符合条件的节点，可以向children()方法传入CSS选择器
lis = items.children('.active')
print(type(lis))
print(lis)
