import re

# match()方法是从字符串的开头开始匹配的，一旦开头不匹配，那么整个匹配就会失败
# content = 'Extra String Hello 1234567 World_This is a Regex Demo Extra String'
# result = re.match('Hello.*?(\d+).*?Demo$',content)
# print(result)
# search()它在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果
content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐泰">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyord">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>
'''
# 获取active的singer和歌名
result2 = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result2:
    print(result2.group(1), result2.group(2))
# 获取不带active的singer和歌名
result3 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result3:
    print(result3.group(1), result3.group(2))
# 获取不带active的singer和歌名，去掉换行
result4 = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
if result4:
    print(result4.group(1), result4.group(2))
