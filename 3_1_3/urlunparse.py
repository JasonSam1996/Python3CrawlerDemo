from urllib.parse import urlunparse

# 长度必须是6
data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))