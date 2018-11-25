import requests
from requests_oauthlib import OAuth1

# 使用OAuth1认证的方法来进行身份认证
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY','YOUR_APP_SECRET','USER_OAUTH_TOKEN','USER_OAUTH_TOKEN_SOCRET')
r = requests.get(url,auth=auth)
print(r.status_code)