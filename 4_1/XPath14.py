from lxml import etree

# 按序选择
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
# 获取第一个节点，顺序是从1开始，不是从0开始
result = html.xpath('//li[1]/a/text()')
print(result)
# 获取最后一个节点
result = html.xpath('//li[last()]/a/text()')
print(result)
# 获取位置小于3的节点
result = html.xpath('//li[position()<3]/a/text()')
print(result)
# 获取倒数第三个节点
result = html.xpath('//li[last()-2]/a/text()')
print(result)