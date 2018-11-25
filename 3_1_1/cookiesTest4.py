import http.cookiejar,urllib.request

cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies2.txt',ignore_expires=True,ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
print(response.read().decode("utf-8"))