from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

# 有些网站在打开时就会弹出提示框，直接提示你输入用户名和密码，验证成功后才能查看页面，借助HTTPBasicAuthHandler就可以完成
username = 'username'
password = 'password'
# 由于我没有本地测试环境，无法测试
url = 'http://localhost:5000'
# 新建对象
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
