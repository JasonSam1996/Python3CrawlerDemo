import re

# 匹配目标
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld',content)
# 通用匹配
result2 = re.match('^Hello.*Demo$',content)
# 贪婪与非贪婪，贪婪匹配是尽可能匹配多的字符
result3 = re.match('^Hello.*(\d+).*Demo$',content)
# 贪婪与非贪婪，非贪婪匹配是尽可能匹配少的字符
result4 = re.match('^Hello.*?(\d+).*Demo$',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())
print(result2)
print(result2.group())
print(result2.span())
print(result3)
print(result3.group(1))
print(result4)
print(result4.group(1))
