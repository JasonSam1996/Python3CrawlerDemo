from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
# 获取item-0的两条记录
result = html.xpath('//li[@class="item-0"]')
print(result)