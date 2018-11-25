import requests

r = requests.get("https://www.taobao.com", timeout=1)
# 永久等待
r2 = requests.get("https://www.taobao.com", timeout=None)
print(r.status_code)
