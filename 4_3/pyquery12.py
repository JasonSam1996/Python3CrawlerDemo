from pyquery import PyQuery as pq

html = """
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span>third item</span></a></li>
"""
doc = pq(html)
# 节点操作
# attr、text和html
li = doc('.item-0.active')
print(li)
# attr 修改属性
li.attr('name','link')
print(li)
# text 修改文本,如果不传值就是取值
li.text('changed item')
print(li)
# html 修改元素,如果不传值就是取值
li.html('<span>6666</span>')
print(li)