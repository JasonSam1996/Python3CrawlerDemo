from urllib.parse import quote

# 将内容转化为URL编码的格式，简称转义
keyword = '壁纸'
url = 'http://www.baidu.com/s?wd=' + quote(keyword)
print(url)
