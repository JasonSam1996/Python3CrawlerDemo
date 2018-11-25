from lxml import etree

# 节点轴选择
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
# 选择所有祖先节点
result = html.xpath('//li[1]/ancestor::*')
print(result)
# 选择div
result = html.xpath('//li[1]/ancestor::div')
print(result)
# 选择所有的属性值
result = html.xpath('//li[1]/attribute::*')
print(result)
# 获取所有子节点
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
# 获取所有子孙节点,加了限定条件获取span节点,所有返回的结果只包含span节点而不包含a节点
result = html.xpath('//li[1]/descendant::span')
print(result)
# 获取当前节点之后的所有节点
result = html.xpath('//li[1]/following::*[2]')
print(result)
# 获取当前节点之后的所有同级节点
result = html.xpath('//li[1]/following-sibling::*')
print(result)



