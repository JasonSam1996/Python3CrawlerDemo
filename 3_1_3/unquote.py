from urllib.parse import unquote

# 将转义转为中文
url = 'http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))