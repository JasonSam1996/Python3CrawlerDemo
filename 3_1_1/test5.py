import ssl
import urllib.request

context = ssl._create_unverified_context()
request = urllib.request.Request('https://python.org')
response = urllib.request.urlopen(request,context=context)
print(response.read().decode('utf-8'))