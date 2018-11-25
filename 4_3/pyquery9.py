from pyquery import PyQuery as pq

html = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span>third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
"""
doc = pq(html)
# 获取信息
# 获取属性，可以调用attr方法俩获取属性
a = doc('.item-0.active a')
print(a, type(a))
# print(a.attr('href'))
# 第二种方法
# print(a.attr.href)
# 多个元素，调用attr方法，只会返回第一个元素
a = doc('a')
# print(a.attr('href'))
# print(a.attr.href)
# 想获取所有的a节点的属性，可以用遍历方法
for item in a.items():
    print(item.attr('href'))
