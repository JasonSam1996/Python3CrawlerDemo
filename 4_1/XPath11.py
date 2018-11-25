from lxml import etree

# 属性获取，获取a元素里的href属性
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
