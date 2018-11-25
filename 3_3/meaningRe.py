import re

# 转义匹配
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com',content)
print(result)
