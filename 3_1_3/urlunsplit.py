from urllib.parse import urlunsplit

# urlunsplit必须长度为5，因为split缺少parse
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
