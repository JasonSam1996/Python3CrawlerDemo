from lxml import etree

html = etree.parse('./test.html',etree.HTMLParser())
# 如果要想获取子孙节点内部的所有文本，可以直接用//加text()的方式，这样可以保证获取到最全面的文本信息，
# 但是可能会夹杂一些换行符等特殊字符
# result = html.xpath('//li[@class="item-0"]//text()')
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)