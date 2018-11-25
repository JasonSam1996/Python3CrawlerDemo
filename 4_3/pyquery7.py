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
doc = pq(html)
# 查找节点
# 兄弟节点
li = doc('.list .item-0.active')
print(li.siblings())
# 如果筛选某个兄弟节点,我们依然可以向siblings方法传入css选择器
li = doc('.list .item-0.active')
print(li.siblings('.active'))