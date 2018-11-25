from pyquery import PyQuery as pq

html = """
<div class="wrap">
    Hello, World
<p>This is a paragraph.</p>
</div>
"""
# 节点操作
# remove
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())