import requests

headers = {
    'Cookie': 'd_c0="ALBmY4Ra0A2PTjGdDNk37jyQcWHYovlxRYs=|1530100671"; '
              'q_c1=aa8282f71dfd4601a92380427265f52e|1530100671000|1530100671000; '
              '_zap=8af15120-9662-41bb-813e-e3cc692b6ce3; tgw_l7_route=69f52e0ac392bb43ffb22fc18a173ee6; '
              '_xsrf=RFxlKZmCe0XTjE3DZDzuHs8kx7NrcV7f; '
              'capsion_ticket="2|1:0|10:1541925299|14:capsion_ticket|44:MGNhNjU3NjMyZjM4NDZmNWE5ZTkyOWNjZjI3ZWI2ZDM'
              '=|bfc447e499f7a11c9346136c7ea6c8308c3e66c704ea7c3578e436b56f4c4a8c"; '
              'z_c0="2|1:0|10:1541925306|4:z_c0|92'
              ':Mi4xaTd5RkF3QUFBQUFBc0daamhGclFEU1lBQUFCZ0FsVk51amZWWEFEd003dDJGaEY0RXVQMWdOcVRyQlVoLUN3SmRn|f2be'
              '§8bbb8741eba523718d19f9eff2bd766fc224975e658f5ab902d8333ef2d0"; tst=r; '
              '__§g§ads=ID=22d81ba4cd36782a:T=1541925373:S=ALNI_Ma6MsDZqWIdlI8vPTVnHad0IIaomw',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:63.0) Gecko/20100101 Firefox/63.0'
}

r = requests.get('https://www.zhihu.com',headers=headers)
print(r.text)