from pyquery import PyQuery as pq

html = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.htnl"><span>third item</span></a></li>
<li class="item-0 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link4.html">fifth item</a></li>
</ul>
</div>
</div>
"""
doc = pq(html)
# 查找节点
# 父节点
items = doc('.list')
# 直接查找父节点，不会查找祖先节点
container = items.parent()
print(type(container))
print(container)
# 查找祖先节点，输出结果有两个，一个是class为wrap的几点，一个是ID为contains的几点，也就是说
# parents()方法会返回所有的祖先节点
parents = items.parents()
print(type(parents))
print(parents)
# 如果想要筛选某个祖先节点的话，可以向parents()方法传入CSS选择器
parents = items.parents('.wrap')
print(type(parents))
print(parents)