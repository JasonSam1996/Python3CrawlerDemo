import requests

# 抓取二进制数据，如图片，音频，视频
r = requests.get('https://github.com/favicon.ico')
print(r.text)
# print(r.content)
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
