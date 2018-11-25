import re

# 匹配结果在字符串结尾，.*?就有可能匹配不到任何内容
content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*?)',content)
result2 = re.match('http.*?comment/(.*)',content)
print('reslut1',result1.group(1))
print('reslut2',result2.group(1))