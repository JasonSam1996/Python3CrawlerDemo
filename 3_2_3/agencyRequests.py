import requests

proxies = {
    'http': '221.212.117.10:808',
    'https': '46.227.162.98:51558',
}

r = requests.get("https://www.taobao.com", proxies=proxies)
print(r.status_code)
