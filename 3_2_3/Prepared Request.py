from requests import Request,Session

url = 'http://httpbin.org/post'
data = {
    'name':'jason'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:63.0) Gecko/20100101 Firefox/63.0'
}
s = Session()
req = Request('POST',url,data=data,headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)