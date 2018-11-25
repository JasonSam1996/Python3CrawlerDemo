from urllib.parse import parse_qsl

# 将参数转化为元组组成的列表
query = 'name=germey&age=22'
print(parse_qsl(query))
