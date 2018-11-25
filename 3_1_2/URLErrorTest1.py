from urllib import request,error
import ssl

context = ssl._create_unverified_context()
try:
    response = request.urlopen('https://cuiqingcai.com/index.html',context=context)
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep="\n")
except error.URLError as e:
    print(e.reason)
else:
    print("request Successfully")