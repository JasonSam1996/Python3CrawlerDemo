import re

content = '''Hello 123 4567 World_This 
is a Regex Demo
'''
# re.S 使.匹配包括换行的所有字符，re.I匹配大小写不敏感
result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))
