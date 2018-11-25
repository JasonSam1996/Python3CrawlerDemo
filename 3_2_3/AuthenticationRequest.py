import requests
from requests.auth import HTTPBasicAuth

# 身份认证,无测试环境没法测试,简写方法
r = requests.get('http://locathost:5000', auth=('username', 'password'))
# HTTPBasicAuth方法
r2 = requests.get('http://locathost:5000', auth=HTTPBasicAuth('username', 'password'))
print(r.status_code)
