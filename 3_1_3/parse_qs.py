from urllib.parse import parse_qs

# 反序列化，返回字典
query = 'name=germey&age=22'
print(parse_qs(query))