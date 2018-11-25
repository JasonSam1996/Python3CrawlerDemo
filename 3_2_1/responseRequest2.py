import requests

r = requests.get('http://www.jianshu.com')
exit() if not r.status_code == requests.codes.forbidden else print('Request Successfully')