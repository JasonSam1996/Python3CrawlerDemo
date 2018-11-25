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
# 基本CSS选择器
print(doc('#container .list li'))
print(type(doc('#container .list li')))