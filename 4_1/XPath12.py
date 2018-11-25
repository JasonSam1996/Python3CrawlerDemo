from lxml import etree

# 属性多值匹配,需要用哪个contains()函数了
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
# 这样通过contains()方法，第一个参数传入属性名称，第二个参数传入属性值，只要此属性包含所出传入的属性值，就可以完成匹配了
result = html.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
