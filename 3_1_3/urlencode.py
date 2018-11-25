from urllib.parse import urlencode

parse = {
    'name':'germey',
    'age':22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(parse)
print(url)