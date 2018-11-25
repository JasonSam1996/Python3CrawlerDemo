from urllib.robotparser import RobotFileParser
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# 它可以根据某网站的robots.txt文件来判断一个爬取爬虫是否有权限来爬取这个网页
rp = RobotFileParser()
# 设置URL
rp.set_url('https://www.jianshu.com/robots.txt')
# 读取robots.txt文件并进行分析，一定要调用这个方法，否则接下来判断都会为false
rp.read()
print(rp.can_fetch('*', 'https://www.jianshu.com/p/3f148ba3cd07'))
print(rp.can_fetch('*', 'https://www.jianshu.com/search?q=python&page=1&type=collections'))
