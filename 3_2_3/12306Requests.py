import requests

# ssl证书验证
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)