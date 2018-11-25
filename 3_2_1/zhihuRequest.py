import requests
import re

# 抓取知乎发现网页，获取标题
hearders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) '
                  'Version/5.1 Safari/534.50 '
}

r = requests.get('https://www.zhihu.com/explore', headers=hearders)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern,r.text)
print(titles)