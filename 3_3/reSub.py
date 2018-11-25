import re

# 除了使用正则表达式提取信息外，有时候还需要借助它来修改文本。比如，想要把一串文本中的所有数字去掉，如果使用字符串replace会很烦琐，这时可以借助sub()方法
content = '54ak54yr5oiR54ix5L2g'
result = re.sub('\d+',"",content)
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
results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
for result in results:
    print(result[1])
# 借助sub方法方便很多
html = re.sub('<a.*?>|</a>','',html)
print(html)
results2 = re.findall('<li.*?>(.*?)</li>',html,re.S)
for result in results2:
    print(result.strip())